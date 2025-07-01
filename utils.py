import subprocess
import os
import tempfile

TEMPLATE_REPO = "https://github.com/OnCloudAcademy/common-infra-template.git"

def run_terraform(project_name, location, subscription_id, github_token, github_org):
    # Create a temporary directory (auto-cleans when done)
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"📦 Cloning into temporary directory: {temp_dir}")

        # Clone the Terraform repo into the temp directory
        subprocess.run(["git", "clone", TEMPLATE_REPO, temp_dir], check=True)

        # Change to the cloned directory
        os.chdir(temp_dir)

        # Set the Azure subscription (optional but useful)
        subprocess.run(["az", "account", "set", "--subscription", subscription_id], check=True)

        # Initialize Terraform
        subprocess.run(["terraform", "init"], check=True)

        # Apply Terraform using provided variables
        subprocess.run([
            "terraform", "apply",
            "-auto-approve",
            f"-var=project_name={project_name}",
            f"-var=location={location}",
            f"-var=subscription_id={subscription_id}",
            f"-var=github_token={github_token}",
            f"-var=github_org={github_org}"
        ], check=True)

        # Temporary directory will be auto-deleted after this block