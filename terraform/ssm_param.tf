resource "aws_ssm_parameter" "db_user" {
  name      = "/QUIZNOSE/DB_USER"
  type      = "SecureString"
  value     = "admin"
  overwrite = true
}

resource "aws_ssm_parameter" "db_pass" {
  name      = "/QUIZNOSE/DB_PASS"
  type      = "SecureString"
  value     = "KuraLabs#123"
  overwrite = true
}

resource "aws_ssm_parameter" "api_key" {
  name      = "/QUIZNOSE/API_KEY"
  type      = "SecureString"
  value     = "at_zmz5m4BQ9kegkMqfGaTujPCCUD135"
  overwrite = true
}

resource "aws_ssm_parameter" "email_user" {
  name      = "/QUIZNOSE/MAIL_USER"
  type      = "SecureString"
  value     = "Kuralabs123"
  overwrite = true
}

resource "aws_ssm_parameter" "email_pass" {
  name      = "/QUIZNOSE/MAIL_PASS"
  type      = "SecureString"
  value     = "quiznose.notification@gmail.com"
  overwrite = true
}


