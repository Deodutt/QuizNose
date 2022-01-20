#ECS
resource "aws_cloudwatch_metric_alarm" "quiznose_ecs_cpu_alarm" {
  alarm_name          = "QuizNose ECS CPU Utilization"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "2"
  metric_name         = "CPUUtilization" #The CPU units used by tasks in the resource that is specified by the dimension set that you're using.
  namespace           = "AWS/ECS"        #needed to select ecs fargate
  period              = "60"             #60 seconds
  statistic           = "Average"
  threshold           = "5"
  alarm_description   = "This metric monitors ECS CPU Utilization"
  alarm_actions       = [aws_sns_topic.quiznose_sns.arn]
  dimensions = {
    "ServiceName" = var.service_name
    "ClusterName" = var.cluster_name
  }
  depends_on = [aws_sns_topic.quiznose_sns]
}

resource "aws_cloudwatch_metric_alarm" "quiznose_ecs_memory_alarm" {
  alarm_name          = "QuizNose ECS Memeory Utilization"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "2"
  metric_name         = "MemoryUtilization" #The memory being used by tasks in the resource that is specified by the dimension set that you're using.
  namespace           = "AWS/ECS"           #needed to select ecs fargate
  period              = "60"                #60 seconds
  statistic           = "Average"
  threshold           = "5" #Percent
  alarm_description   = "This metric monitors ECS Memeory Utilization"
  alarm_actions       = [aws_sns_topic.quiznose_sns.arn]
  dimensions = {
    "ServiceName" = var.service_name
    "ClusterName" = var.cluster_name
  }
  depends_on = [aws_sns_topic.quiznose_sns]
}


#Database
resource "aws_cloudwatch_metric_alarm" "quiznose_rds_cpu_alarm" {
  alarm_name          = "QuizNose RDS CPU Utilization"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "2"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/RDS"
  period              = "60"
  statistic           = "Average"
  threshold           = "15"
  alarm_description   = "This metric monitors RDS CPU Utilization"
  alarm_actions       = [aws_sns_topic.quiznose_sns.arn]

  dimensions = {
    DBInstanceIdentifier = aws_db_instance.database.id #need to change to terraform
  }
}

resource "aws_cloudwatch_metric_alarm" "quiznose_rds_read_alarm" {
  alarm_name          = "QuizNose RDS Read I/O"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "2"
  metric_name         = "ReadIOPS" #The average number of disk read I/O operations per second.
  namespace           = "AWS/RDS"
  period              = "60"
  statistic           = "Average"
  threshold           = "5"
  alarm_description   = "This metric monitors RDS average number of disk read I/O operations per second"
  alarm_actions       = [aws_sns_topic.quiznose_sns.arn]

  dimensions = {
    DBInstanceIdentifier = aws_db_instance.database.id #need to change to terraform
  }
}

resource "aws_cloudwatch_metric_alarm" "quiznose_rds_write_alarm" {
  alarm_name          = "QuizNose RDS Write I/O"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "2"         #Amount of datapoints that must go through until the alarm goes off.
  metric_name         = "WriteIOPS" #The average number of disk write I/O operations per second.
  namespace           = "AWS/RDS"
  period              = "60"
  statistic           = "Average"
  threshold           = "75"
  alarm_description   = "This metric monitors RDS average number of disk write I/O operations per second"
  alarm_actions       = [aws_sns_topic.quiznose_sns.arn]

  dimensions = {
    DBInstanceIdentifier = aws_db_instance.database.id #need to change to terraform
  }
}

#error code 500
resource "aws_cloudwatch_metric_alarm" "quiznose_error_code_500_alarm" {
  alarm_name          = "QuizNose Error Code 500"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = "2"                     #Amount of datapoints that must go through until the alarm goes off.
  metric_name         = "${var.error_code}_500" #The average number of disk write I/O operations per second.
  namespace           = var.error_code
  period              = "10"
  statistic           = "Sum"
  threshold           = "20"
  alarm_description   = "This metric monitors Error Code 500 Sum per minute"
  alarm_actions       = [aws_sns_topic.quiznose_sns.arn]

  depends_on = [aws_cloudwatch_log_metric_filter.quiznose_error_500]
}
