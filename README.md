# Template Python

> A cookiecutter template for Azure Devops Python projects

# Quick Start

In order to get started, it is NOT necessary to clone the git repository of the template. Instead, run the commands below:

1. Make sure `cookiecutter` is installed:

```console
python3 -m pip install --user cookiecutter
```

2. Generate new project in an interactive manner:

```console
cookiecutter gh:quara-dev/python-template-internal
```

> When running the command, you will be prompted for option values. When no value is provided, default value (displayed between `[]`) is used.

# Azure Devops Project configuration

Before pushing the first commit to remote repository, some pre-requisites must be met. 

## Azure Devops Secrets

1. Create new pip config according to your needs. For example:

```console
[global]
index-url=https://pkgs.dev.azure.com/QUARA/_packaging/quara-project/pypi/simple/
```

2. Upload pip config as a secret named `pip.conf`

## Sonarqube configuration

1. Import project from Azure Devops into Sonarqube.

2. Obtain project token from Sonarcloud.

3. Update project key in `sonar-project.properties` if required.

4. Update service connection name in `.azuredevops/pipelines/ci.yml`  is required.

## Static Web App Deployment

Documentation can be built and deployed as an azure static webapp.

Update the variable holding the API token in `.azuredevops/pipelines/cd.yml` to enable app publish.
