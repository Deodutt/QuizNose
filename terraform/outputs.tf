# output "rds_endpoint" {
#   value = aws_db_instance.database.endpoint
# }

output "URL_TO_APPLICATION" {
  value = aws_alb.quiznose_alb.dns_name
}
