resource "google_pubsub_topic" "users_api_events" {
  name = "users_api_events"
  labels = local.pubsub_users_api_events
}