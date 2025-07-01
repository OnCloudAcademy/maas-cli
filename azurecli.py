import argparse
import os
import shutil
import subprocess
import tempfile
from utils import clone_repo, generate_tfvars, validate_az_login

COMMON_INFRA_REPO = "https://github.com/OnCloudAcademy/common-infra-template.git"

def run_terraform(directory):
    os.chdir(directory)
    subprocess.run(["terraform", "init"], check=True)
    subprocess.run(["terraform", "plan", "-var-file=terraform.tfvars.json"], check=True)
    subprocess.run(["terraform", "apply", "-auto-approve", "-var-file=terraform.tfvars.json"], check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MAAS CLI")
    parser.add_argument("-create", action="store_true", help="Create infrastructure")
    parser.add_argument("-projectname", required=True, help="Project name")
    parser.add_argument("-subscription", required=True, help="Azure Subscription ID")

    args = parser.parse_args()

    if args.create:
        validate_az_login(args.subscription)

        temp_dir = tempfile.mkdtemp(prefix=f"maas-{args.projectname}-")
        clone_repo(COMMON_INFRA_REPO, temp_dir)

        tfvars_path = os.path.join(temp_dir, "terraform.tfvars.json")
        generate_tfvars(tfvars_path, {
            "project_name": args.projectname,
            "subscription_id": args.subscription
        })

        run_terraform(temp_dir)

        print(f"\n✅ Infrastructure deployed from: {temp_dir}")
