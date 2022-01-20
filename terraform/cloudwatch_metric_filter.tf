resource "aws_cloudwatch_log_metric_filter" "quiznose_error_500" {
  name           = "Error Code - 500"
  pattern        = "\"500 -\""
  log_group_name = aws_cloudwatch_log_group.quiznose_log_group.name
  depends_on     = [aws_cloudwatch_log_group.quiznose_log_group]

  metric_transformation {
    name      = "${var.error_code}_500" #metric name identifies this metric unique with the namespace
    namespace = var.error_code          #lets you group up similiar metrics
    value     = "1"                     #value that is published to the metric name when a pattern match occurs
  }
}
