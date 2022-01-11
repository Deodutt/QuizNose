# resource "aws_ecs_task_set" "quiznose_task_set" {
#   service         = aws_ecs_service.quiznose_service.id
#   cluster         = aws_ecs_cluster.quiznose_cluster.id
#   task_definition = aws_ecs_task_definition.quiznose_task_definition.arn

#   #   load_balancer {
#   #     target_group_arn = aws_lb_target_group.example.arn
#   #     container_name   = "mongo"
#   #     container_port   = 8080
#   #   }
# }
# # 
