pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Docker Image...'
                bat '''
                    docker build -t imagecharm .
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application in Docker container...'
                bat '''
                    docker stop myycontainer || true
                    docker rm myycontainer || true
                    docker run -d -p 5000:5000 --name myycontainer imagecharm
                '''
            }
        }

        stage('Health Check') {
            steps {
                echo 'Checking if Flask app is running...'
                bat '''
                    curl http://localhost:5000 || exit 1
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ Pipeline failed. Please check the logs.'
        }
        success {
            echo '✅ Pipeline executed successfully and app is running.'
        }
    }
}
