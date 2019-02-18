pipeline {
    agent any

    stages {
        stage('Prep'){
            steps{
                echo "Prep"
            }
        }
        stage('Build'){
            parallel {
                stage('Deb') {
                    steps {
                        echo "deb done"
                    }
                }
                stage('Raspberry Deb') {
                    steps {
                        echo "heck"
                    }
                }
                stage('Arch') {
                    steps {
                        echo "Fuck this"
                    }
                }
            }
        }
        stage('Deploy'){
            steps {
                echo "Deploy"
            }
        }
        stage('Cleanup') {
            steps {
                echo "Clean"
            }
        }
    }
}
