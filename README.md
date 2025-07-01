
# maas-cli

This CLI triggers a Terraform deployment using a shared infrastructure template.

## ✅ Requirements

- Python 3.8+
- Azure CLI (`az login` and `az account set`)
- Terraform CLI installed
- Git installed

## 🚀 Usage

```bash
python cli.py -projectname myproject -location eastus -subscription <subscription-id>
```

This will:
- Clone the common-infra-template repo
- Set Azure subscription
- Run `terraform init` and `terraform apply` with your inputs
