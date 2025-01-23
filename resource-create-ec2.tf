# resources provided by users with variables
provider "aws" {
    region = "us-west-2"
  
}

resource "aws_instance" "example" {
    ami = var.ami_value
    instance_type = var.instance_type_value
}


resource "aws_s3_bucket" "myboabucket" {
  bucket = "boabuckethyd"
  tags = {
    Name= "boabuckethyd"
    Environment = "Production"
  }
}