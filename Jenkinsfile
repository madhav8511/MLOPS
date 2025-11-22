pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/madhav8511/mlops-example.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Pull Data (DVC)') {
            steps {
                sh 'dvc pull'
            }
        }

        stage('Run Pipeline (DVC)') {
            steps {
                sh 'dvc repro'
            }
        }

        stage('Push Artifacts') {
            steps {
                sh 'dvc push'
            }
        }

        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'models/model.pkl', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "Pipeline Completed Successfully!"
        }
    }
}
