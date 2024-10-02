resource "aws_glue_catalog_database" "this" {
  name = var.glue_database_name
}