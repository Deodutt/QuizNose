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
      Application  = "Quiznose"
      Team_Number  = "3"
      Organization = "Kura Labs"
    }
  }
}

terraform {
  backend "s3" {
    bucket = "quiznose-s3"
    key    = "terraform/terraform.tfstate"
    region = "us-east-1"
  }
}
