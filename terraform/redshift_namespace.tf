resource "aws_redshiftserverless_namespace" "this" {
  namespace_name = var.redshift_namespace_name

  iam_roles = [ 
    aws_iam_role.this.arn
  ]
}