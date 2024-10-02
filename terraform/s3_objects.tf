resource "aws_s3_object" "this" {
  for_each = {
    for index, s3_object in var.s3_objects : s3_object.key => s3_object
  }

  bucket = aws_s3_bucket.this.bucket

  key    = each.value.key
  source = each.value.source

  force_destroy = true
}
