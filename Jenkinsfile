pipeline {
    agent any

    environment {
        GITHUB_REPO = 'https://github.com/ak-arsalan/cli-taskwarrior-and-restapi-automation.git'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: "${GITHUB_REPO}", branch: 'code-refactoring'
            }
        }

        stage('Set Up Python') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
            }
        }

        stage('Create Taskwarrior Configuration File') {
            steps {
                sh 'echo "data.location=~/.task" > ~/.taskrc'
            }
        }

        stage('Install Taskwarrior') {
            steps {
                sh 'apt-get update && apt-get install -y taskwarrior'
            }
        }

        stage('Install Dependencies and Run Tests') {
            steps {
                sh '''
                if [ -f requirements.txt ]; then
                    pip install -r requirements.txt
                fi
                pytest
                '''
            }
        }
    }

    post {
        always {
            junit 'reports/**/*.xml'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Some tests failed.'
        }
    }
}
