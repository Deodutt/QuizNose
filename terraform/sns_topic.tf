resource "aws_sns_topic" "quiznose_sns" {
  name = "${var.application_name}_sns_topic"
}

resource "aws_sns_topic_subscription" "email-target" {
  topic_arn = aws_sns_topic.quiznose_sns.arn
  protocol  = "email"
  endpoint  = "RicardoDeodutt@gmail.com" #add ssm paramater
}
