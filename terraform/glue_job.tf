resource "aws_glue_job" "this" {
  name              = var.glue_job_name
  role_arn          = aws_iam_role.this.arn
  glue_version      = "4.0"
  worker_type       = "Standard"
  number_of_workers = 10

  command {
    script_location = "s3://${aws_s3_bucket.this.bucket}/scripts/aws_glue_script.py"
  }
}
