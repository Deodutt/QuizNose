resource "aws_cloudwatch_metric_alarm" "ecs_cpu_alarm" {
  alarm_name                = "quiznose ecs cpu"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "2"
  metric_name               = "CPUUtilization"
  namespace                 = "AWS/ECS"
  period                    = "120"
  statistic                 = "Average"
  threshold                 = "80"
  alarm_description         = "This metric monitors ecs cpu utilization"
}

resource "aws_cloudwatch_metric_alarm" "rds_cpu_alarm" {
  alarm_name                = "quiznose rds cpu"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "2"
  metric_name               = "CPUUtilization"
  namespace                 = "AWS/RDS"
  period                    = "120"
  statistic                 = "Average"
  threshold                 = "80"
  alarm_description         = "This metric monitors rds cpu utilization"
}

resource "aws_cloudwatch_metric_alarm" "rds_read_alarm" {
  alarm_name                = "quiznose rds cpu"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "2"
  metric_name               = "ReadIOPS"
  namespace                 = "AWS/RDS"
  period                    = "120"
  statistic                 = "Average"
  threshold                 = "80"
  alarm_description         = "This metric monitors rds average number of disk read I/O operations per second"
}
