pipeline {
    agent any
  
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t assignment1 .' 
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh "docker login -u ${USERNAME} -p ${PASSWORD}"
                        sh 'docker push assignment1'
                    }
                }
            }
        }
        stage('Notify Admin') {
            steps {
                script {
                    def adminEmail = 'i200943@nu.edu.pk' 
                    emailaction(subject: 'Deployment Successful!', body: 'Your application has been successfully deployed!', to: adminEmail)
                }
            }
        }
    }
}
