# Qytera Documentation Hub

Everything here is based on [mkdocs](https://www.mkdocs.org).

## Setup

It is highly recommended to use virtual Python environments instead of global ones:

```sh
python -m venv venv
```

To activate the virtual environment, run the following commands:

- Windows:

```sh
.\venv\Scripts\activate
```

- Unix:

```sh
source venv/bin/activate
```

From then on, every python package will be installed into the `venv` directory without modifying your global python configuration.

Run the following commands to setup everything (either inside your virtual environment, or outside/globally on your machine):

```sh
pip install -r requirements.txt
```

#### ffmpeg

If you want to work with videos, you should probably install [`ffmpeg`](https://ffmpeg.org/) as well.
In the `scripts` directory, there is a useful script for generating video thumbnails.

#### VS Code

The following plugins are recommended when using VS Code:

- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [YAML Red Hat](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)

### Existing Project

> **Note**
> Make sure you have [activated your virtual environment](#setup)!

To prepare an existing project, simply run the following command:

```sh
python docs.py update-project path/to/project/dir
```

This will create a file called `mkdocs.yml` inside the project's directory, which can then be used to view the page as described [here](#usage).

### New Project

> **Note**
> Make sure you have [activated your virtual environment](#setup)!

To create a new project, run the following command:

```sh
python docs.py setup-project <project-name>
```

This will create a new project called `<project-name>` inside the `projects` directory.

> **Warning**
> Make sure that you set up a corresponding GitHub action as well.
> Have a look at the existing project actions and copy & paste one for your new project.

## Usage

> **Note**
> Make sure you have [activated your virtual environment](#setup)!

From inside your project's directory, run the following command to view your documentation using a live-reloading docs server:

```sh
mkdocs serve
```

Whenever you modify `mkdocsLocal.yml` inside your project's directory, you should run the following command to update the _automatically generated_ `mkdocs.yml` YAML file used by _mkdocs_:

```sh
python docs.py update-project path/to/project/dir
```

Apart from that, you can freely write your documentation inside the project's directory.

> **Note**
> Make sure to checkout [the _mkdocs_ reference](https://squidfunk.github.io/mkdocs-material/reference/) on how to use its many features.

## Deployment

You don't have to do any manual deploying.
Everything is based on GitHub actions: If you modify your project's documentation and push the changes, your GitHub action will automatically redeploy your project's documentation.
