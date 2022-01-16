resource "aws_ecs_service" "quiznose_service" {
  name                 = "quiznose_service"
  cluster              = aws_ecs_cluster.quiznose_cluster.id
  task_definition      = aws_ecs_task_definition.quiznose_task_definition.arn
  desired_count        = var.app_count
  launch_type          = "FARGATE"
  force_new_deployment = true

  network_configuration {
    security_groups  = [aws_security_group.quiznose_ecs_sg.id]
    subnets          = [aws_subnet.public1.id]
    assign_public_ip = true
  }

  load_balancer {
    target_group_arn = aws_alb_target_group.quiznose_target_group.id
    container_name   = "quiznose-app"
    container_port   = var.app_port
  }

  depends_on = [aws_ecs_task_definition.quiznose_task_definition]
}


#Security Group for Development EC2 Instance
resource "aws_security_group" "quiznose_ecs_sg" {
  name        = "quiznose_ecs_sg"
  description = "security group for quiznose ecs service"
  vpc_id      = aws_vpc.main.id

  tags = {
    Name = "Quiznose ECS Security Group"
  }
}

resource "aws_security_group_rule" "quiznose_ecs_ingress" {
  type              = "ingress"
  description       = "All inbound traffic"
  protocol          = "-1"
  from_port         = 80
  to_port           = 80
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.quiznose_ecs_sg.id
}

resource "aws_security_group_rule" "quiznose_ecs_egress" {
  type              = "egress"
  description       = "All outbound traffic"
  protocol          = "-1"
  from_port         = 80
  to_port           = 80
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.quiznose_ecs_sg.id
}
