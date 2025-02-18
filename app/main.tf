# Specifying Docker provider

terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    },
      aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
}

provider "aws" {
  region  = "us-east-1"
  profile = "jasmine.dillard"
}

# Define the Docker container data source
data "docker_image" "local_image" {
  name = "blockchain-explorer_backend"
}

# Define the Docker container resource
resource "docker_container" "blockchain-explorer" {
  name  = "blockchain-explorer"
  image = data.docker_image.local_image.name

  # Expose port 5000 for Flask app
  ports {
    internal = 5000
    external = 5000
  }
}

resource "aws_instance" "MyWebServer" {
  ami           = "ami-04b4f1a9cf54c11d0"
  instance_type = "t2.micro"

  tags = {
    Name = "app"
  }
}

# Terraform provisioner to wait for container to be ready
resource "null_resource" "wait_for_container" {
  depends_on = [docker_container.pure_app]
  # Local-exec provisioner to wait for container to be ready
  provisioner "local-exec" {
    command = "sleep 10"
  }
}
