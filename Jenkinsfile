pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t kubedemoapp:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                bat 'docker login -u charmitha05 -p Charm@2005'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Push Docker Image to Docker Hub"
                bat "docker tag kubedemoapp:v1 charmitha05/sample1:kubeimage1"
                bat "docker push charmitha05/sample1:kubeimage1"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo 'Successful'
        }
        failure {
            echo 'Unsuccessful'
        }
    }
}
