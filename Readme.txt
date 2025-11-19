Project Architecture
=====================

Infrastructure: 1 Master Node, 2 Worker Nodes.

Orchestration: Ansible configures the servers and deploys the application.

Management & Access Control: Portainer provides the UI and handles the specific requirement of restricting container access per user (RBAC).

Application: A Python Flask app served by Gunicorn (Production Ready) running in Docker containers.

Directory Structure
====================

ansible-docker-flask/
├── ansible/
│   ├── inventory.ini
│   └── playbook.yml
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── docker-compose.yml
├── portainer-server-stack.yml  (For Master Node)
└── portainer-agent-stack.yml   (For Worker Nodes)

Execution Steps
================

1. Run Ansible: ansible-playbook -i ansible/inventory.ini ansible/playbook.yml
2. Access Portainer: Open https://<MASTER_IP>:9443 
3. Connect Workers: Inside Portainer, add Worker 1 using IP <WORKER_1_IP>:9001
4. Configure Access (RBAC): Create Users in Portainer (e.g., UserA, UserB) , Go to Environments -> Worker 1 , Assign UserA access to specific containers. Now UserA can only see and manage their assigned containers. And similarly for Worker 2/UserB.


