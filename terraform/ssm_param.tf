resource "aws_ssm_parameter" "db_pass" {
  name  = "/QUIZNOSE/DB_PASS"
  type  = "SecureString"
  value = "KuraLabs#123"
  # value = ${{DB_PASS}}
}

resource "aws_ssm_parameter" "api_key" {
  name  = "/QUIZNOSE/API_KEY"
  type  = "SecureString"
  value = "at_zmz5m4BQ9kegkMqfGaTujPCCUD135"
  # value = ${{API_KEY}}
}

# resource "aws_ssm_parameter" "email_pass" {
#   name  = "/QUIZNOSE/EMAIL_PASS"
#   type  = "SecureString"
#   # value = ${{EMAIL_PASS}}
# }

# resource "aws_ssm_parameter" "email_user" {
#   name  = "/QUIZNOSE/ENAIL_USER"
#   type  = "SecureString"
#   # value = ${{EMAIL_USER}}
# }
