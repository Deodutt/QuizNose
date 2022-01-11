#Creating ECS Cluster
resource "aws_ecs_cluster" "quiznose_cluster" {
  name = "quiznose_cluster"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
  depends_on = [aws_ecr_repository.quiznose_ecr]
}
