variable "project" {
  type = map(string)
  default = {
    name = "yams-lab-nonprod"
    id = "yams-lab-nonprod"
    auto_create_network = false
  }
}

variable "region" {
  default = "us-central1"
}

variable "zone" {
  default = "us-central1-a"
}

variable "datasets" {
  type = list(object({
    name = string
  }))
  default = [
    {
      name = "accounts"
    },
    {
      name = "leads"
    }
  ]
}