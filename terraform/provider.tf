terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "3.69.0"
      
    }
  }
}

provider "aws" {
  # Configuration options
  region = "us-east-1"
}