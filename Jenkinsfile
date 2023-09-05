pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/LeviAckermanga/Mongo.git'
            }
        }stage('Build') {
            steps {
                sh 'python3 db.py'
            }
        }
        
    }
    

}
