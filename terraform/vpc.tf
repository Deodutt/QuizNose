resource "aws_vpc" "main" {
  cidr_block           = "192.168.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name = "Quiznose VPC"
  }
}

resource "aws_subnet" "public1" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "192.168.0.0/18"
  availability_zone       = "${var.region}a"
  map_public_ip_on_launch = true
  depends_on              = [aws_vpc.main]

  tags = {
    Name = "Quiznose Public Subnet 1"
  }
}

resource "aws_subnet" "public2" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "192.168.64.0/18"
  availability_zone       = "${var.region}b"
  map_public_ip_on_launch = true
  depends_on              = [aws_vpc.main]

  tags = {
    Name = "Quiznose Public Subnet 2"
  }
}

resource "aws_subnet" "private1" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "192.168.128.0/18"
  availability_zone       = "${var.region}a"
  map_public_ip_on_launch = false
  depends_on              = [aws_vpc.main]

  tags = {
    Name = "Quiznose Private Subnet 1"
  }
}


resource "aws_subnet" "private2" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "192.168.192.0/18"
  availability_zone       = "${var.region}b"
  map_public_ip_on_launch = false
  depends_on              = [aws_vpc.main]

  tags = {
    Name = "Quiznose Private Subnet 2"
  }
}


#Create Internet gateway
resource "aws_internet_gateway" "igw" {
  vpc_id     = aws_vpc.main.id
  depends_on = [aws_vpc.main]

  tags = {
    Name = "Quiznose Internet Gateway"
  }
}


# Elastic IP for Nat Gateway
resource "aws_eip" "nat_elastic_ip" {
  vpc = true
  tags = {
    "Name" = "Quiznose Elastic IP"
  }
}


#Create NAT Gateway
resource "aws_nat_gateway" "nat_private" {
  allocation_id = aws_eip.nat_elastic_ip.id
  subnet_id     = aws_subnet.public1.id
  depends_on    = [aws_subnet.public1]

  tags = {
    "Name" = "Quiznose NAT Gateway"
  }
}


#Create Public and Private Route Table
resource "aws_route_table" "routetable_public" {
  vpc_id     = aws_vpc.main.id
  depends_on = [aws_vpc.main, aws_internet_gateway.igw]

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    "Name" = "Quiznose RouteTable Public"
  }
}

resource "aws_route_table" "routetable_private" {
  vpc_id     = aws_vpc.main.id
  depends_on = [aws_vpc.main, aws_nat_gateway.nat_private]

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_private.id
  }

  tags = {
    "Name" = "Quiznose RouteTable Private"
  }
}


#Create Route table association
resource "aws_route_table_association" "publicroute1" {
  subnet_id      = aws_subnet.public1.id
  route_table_id = aws_route_table.routetable_public.id
  depends_on     = [aws_route_table.routetable_public]
}

resource "aws_route_table_association" "publicroute2" {
  subnet_id      = aws_subnet.public2.id
  route_table_id = aws_route_table.routetable_public.id
  depends_on     = [aws_route_table.routetable_public]
}

resource "aws_route_table_association" "privateroute1" {
  subnet_id      = aws_subnet.private1.id
  route_table_id = aws_route_table.routetable_private.id
  depends_on     = [aws_route_table.routetable_private]
}

resource "aws_route_table_association" "privateroute2" {
  subnet_id      = aws_subnet.private2.id
  route_table_id = aws_route_table.routetable_private.id
  depends_on     = [aws_route_table.routetable_private]
}
