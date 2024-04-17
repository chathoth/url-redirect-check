pipeline {
    agent any

    environment {
        DOMAIN_NAME = ''
    }

    stages {
        stage('Execute Python Script') {
            steps {
                script {
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install requests
                        python script.py $DOMAIN_NAME
                    '''
                }
            }
        }
    }

    post {
        always {
            script {
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Redirect Report'
                ])
            }
        }
    }
}
