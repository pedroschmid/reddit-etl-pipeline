resource "aws_subnet" "this" {
  for_each = {
    for index, subnet in var.subnets : subnet.cidr_block => subnet
  }

  vpc_id = aws_vpc.this.id

  cidr_block        = each.value.cidr_block
  availability_zone = each.value.availability_zone
}
