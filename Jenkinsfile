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
          SECRET_FILE_ID = credentials('KEY_SAM')
        }
        steps {
          script{
            echo "####DISPLAYING KEY_SAM####"
            def my_data = readFile "${mydata}"
            echo "Global property file KEY_SAM: ${mydata}"
            }
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