terraform {
  backend "s3" {
    profile = "terraform"
    region  = "us-east-1"
    bucket  = "s3-terraform-states-88qiu9"
    key     = "reddit/terraform.tfstate"
  }
}
