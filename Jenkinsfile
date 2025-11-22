pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/madhav8511/MLOPS.git'
            }
        }

         stage('Setup Python venv') {
            steps {
                sh 'python3 -m venv mlops'
                sh '. mlops/bin/activate && pip install --upgrade pip'
                sh '. mlops/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('DVC Pull') {
            steps {
                sh '. mlops/bin/activate && dvc pull'
            }
        }

        stage('Run DVC Pipeline') {
            steps {
                sh '. mlops/bin/activate && dvc repro'
            }
        }

        stage('DVC Push') {
            steps {
                sh '. mlops/bin/activate && dvc push'
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
