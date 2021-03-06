resource "aws_db_instance" "database" {
  multi_az            = true
  instance_class      = "db.t2.micro"
  name                = "quiznose_mysql"
  username            = "admin"
  password            = aws_ssm_parameter.db_pass.value
  identifier          = "quiznose"
  publicly_accessible = true

  allocated_storage      = 10
  engine                 = "mysql"
  engine_version         = "8.0.23"
  skip_final_snapshot    = true
  vpc_security_group_ids = [aws_security_group.quiznose_database_sg.id]
  db_subnet_group_name   = aws_db_subnet_group.database_subnet_groups.id
  tags = {
    "Name" = "Quiznose Database"
  }

  depends_on = [aws_ssm_parameter.db_user, aws_ssm_parameter.db_pass, aws_ssm_parameter.api_key, aws_ssm_parameter.email_user, aws_ssm_parameter.email_pass, aws_db_subnet_group.database_subnet_groups, aws_security_group.quiznose_database_sg]
}


resource "aws_db_subnet_group" "database_subnet_groups" {
  name       = "quiznose_subnet_group"
  subnet_ids = [aws_subnet.public1.id, aws_subnet.public2.id]

  tags = {
    Name = "Quiznose Database Subnet Group"
  }
}

#Security Group for RDS
resource "aws_security_group" "quiznose_database_sg" {
  name        = "quiznose_db_sg"
  description = "security group for quiznose database"
  vpc_id      = aws_vpc.main.id

  tags = {
    Name = "Quiznose Database Security Group"
  }
}

resource "aws_security_group_rule" "quiznose_database_ingress" {
  type              = "ingress"
  description       = "Allow inbound traffic from port 3306"
  protocol          = "tcp"
  from_port         = 3306
  to_port           = 3306
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.quiznose_database_sg.id
}

resource "aws_security_group_rule" "quiznose_database_egress" {
  type              = "egress"
  description       = "All outbound traffic"
  protocol          = "-1"
  from_port         = 80
  to_port           = 80
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.quiznose_database_sg.id
}
