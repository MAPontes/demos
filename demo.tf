provider "aws" {
  region = "eu-west-1"
  version = "~> 2.8"
}

resource "aws_sqs_queue" "cafeteria" {
  name = "cafeteria.fifo"
  fifo_queue = true
}

resource "aws_sns_topic" "coffe" {
  name = "coffe-update"
}
