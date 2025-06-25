pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/JitenPalaparthi/python-selenium-demo1'
            }
        }

        stage('Install Dependencies') {
            steps {
                // // sh 'apt install python3.11-venv'
                // sh 'python3 -m venv venv'
                // sh '. venv/bin/activate && pip install -r requirements.txt'
                sh 'pip install -r requirements.txt --break-system-packages'

            }
        }

        stage('Run Selenium Tests') {
            steps {
                // sh '. venv/bin/activate && python -m unittest tests/test_text_box.py -v'
                sh 'python -m unittest tests/test_text_box.py -v'
            }
        }
    }
}