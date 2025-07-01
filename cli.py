
import argparse
from utils import run_terraform

def main():
    parser = argparse.ArgumentParser(description="Deploy Azure Infra via Terraform")
    parser.add_argument("-projectname", required=True, help="Project Name")
    parser.add_argument("-location", required=True, help="Azure Region")
    parser.add_argument("-subscription", required=True, help="Azure Subscription ID")
    parser.add_argument("-github_token", required=True, help="GitHub Personal Access Token")
    parser.add_argument("-github_org", required=True, help="GitHub Organization")

    args = parser.parse_args()
    run_terraform(args.projectname, args.location, args.subscription, args.github_token, args.github_org)

if __name__ == "__main__":
    main()
