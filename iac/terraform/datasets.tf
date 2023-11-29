resource "google_bigquery_dataset" "dataset" {
  count = length(var.datasets)
  dataset_id = var.datasets[count.index].name
  project = var.project.id
}
