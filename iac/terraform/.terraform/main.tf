resource "google_service_account" "service_account" {
  account_id   = "101069861825044749052"
  display_name = "Service Account One"
}

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.57.0"
    }
  }

  backend "gcs" {}
}


provider "google" {
  project = "yams-lab-nonprod"
}