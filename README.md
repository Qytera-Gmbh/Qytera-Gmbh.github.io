# Qytera Documentation Hub

Everything here is based on [mkdocs](https://www.mkdocs.org).

## Setup

Run the following commands to setup everything:
```sh
python -m venv && source venv/bin/activate
pip install -r requirements.txt
```

If you want to work with videos, you should probably install [`ffmpeg`](https://ffmpeg.org/) as well.
In the `scripts` directory, there is a useful script for generating video thumbnails.

### New Project

To create a new project, run the following command:

```sh
python docs.py setup-project <project-name>
```
This will create a new project called `<project-name>` inside the `projects` directory.

## Usage

From inside your project's directory, run the following command to view your documentation using a live-reloading docs server:

```sh
mkdocs serve
```

Whenever you modify `mkdocsLocal.yml` inside your project's directory, you should run the following command to update the *automatically generated* `mkdocs.yml` YAML file used by `mkdocs`:

```sh
python docs.py update-project <project-name>
```

Apart from that, you can freely write your documentation inside the project's directory.

> **Note**
> Make sure to checkout [the `mkdocs` reference](https://squidfunk.github.io/mkdocs-material/reference/) on how to use its many features.
