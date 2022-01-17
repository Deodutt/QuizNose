resource "aws_ssm_parameter" "db_endpoint" {
  name  = "/QUIZNOSE/DB_ENDPOINT"
  type  = "SecureString"
  value = aws_db_instance.database.address
  # "database-1.cet4jo0trfys.us-east-1.rds.amazonaws.com"
  # value = ${{DB_PASS}}
}

