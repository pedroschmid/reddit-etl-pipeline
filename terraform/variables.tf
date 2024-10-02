variable "aws_profile" {
  type        = string
  description = "AWS CLI profile name used to authenticate and manage AWS resources."
}

variable "aws_region" {
  type        = string
  description = "AWS region where the resources will be deployed (e.g., us-east-1)."
}

variable "vpc_cidr" {
  type        = string
  description = "CIDR block for the VPC to define the range of IP addresses."
}

variable "subnets" {
  type = list(object({
    cidr_block        = string
    availability_zone = string
  }))
  description = "List of subnet configurations, each specifying a CIDR block and the associated availability zone."
}

variable "s3_bucket_name" {
  type        = string
  description = "Name of the S3 bucket used for storing data."
}

variable "s3_objects" {
  type = list(object({
    key    = string
    source = string
  }))
  description = "List of objects to be stored in the S3 bucket, each containing a key and a source path."
}

variable "glue_job_name" {
  type        = string
  description = "Name of the AWS Glue job to be created or managed."
}

variable "glue_job_iam_role_name" {
  type        = string
  description = "IAM role name associated with the AWS Glue job to provide necessary permissions."
}

variable "glue_database_name" {
  type        = string
  description = "Name of the Glue database where the data catalog will be stored."
}

variable "glue_crawler_name" {
  type        = string
  description = "Name of the AWS Glue crawler used to discover datasets and populate the data catalog."
}

variable "redshift_namespace_name" {
  type        = string
  description = "Name of the Redshift namespace to configure the database resources."
}

variable "redshift_workgroup_name" {
  type        = string
  description = "Name of the Redshift workgroup used to manage and scale the cluster resources."
}
