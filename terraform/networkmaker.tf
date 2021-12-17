resource "aws_vpc" "Quizlette_VPC" {
    cidr_block = "192.168.0.0/16"

    tags = {
        Name = "QuizLette VPC"
    }
}

resource "aws_subnet" "public1" {
    vpc_id      = aws_vpc.Quizlette_VPC.id
    cidr_block  = "192.168.0.0/18"
    availability_zone   = "us-east-1a"
    tags = {
        Name = "Public1"
    map_public_ip_on_launch = true
    }
}

resource "aws_subnet" "public2" {
    vpc_id      = aws_vpc.Quizlette_VPC.id
    cidr_block  = "192.168.64.0/18"
    availability_zone   = "us-east-1b"
    tags = {
        Name = "Public2"
    map_public_ip_on_launch = true
    }
}

resource "aws_subnet" "private1" {
    vpc_id      = aws_vpc.Quizlette_VPC.id
    cidr_block  = "192.168.128.0/18"
    availability_zone   = "us-east-1a"
    tags = {
        Name = "private1"
    map_public_ip_on_launch = false
    }
}

resource "aws_subnet" "private2" {
    vpc_id      = aws_vpc.Quizlette_VPC.id
    cidr_block  = "192.168.192.0/18"
    availability_zone   = "us-east-1b"
    tags = {
        Name = "private2"
    map_public_ip_on_launch = false
    }
}

resource "aws_internet_gateway" "ig1" {
  vpc_id = aws_vpc.Quizlette_VPC.id
  
  tags = {
    Name = "QuizIG"
    
  }
}

resource "aws_route_table" "routetable1" {
  vpc_id = aws_vpc.Quizlette_VPC.id

  route {
  cidr_block = "0.0.0.0/0"
  gateway_id = aws_internet_gateway.ig1.id
  }

  tags = {
    "Name" = "RouteTable1"
  }
}

resource "aws_route_table" "routetable2" {
  vpc_id = aws_vpc.Quizlette_VPC.id
  route = []
  tags = {
    "Name" = "RouteTable2"
  }
}

resource "aws_route_table_association" "publicroute1" {
  subnet_id      = aws_subnet.public1.id
  route_table_id = aws_route_table.routetable1.id
}

resource "aws_route_table_association" "publicroute2" {
  subnet_id      = aws_subnet.public2.id
  route_table_id = aws_route_table.routetable1.id
}

resource "aws_route_table_association" "privateroute1" {
  subnet_id      = aws_subnet.private1.id
  route_table_id = aws_route_table.routetable2.id
}

resource "aws_route_table_association" "privateroute2" {
  subnet_id      = aws_subnet.private2.id
  route_table_id = aws_route_table.routetable2.id
}