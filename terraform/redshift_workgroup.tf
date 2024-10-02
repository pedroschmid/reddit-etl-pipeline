resource "aws_redshiftserverless_workgroup" "this" {
  namespace_name = aws_redshiftserverless_namespace.this.id
  subnet_ids     = values(aws_subnet.this)[*].id

  workgroup_name = var.redshift_workgroup_name
}
