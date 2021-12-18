resource "aws_db_instance" "mydb" {
  allocated_storage    = 20
  engine               = "mysql"
  instance_class       = "db.t2.micro"
  multi_az             = true
  name                 = "mydb"
  username             = "testtest" ##add your own
  password             = "testtest" #add your own
  skip_final_snapshot  = true
  vpc_security_group_ids = [aws_security_group.DB_PUBLIC.id]
  db_subnet_group_name   = aws_db_subnet_group.mysqlsubnet.id
}

resource "aws_db_subnet_group" "mysqlsubnet" {
  name       = "mysqldb"
  subnet_ids = [aws_subnet.public1.id, aws_subnet.public2.id]

  tags = {
    Name = "My DB subnet group"
  }
}

resource "aws_security_group" "DB_PUBLIC" {
  name        = "DBtoPublic"
  description = "Allow all to DB"
  vpc_id      = aws_vpc.Quizlette_VPC.id

  ingress {
    description      = "TLS from VPC"
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_public"
  }
}