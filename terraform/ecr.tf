#Creating ECR Repository
resource "aws_ecr_repository" "quiznose_ecr" {
  name = "quiznose"
}
