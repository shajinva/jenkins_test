pipeline {
  agent any

  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('hello') {
      steps {
        bat 'python hello.py'
      }
    }
    stage('secret') {
        environment {
          SECRET_FILE_ID = credentials('secret-file-id')
          username = credentials('username')
        }
        steps {
            echo "####DISPLAYING SECRET_FILE_ID####"
            echo "Global property file: ${SECRET_FILE_ID}"
            echo "Global property file: ${username}"
      }
    }
    stage('Example Deploy') {
        when {
            branch 'production'
            environment name: 'DEPLOY_TO', value: 'production'
        }
        steps {
            echo 'Deploying'
        }
    }
  }
}