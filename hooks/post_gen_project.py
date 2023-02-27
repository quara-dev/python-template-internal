"""See: https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html#using-pre-post-generate-hooks-0-7-0"""
import os
import shutil
import subprocess
import sys

HELP = """
####### Next steps ##########


1. Visit project on Azure Devops:

    {{ cookiecutter.repo_url }}


2. Add a secret file named `pip.conf` in Azure Devops Library:


3. Import project in sonarqube:

    https://sonar.quara.cloud


4. Add git origin remote:
    $ git remote add origin git@github.com:{{ cookiecutter.repo_org }}/{{ cookiecutter.repo_name }}.git


5. Push next branch:

    $ git push -u origin next


6. Push main branch:

    $ git checkout main
    $ git push -u origin main


7. Start developping on a new branch:

    $ git checkout -b feat/my_feature_branch
"""

CLI = "{{ cookiecutter.command_line_interface }}".lower()

if CLI == "no command-line interface":
    shutil.rmtree("src/{{ cookiecutter.project_slug }}/cli")
    os.remove("src/{{ cookiecutter.project_slug }}/__main__.py")
    os.remove("tests/e2e/test_cli.py")
elif CLI == "argparse":
    os.remove("src/{{ cookiecutter.project_slug }}/cli/app.click.py")
    os.remove("src/{{ cookiecutter.project_slug }}/cli/app.typer.py")
    shutil.move(
        "src/{{ cookiecutter.project_slug }}/cli/app.argparse.py",
        "src/{{ cookiecutter.project_slug }}/cli/app.py",
    )
elif CLI == "click":
    os.remove("src/{{ cookiecutter.project_slug }}/cli/app.argparse.py")
    os.remove("src/{{ cookiecutter.project_slug }}/cli/app.typer.py")
    shutil.move(
        "src/{{ cookiecutter.project_slug }}/cli/app.click.py",
        "src/{{ cookiecutter.project_slug }}/cli/app.py",
    )
elif CLI == "typer":
    os.remove("src/{{ cookiecutter.project_slug }}/cli/app.argparse.py")
    os.remove("src/{{ cookiecutter.project_slug }}/cli/app.click.py")
    shutil.move(
        "src/{{ cookiecutter.project_slug }}/cli/app.typer.py",
        "src/{{ cookiecutter.project_slug }}/cli/app.py",
    )

subprocess.check_call([sys.executable, "./scripts/install.py", "--all"])
project_python = subprocess.check_output([sys.executable, "./scripts/install.py", "--show-python-path"]).strip().decode()
subprocess.check_call([project_python, "-m", "invoke", "requirements"])

if {{cookiecutter.init_git_repo}}:
    process = subprocess.run(
        ["git", "init"], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE
    )
    if process.returncode != 0:
        print(process.stderr.decode(), file=sys.stderr)
        sys.exit(1)
    subprocess.check_call(["git", "checkout", "-b", "main"], stdout=subprocess.DEVNULL)
    subprocess.check_call(["git", "add", "."], stdout=subprocess.DEVNULL)
    subprocess.check_call(
        [
            "git",
            "commit",
            "-m",
            "chore(project): initialize project layout and configured development tools",
        ],
        stdout=subprocess.DEVNULL,
    )
    subprocess.check_call(["git", "checkout", "-b", "next"], stdout=subprocess.DEVNULL)
    subprocess.check_call(["git", "--no-pager", "log", "--stat"])
    print(HELP)
