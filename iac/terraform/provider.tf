terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.57.0"
    }
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "4.57.0"
    }
    github = {
      source = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project.id
  region  = var.region
  zone    = var.zone
  batching {
    enable_batching = false
  }
}

provider "google-beta" {
  project = var.project.id
  region  = var.region
  zone    = var.zone
}
