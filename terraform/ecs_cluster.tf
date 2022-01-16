#Creating ECS Cluster
resource "aws_ecs_cluster" "quiznose_cluster" {
  name = "${var.application_name}_cluster"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
  depends_on = [aws_ecr_repository.quiznose_ecr]
}
