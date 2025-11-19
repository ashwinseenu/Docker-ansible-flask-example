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

Brief Execution Steps
======================

1. Run Ansible: ansible-playbook -i ansible/inventory.ini ansible/playbook.yml
2. Access Portainer: Open https://<MASTER_IP>:9443 
3. Connect Workers: Inside Portainer, add Worker 1 using IP <WORKER_1_IP>:9001
4. Configure Access (RBAC): Create Users in Portainer (e.g., UserA, UserB) , Go to Environments -> Worker 1 , Assign UserA access to specific containers. Now UserA can only see and manage their assigned containers. And similarly for Worker 2/UserB.

Ports Used 
===========

Custom TCP | Port 9443 | Source: X.X.X.X/X (For HTTPS UI)

Custom TCP | Port 8000 | Source: X.X.X.X/X (For Agent Tunnel)

Custom TCP | Port 9000 | Source: X.X.X.X/X (For Legacy HTTP UI)

Custom TCP | Port 5000 | Source: X.X.X.X/X (For your Flask App)

Custom TCP | Port 9001 | Source: X.X.X.X/X (For Worker Node to Master Communication)

Configuring Portainer - Role-Based Access Control (RBAC)
=========================================================

1. Go to Environments Section--> Select Add Environment--> Select Docker Standalone--> Select Agent.
2. Enter Name [Ex: worker1] and Env Address [Ex: WorkerIP:9001]. Click Connect and close.
3. For User Creation, Go to Users Section--> Enter Username [Ex: Developer, Password--> Click Create User.
4. For Assiging Access, Go to Environments--> Select Worker1->Manage Access->Select Users from User dropdown list--> Click Create Access.
5. Repeat the Process from Step 1 for Other Worker Nodes and Users.

Check-List:
===========

Portainer Management UI: https://MasterIP:9443 --> Login_Page
ContainerHello: http:WorkerIP:5000


OUTPUT
======

https://github.com/ashwinseenu/Docker-ansible-flask-example/issues/1#issue-3643487834




