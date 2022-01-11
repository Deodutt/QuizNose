# output "rds_endpoint" {
#   value = aws_db_instance.database.endpoint
# }

# output "ecr_repository_url" {
#   value = aws_ecr_repository.quiznose_ecr.repository_url
# }

output "URL_TO_APPLICATION" {
  value = aws_alb.quiznose_alb.dns_name
}
