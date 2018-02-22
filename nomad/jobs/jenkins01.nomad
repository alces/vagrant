job "jenkins01" {
  datacenters = ["dc1"]

  group "server" {
    task "master" {
      driver = "java"
      config {
        jar_path = "local/jenkins.war"
      }

      artifact {
        source = "http://mirrors.jenkins.io/war-stable/latest/jenkins.war"
      }

      resources {
        memory = 256
      }
    }
  }
}
