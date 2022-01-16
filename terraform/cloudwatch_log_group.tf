resource "aws_cloudwatch_log_group" "quiznose_log_group" {
  name = "QuizNose"

  tags = {
    Environment = "production"
    Application = "QuizNose"
  }
}
