resource "aws_glue_crawler" "example" {
  role          = aws_iam_role.this.arn
  database_name = aws_glue_catalog_database.this.name

  name = var.glue_crawler_name

  s3_target {
    path = "s3://${aws_s3_bucket.this.bucket}/trans"
  }
}
