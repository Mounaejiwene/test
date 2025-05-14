pipeline {
    agent any

    environment {
        ANSIBLE_INVENTORY = 'inventory.ini'
        ANSIBLE_PLAYBOOK = 'playbook.yml'
    }

    stages {
        stage('Hello') {
            steps {
                echo '🎉 Jenkins fonctionne !'
            }
        }

        stage('Déploiement Ansible') {
            steps {
                sh 'ansible-playbook -i $ANSIBLE_INVENTORY $ANSIBLE_PLAYBOOK'
            }
        }
    }
}
