import groovy.json.JsonSlurper
import groovy.json.JsonSlurperClassic
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
            def my_data = readFile "${SECRET_FILE_ID}"

            def jsonSlurper = new JsonSlurper()

            def config = jsonSlurper.parseText(my_data)


//             def my_data = readFile "${SECRET_FILE_ID}"
//             def res =  json.loads(my_data)
//
//             echo res.get("value1")
//
//             echo "################ ${my_data[value1]}"
//
            echo "Global property file KEY_SAM: ${config}"
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