
# CI/CD and Jenkins Overview

---

## ✅ What is CI and CD?

### 🔧 Continuous Integration (CI)

- **Definition**: CI is the practice of frequently integrating code changes into a shared repository, usually several times a day.
- **Goal**: Detect bugs early and reduce integration issues.
- **How**: Automated builds and tests run on every commit.

> 💡 Example: When a developer pushes code to GitHub, CI automatically runs unit tests and builds the project.

---

### 🚀 Continuous Delivery / Deployment (CD)

#### 📦 Continuous Delivery:
- Automatically prepares code for **release to production**, but **manual approval** is required to deploy.

#### 🤖 Continuous Deployment:
- **Fully automated** process from code push to **deployment in production**, without manual intervention.

---

## 🔧 What is Jenkins?

- **Jenkins** is an **open-source automation server** used to implement CI/CD pipelines.
- Originally developed in Java.
- Supports plugins to integrate with tools like Git, Docker, Maven, Kubernetes, etc.

---

## ⭐ Features of Jenkins

| Feature             | Description                                               |
|---------------------|-----------------------------------------------------------|
| 🧩 Plugin System     | 1800+ plugins to integrate with almost any tool           |
| ⏱️ Pipeline as Code | Define CI/CD pipelines using `Jenkinsfile` (Groovy-based DSL) |
| 👥 Distributed Builds| Supports master-agent architecture to run builds remotely |
| 🔄 SCM Integration   | Works with Git, GitHub, Bitbucket, SVN, etc.             |
| 💻 Platform Independent | Runs on Windows, macOS, Linux                        |
| 🔔 Notifications     | Can send build notifications via email, Slack, etc.      |
| 🔒 Security          | Role-based access, matrix-based authorization, LDAP support |
| 📊 Visualization     | Graphs, build trends, test reports, etc.                 |

---

## 🏗️ Jenkins Architecture

### 🎯 1. Master-Slave (now called Controller-Agent) Model

```
+------------------------+
|     Jenkins Master     |
|------------------------|
| - Web UI               |
| - Job Scheduling       |
| - Load Distribution    |
| - Result Aggregation   |
+------------------------+
          |
          | SSH/Java Web Start
          v
+------------------------+
|    Jenkins Agent(s)    |
|------------------------|
| - Executes build jobs  |
| - Reports back status  |
+------------------------+
```

### Key Components:

| Component        | Description                                                  |
|------------------|--------------------------------------------------------------|
| **Master/Controller** | Manages UI, scheduling, plugin management, stores build info |
| **Agent/Slave**       | Executes jobs assigned by master, useful for scaling         |
| **Jenkinsfile**       | Script that defines pipeline stages (build, test, deploy)    |
| **Executor**          | A slot on agent where a job runs                             |

---

## 🔁 Jenkins CI/CD Pipeline Example

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'mvn clean package'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'mvn test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh './deploy.sh'
            }
        }
    }
}
```

---

## ✅ Summary

| Concept     | Description                                      |
|-------------|--------------------------------------------------|
| **CI/CD**   | Automate code integration, testing, and deployment |
| **Jenkins** | Open-source tool to manage CI/CD pipelines         |
| **Features**| Plugin-rich, extensible, scalable, secure          |
| **Architecture** | Controller-Agent model, pipelines defined in code |

---
