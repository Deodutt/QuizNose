# Reference
# https://medium.com/@bradford_hamilton/deploying-containers-on-amazons-ecs-using-fargate-and-terraform-part-2-2e6f6a3a957f
#Security Group for Load Balancer
resource "aws_security_group" "quiznose_load_balancer_sg" {
  name        = "quiznose_lb_SG"
  description = "security group for load balancer"
  vpc_id      = aws_vpc.main.id
  tags = {
    Name = "Quiznose Load Balancer Security Group"
  }
}

resource "aws_security_group_rule" "quiznose_ingress_lb" {
  type              = "ingress"
  description       = "Allow port 80 inbound traffic from any IPv4"
  protocol          = "tcp"
  from_port         = 80
  to_port           = 80
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.quiznose_load_balancer_sg.id
}

resource "aws_security_group_rule" "quiznose_egress_lb" {
  type              = "egress"
  description       = "Allow all outbound traffic"
  protocol          = "-1"
  from_port         = 0
  to_port           = 0
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.quiznose_load_balancer_sg.id
}


resource "aws_alb" "quiznose_alb" {
  name            = "quiznose-load-balancer"
  subnets         = [aws_subnet.public1.id, aws_subnet.public2.id]
  security_groups = [aws_security_group.quiznose_load_balancer_sg.id]
}

resource "aws_alb_target_group" "quiznose_target_group" {
  name        = "quiznosetargetgroup"
  port        = 80
  protocol    = "HTTP"
  vpc_id      = aws_vpc.main.id
  target_type = "ip"
  depends_on  = [aws_alb.quiznose_alb]

  health_check {
    healthy_threshold   = "3"
    interval            = "30"
    protocol            = "HTTP"
    matcher             = "200"
    timeout             = "3"
    path                = var.health_check_path
    unhealthy_threshold = "2"
  }
}

# Redirect all traffic from the ALB to the target group
resource "aws_alb_listener" "quiznose_listener" {
  load_balancer_arn = aws_alb.quiznose_alb.id
  port              = 80
  protocol          = "HTTP"

  default_action {
    target_group_arn = aws_alb_target_group.quiznose_target_group.id
    type             = "forward"
  }
}

