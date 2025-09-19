pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build Docker Image'
                bat '''
                    docker build -t formappnew .
                '''
            }
        }

        stage('Run') {
            steps {
                echo 'Run application in Docker container'
                bat '''
                    docker rm -f mycontainer || exit 0
                    docker run -d -p 5000:5000 --name mycontainer formappnew
                '''
            }
        }
    }

    post {
        failure {
            echo 'Pipeline failed. please check the logs.'
        }
        success {
            echo 'Pipeline executed successfully.'
        }
    }
}
