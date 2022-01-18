resource "aws_iam_role" "task_def_role" {
  name = "task_def_role"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
            "Effect": "Allow",
            "Action": [
                "ssm:ListCommands",
                "ssm:DescribeInstancePatches",
                "ssm:GetParameter",
                "ssm:GetMaintenanceWindowExecutionTaskInvocation",
                "ssm:DescribeAutomationExecutions",
                "ssm:GetMaintenanceWindowTask",
                "ssm:DescribeAutomationStepExecutions",
                "ssm:GetConnectionStatus",
                "ssm:GetMaintenanceWindowExecutionTask",
                "ssm:GetOpsItem",
                "ssm:GetMaintenanceWindowExecution",
                "ssm:GetParameters",
                "ssm:GetOpsMetadata",
                "ssm:ListOpsItemRelatedItems",
                "ssm:DescribeOpsItems",
                "ssm:DescribeEffectivePatchesForPatchBaseline",
                "ecs:*",
                "ssm:GetServiceSetting",
                "ssm:DescribeAssociationExecutions",
                "ssm:DescribeDocumentPermission",
                "ssm:ListCommandInvocations",
                "ssm:GetAutomationExecution",
                "ssm:GetDefaultPatchBaseline",
                "ssm:DescribeDocument",
                "ssm:GetPatchBaselineForPatchGroup",
                "ssm:PutConfigurePackageResult",
                "ssm:GetManifest",
                "ssm:DescribeInstancePatchStates",
                "ssm:DescribeInstancePatchStatesForPatchGroup",
                "ssm:GetDocument",
                "ssm:GetInventorySchema",
                "ssm:GetParametersByPath",
                "ssm:GetMaintenanceWindow",
                "ssm:DescribeInstanceAssociationsStatus",
                "ssm:DescribeAssociationExecutionTargets",
                "ssm:GetPatchBaseline",
                "ssm:DescribeInstanceProperties",
                "ssm:DescribeAssociation",
                "ssm:ListOpsItemEvents",
                "ssm:GetDeployablePatchSnapshotForInstance",
                "ssm:GetParameterHistory",
                "ssm:DescribeEffectiveInstanceAssociations",
                "ssm:DescribeInventoryDeletions",
                "ssm:GetInventory",
                "ssm:GetOpsSummary",
                "ssm:DescribeActivations",
                "ssm:GetCommandInvocation",
                "ssm:DescribeInstanceInformation",
                "ssm:ListTagsForResource",
                "ssm:DescribeDocumentParameters",
                "ecr:*",
                "ssm:GetCalendarState",
                "ssm:DescribeAvailablePatches"
            ],
            "Resource": "*"
        }
    ]
  })

}
