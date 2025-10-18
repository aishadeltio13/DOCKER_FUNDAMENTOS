# Docker Python Project

## Overview
In this project, we played around with Docker to containerize Python applications. The idea was to make sure our apps can run anywhere, without worrying about Python versions or missing packages.

---

## What We Did

### 1. Dockerfile
- We created Dockerfiles to define how our images should look.
- Used a lightweight Python image, set a working folder (`WORKDIR /app`), copied our files (`COPY`), installed dependencies from `requirements.txt` (`RUN pip install -r requirements.txt`), and set the command to run the app (`CMD`).
- Basically, it makes the container run our Python script the same way on any computer.

### 2. requirements.txt
- This file lists all the Python packages we need (`requests`, `numpy`, `scipy`, etc.).
- It makes sure the container installs everything we need, so no “it works on my machine” problems.

### 3. Running containers
- Built images with `docker build` and ran them with `docker run`.
- Each container is isolated, so we could test different parts of the project without interfering with each other.

### 4. Docker Compose
- We also tried Docker Compose to manage multiple containers at once.
- Defined services in a `docker-compose.yml` file, set dependencies, and exposed ports.
- Makes it super easy to start everything at once and see how containers can talk to each other.

### 5. Ports & debugging
- Used `EXPOSE` to open ports for communication when needed.
- Tried `docker run -it` and `docker exec` to enter containers and check what’s going on.

---

## Summary
So in short, we learned how to:
- Build Docker images with Dockerfiles
- Manage Python dependencies in a container
- Run and check containers
- Use Docker Compose for multiple containers

This README doubles as both a **GitHub project description** and my **personal notes** for remembering how Docker works.


