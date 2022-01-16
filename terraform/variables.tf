variable "application_name" {
  type    = string
  default = "quiznose"
}

variable "region" {
  type    = string
  default = "us-east-1"
}

variable "health_check_path" {
  default = "/"
}

variable "app_port" {
  description = "Port exposed by the docker image to redirect traffic to"
  default     = 5000
}

variable "app_count" {
  description = "Number of docker containers to run"
  default     = 1
}
