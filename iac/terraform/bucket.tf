resource "google_storage_bucket" "pipeline-dataflow-templates" {
  name = "pipeline-dataflow-templates"
  project = var.project.id
  location = "us"
}

