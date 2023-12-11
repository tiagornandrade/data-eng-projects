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
  credentials = var.credential
  project = var.project.id
  region  = var.region
}

provider "google-beta" {
  project = var.project.id
  region  = var.region
  zone    = var.zone
}
