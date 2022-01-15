# #creating task defintion
resource "aws_ecs_task_definition" "quiznose_task_definition" {
  family                   = "quiznose"
  requires_compatibilities = ["FARGATE"]
  task_role_arn            = "arn:aws:iam::252544977596:role/ecsTaskExecutionRole"
  execution_role_arn       = "arn:aws:iam::252544977596:role/ecsTaskExecutionRole"
  network_mode             = "awsvpc"
  cpu                      = 1024 #1gb 
  memory                   = 2048 #2gb
  depends_on               = [aws_ecs_cluster.quiznose_cluster]

  # This will use images pushed to ECR
  #Image is the URI
  #containerport and hostport must match
  container_definitions = <<TASK_DEFINITION
[
  {
    "name": "quiznose-app",
    "image": "252544977596.dkr.ecr.us-east-1.amazonaws.com/quiznose:latest",
    "cpu": 1024,
    "memory": 2048,
    "essential": true,
    "portMappings": [
    {
        "containerPort": 5000,
        "hostPort": 5000
    }
    ],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "${aws_cloudwatch_log_group.quiznose_log_group.name}",
        "awslogs-stream-prefix": "quiznose",
        "awslogs-region": "us-east-1"
      }
    }

  }
]
TASK_DEFINITION

  runtime_platform {
    operating_system_family = "LINUX"
  }
}
