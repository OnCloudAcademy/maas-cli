
import subprocess
import os
import shutil

TEMPLATE_REPO = "https://github.com/OnCloudAcademy/common-infra-template.git"
TEMPLATE_DIR = "common-infra-template"

def run_terraform(project_name, location, subscription_id):
    # Clone repo
    if os.path.exists(TEMPLATE_DIR):
        shutil.rmtree(TEMPLATE_DIR)
    subprocess.run(["git", "clone", TEMPLATE_REPO], check=True)

    os.chdir(TEMPLATE_DIR)

    # Set subscription (optional)
    subprocess.run(["az", "account", "set", "--subscription", subscription_id], check=True)

    # Terraform init and apply
    subprocess.run(["terraform", "init"], check=True)
    subprocess.run([
        "terraform", "apply",
        "-auto-approve",
        f"-var=project_name={project_name}",
        f"-var=location={location}"
    ], check=True)
