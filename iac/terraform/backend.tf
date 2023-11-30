terraform {
  backend "gcs" {
    bucket = "terraform-projects-storage"
    prefix = "terraform/state"
#    credentials = "credential.json"
  }
}
