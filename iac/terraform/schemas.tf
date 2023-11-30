resource "google_bigquery_table" "accounts_users" {
  dataset_id = google_bigquery_dataset.dataset[0].dataset_id

  table_id   = "users"

  schema = [
    {
      name = "user_id"
      type = "STRING"
    },
    {
      name = "username"
      type = "STRING"
    }
  ]
}
