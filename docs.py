import os.path
import shutil
from enum import Enum
from pathlib import Path
from typing import Optional, Any, List, Dict

import logging
import inspect

import fire
import yaml

PATH_ASSETS = "docs/assets"
PATH_STYLESHEETS = "docs/stylesheets"
PATH_SECTIONS = "docs/sections"
PATH_INDEX = "docs/index.md"
PATH_YML = "mkdocs.yml"
PATH_YML_ROOT = "mkdocsRoot.yml"
PATH_YML_LOCAL = "mkdocsLocal.yml"

logger = logging.getLogger(__name__)


class Level(Enum):
    INFO = logging.INFO
    DEBUG = logging.DEBUG


root_stack_depth = 0


def _log(level: Level, text: str):
    # Subtract one for the current frame as well.
    message = f"{' ' * (len(inspect.stack(0)) - root_stack_depth - 1)} [{text}]"
    match level:
        case Level.INFO: logger.info(message)
        case Level.DEBUG: logger.debug(message)


def _quoted(value: str | List | Dict) -> str:
    return f"'{value}'" if isinstance(value, str) else value


"""
Work-around to allow loading and dumping yaml with tags in a way that the tags do not get lost.
From: https://github.com/yaml/pyyaml/issues/656
"""


class YamlType(Enum):
    SCALAR = 0
    SEQUENCE = 1
    MAPPING = 2


class Yaml:
    suffix: str
    type: YamlType
    value: Any

    def __init__(self, suffix: str, yaml_type: YamlType, value: None):
        self.suffix = f"tag:{suffix}"
        self.type = yaml_type
        self.value = value

    @staticmethod
    def construct(loader: yaml.Loader, suffix: str, node: yaml.Node):
        if isinstance(node, yaml.ScalarNode):
            constructor = loader.__class__.construct_scalar
            yaml_type = YamlType.SCALAR
        elif isinstance(node, yaml.SequenceNode):
            constructor = loader.__class__.construct_sequence
            yaml_type = YamlType.SEQUENCE
        elif isinstance(node, yaml.MappingNode):
            constructor = loader.__class__.construct_mapping
            yaml_type = YamlType.MAPPING
        else:
            raise ValueError(f"unknown node type for node {node}")
        return Yaml(suffix=suffix, yaml_type=yaml_type, value=constructor(loader, node))

    @staticmethod
    def represent(dumper: yaml.Dumper, data) -> yaml.Node:
        if data.type == YamlType.SCALAR:
            return dumper.represent_scalar(tag=data.suffix, value=data.value)
        elif data.type == YamlType.SEQUENCE:
            return dumper.represent_sequence(tag=data.suffix, sequence=data.value)
        elif data.type == YamlType.MAPPING:
            return dumper.represent_mapping(tag=data.suffix, mapping=data.value)
        else:
            raise ValueError(f"unknown data type: {data.type}")


class YamlLoader(yaml.SafeLoader):
    """
    SafeLoader on which multi-constructors are registered without influencing SafeLoader.

    Usage:
    yaml.load_all(yaml_string, Loader=TypedYamlLoader)
    """

    pass


class YamlDumper(yaml.Dumper):
    """
    Dumper on which a representer for Yaml is registered without influencing the regular Dumper.
    """

    pass


YamlLoader.add_multi_constructor("!", Yaml.construct)
YamlLoader.add_multi_constructor("tag:", Yaml.construct)
YamlDumper.add_representer(Yaml, Yaml.represent)


def _merge_into_list(new_list: List, target_list: List) -> None:
    _log(
        Level.INFO,
        f"merging list {new_list} into existing list {target_list}"
    )
    for item in new_list:
        _log(
            Level.DEBUG,
            f"inspecting {_quoted(item)}"
        )
        if isinstance(item, str):
            if item not in target_list:
                _log(
                    Level.DEBUG,
                    f"appending {_quoted(item)} to {target_list}"
                )
                target_list.append(item)
        if isinstance(item, list):
            raise ValueError(
                f"cannot merge list item {item} into list {target_list}")
        if isinstance(item, dict):
            existing_dict = None
            for existing_item in target_list:
                # Check if the existing item is a dictionary which contains at least one of the new keys.
                if isinstance(existing_item, dict) and (item.keys() & existing_item.keys()):
                    existing_dict = existing_item
                    break
            if existing_dict is None:
                _log(
                    Level.DEBUG,
                    f"appending {_quoted(item)} to {target_list}"
                )
                target_list.append(item)
            else:
                _merge_into_dict(item, existing_dict)


def _merge_into_dict(new_dict: Dict, target_dict: Dict) -> None:
    _log(
        Level.INFO,
        f"merging dict {new_dict} into existing dict {target_dict}"
    )
    for key, new_value in new_dict.items():
        _log(
            Level.DEBUG,
            f"inspecting {{{_quoted(key)}: {_quoted(new_value)}}}"
        )
        if key not in target_dict:
            _log(
                Level.DEBUG,
                f"inserting {{{_quoted(key)}: {_quoted(new_value)}}} into {target_dict}"
            )
            target_dict[key] = new_value
        else:
            existing_value = target_dict[key]
            if isinstance(new_value, str):
                if not isinstance(existing_value, str):
                    raise ValueError(
                        f"cannot merge value {new_value}: {existing_value} is not a scalar"
                    )
                _log(
                    Level.DEBUG,
                    f"replacing {_quoted(target_dict[key])} with {_quoted(new_value)}"
                )
                target_dict[key] = new_value
            elif isinstance(new_value, list):
                if not isinstance(existing_value, list):
                    raise ValueError(
                        f"cannot merge value {new_value}: {existing_value} is not a sequence"
                    )
                _merge_into_list(new_value, existing_value)
            elif isinstance(new_value, dict):
                _merge_into_dict(new_value, existing_value)


def _update_yml(
    project_dir: str | os.PathLike[str], template_dir: str | os.PathLike[str]
):
    _log(
        Level.INFO,
        f"updating project directory {_quoted(project_dir)} based on templates from template directory {_quoted(template_dir)}"
    )
    template_yaml_root = Path(template_dir).joinpath(PATH_YML_ROOT)
    if not os.path.exists(template_yaml_root):
        raise ValueError(
            f"root YAML file {PATH_YML_ROOT} missing in template directory"
        )
    project_yaml_local = Path(project_dir).joinpath(PATH_YML_LOCAL)
    if not os.path.exists(project_yaml_local):
        template_yaml_local = Path(template_dir).joinpath(PATH_YML_LOCAL)
        if not os.path.exists(template_yaml_local):
            raise ValueError(
                f"local YAML file {PATH_YML_LOCAL} missing in template directory"
            )
        shutil.copyfile(src=template_yaml_local, dst=project_yaml_local)
    yaml_root = None
    yaml_local = None
    with open(template_yaml_root, "r", encoding="utf-8") as yaml_file:
        yaml_root = yaml.load(yaml_file, Loader=YamlLoader)
    with open(project_yaml_local, "r", encoding="utf-8") as yaml_file:
        yaml_local = yaml.load(yaml_file, Loader=YamlLoader)

    _merge_into_dict(yaml_local, yaml_root)

    with open(Path(project_dir).joinpath(PATH_YML), "w", encoding="utf-8") as yaml_file:
        yaml_file.writelines(
            [
                "# ======================= #\n",
                "# GENERATED AUTOMATICALLY #\n",
                "# DO NOT MODIFY!          #\n",
                "# ======================= #\n",
            ]
        )
    with open(Path(project_dir).joinpath(PATH_YML), "a", encoding="utf-8") as yaml_file:
        yaml.dump(
            data=dict(sorted(yaml_root.items())),
            stream=yaml_file,
            indent=2,
            Dumper=YamlDumper,
        )


def update_project(
    project_dir: str | os.PathLike[str],
    template_dir: str | os.PathLike[str] = "template/",
    update_assets: Optional[bool] = True,
    update_stylesheets: Optional[bool] = True,
    update_yml: Optional[bool] = True,
) -> None:
    """
    Updates an existing project based on the content in the provided template directory. Existing files will be
    overwritten with their counterparts from the template directory. New files will be added to the corresponding
    directories. New directories will be created automatically.

    :param project_dir: the project directory to update
    :param template_dir: the template directory to pull content from
    :param update_assets: True to update assets, False to skip updating assets
    :param update_stylesheets: True to update stylesheets, False to skip updating stylesheets
    :param update_yml: True to update mkdocs.yml, False to skip updating mkdocs.yml
    """
    logging.basicConfig(
        filename="update.log",
        encoding="utf-8",
        level=logging.DEBUG
    )
    global root_stack_depth
    root_stack_depth = len(inspect.stack(0))
    _log(
        Level.INFO,
        f"updating project with args project_dir={_quoted(project_dir)}, template_dir={_quoted(template_dir)}, update_assets={update_assets}, update_stylesheets={update_stylesheets}, update_yml={update_yml}"
    )
    if not os.path.exists(template_dir):
        raise ValueError(f"template directory does not exist: {template_dir}")
    if not os.path.exists(project_dir):
        raise ValueError(f"project directory does not exist: {project_dir}")
    if update_assets:
        shutil.copytree(
            src=Path(template_dir).joinpath(PATH_ASSETS),
            dst=Path(project_dir).joinpath(PATH_ASSETS),
            dirs_exist_ok=True,
        )
    if update_stylesheets:
        shutil.copytree(
            src=Path(template_dir).joinpath(PATH_STYLESHEETS),
            dst=Path(project_dir).joinpath(PATH_STYLESHEETS),
            dirs_exist_ok=True,
        )
    if update_yml:
        _update_yml(project_dir, template_dir)


def setup_project(
    project_name: str,
    template_dir: str | os.PathLike[str] = "template/",
    projects_dir: str | os.PathLike[str] = "projects/",
) -> None:
    """
    Creates a new project with the given name under the provided project directory. The template directory will serve
    as base for all initial files (sections, stylesheets, assets and the root YAML file).

    :param project_name: the name of the new project
    :param template_dir: the template directory to pull initial content from
    :param projects_dir: the directory where the new project directory should be created
    """
    logging.basicConfig(
        filename="setup.log",
        encoding="utf-8",
        level=logging.DEBUG
    )
    global root_stack_depth
    root_stack_depth = len(inspect.stack(0))
    _log(
        Level.INFO,
        f"setting up project with args project_name={_quoted(project_name)}, template_dir={_quoted(template_dir)}, projects_dir={_quoted(projects_dir)}"
    )
    if not os.path.exists(template_dir):
        raise ValueError(f"template directory does not exist: {template_dir}")
    project_dir = Path(projects_dir).joinpath(project_name)
    if os.path.exists(project_dir):
        raise ValueError(
            f"cannot setup project: project directory {project_dir} exists already"
        )
    os.makedirs(project_dir, exist_ok=True)
    # Create initial sections.
    shutil.copytree(
        src=Path(template_dir).joinpath(PATH_SECTIONS),
        dst=Path(project_dir).joinpath(PATH_SECTIONS),
        dirs_exist_ok=True,
    )
    shutil.copyfile(
        src=Path(template_dir).joinpath(PATH_INDEX),
        dst=Path(project_dir).joinpath(PATH_INDEX),
    )
    shutil.copyfile(
        src=Path(template_dir).joinpath(".gitignore"),
        dst=Path(project_dir).joinpath(".gitignore"),
    )
    update_project(
        project_dir=project_dir,
        template_dir=template_dir,
        update_assets=True,
        update_stylesheets=True,
        update_yml=True,
    )


if __name__ == "__main__":
    fire.Fire(
        {
            "setup-project": setup_project,
            "update-project": update_project,
        }
    )
