pipeline {
    agent {
        docker {
            image 'python:3.10.12'
            args '-v /jenkins_home/cache:/cache'
        }
    }

    environment {
        GITHUB_REPO = 'https://github.com/yourusername/yourrepo.git'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: "${GITHUB_REPO}", branch: 'main'
            }
        }

        stage('Set Up Python') {
            steps {
                sh 'python -m pip install --upgrade pip'
            }
        }

        stage('Create Taskwarrior Configuration File') {
            steps {
                sh 'echo "data.location=~/.task" > ~/.taskrc'
            }
        }

        stage('Install Taskwarrior') {
            steps {
                sh 'sudo apt-get update && sudo apt-get install -y taskwarrior'
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
