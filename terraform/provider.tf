terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.69.0"

    }
  }
}


# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
  default_tags {
    tags = {
      Application  = var.application_name
      Team_Number  = "3"
      Organization = "Kura Labs"
    }
  }
}
