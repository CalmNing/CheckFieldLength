pipeline {
  agent any
  stages {
    stage('git') {
      steps {
        git(credentialsId: '  ', url: 'git@github.com:zhaosq8/CheckFieldLength.git')
      }
    }

    stage('sonar') {
      steps {
        withSonarQubeEnv(installationName: 'SonarQube', envOnly: true)
      }
    }

  }
}