terraform {
  required_providers {
    github = {
      source = "integrations/github"
      version = "~> 5.0"
    }
  }

  backend "gcs" {
    bucket = "terraform-projects-storage"
    prefix = "terraform/state"
    credentials = "credential.json"
  }
}