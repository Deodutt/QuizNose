resource "aws_s3_bucket" "quiznose_s3" {
  bucket        = "quiznose-s3"
  acl           = "private"
  force_destroy = true

  versioning {
    enabled    = true
    mfa_delete = false
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    Name = "Quiznose S3"
  }

}

