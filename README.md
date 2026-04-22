# KeaBuilder ML Assessment Submission

## Overview

This repository contains solutions to a set of practical machine learning and system design tasks based on a real world SaaS platform scenario similar to KeaBuilder. The goal of this assignment is to demonstrate practical ML understanding, system thinking, and the ability to design scalable and production ready solutions.

The solutions focus on lightweight implementations, clear architecture, and real world applicability rather than heavy model training.

## Structure of Submission

### question 1 similarity matching
Implementation of a simple text similarity system using TF IDF and cosine similarity. Includes a FastAPI service and sample inputs and outputs.

### question 2 ml serving
Design and implementation of a production style ML serving architecture integrating a Python ML service with a Node.js backend using REST APIs.

### question 3 schema design
Database schema design for storing user inputs and model predictions with proper relationships and production relevant fields.

### question 4 ui latency handling
If ML responses are slow, one simple way to handle this in the UI is by showing a loading state such as a spinner or a “generating response” message.
This ensures users get immediate feedback and don’t feel the system is unresponsive.
Additionally, for LLM-based systems, we can improve user experience further by streaming partial responses instead of waiting for the full output.

### question 5 production challenges
When moving ML models from a notebook to production, there are several challenges.
First is data drift, where real-world data differs from training data, affecting performance.
Second is scalability and latency, since production systems must handle real-time requests efficiently.
Third is deployment and integration, where models need to be properly packaged, versioned, and integrated with backend systems.

### question 6 lora face consistency
If I wanted face consistency with LoRA, I would fine-tune a pre-trained diffusion model on the images of some person.
First I would gather a small dataset of images of different angles and lighting conditions.
Then I would preprocess the data by aligning and cleaning the images .
Then I would train a LoRA module on top of a base model like Stable Diffusion to learn identity specific features.
I would use a special trigger token in the prompts during inference to generate consistent faces.
This approach is light and efficient, but is highly dependent on data quality and can easily overfit if not carefully controlled.
Can be further improved with ControlNet and other techniques for better pose control

### question 7 tools and frameworks
Tools, frameworks and platforms I have used in real life projects:

I am a Senior AI Engineer with more than 8 years of professional experience working on building and deploying end-to-end AI systems in multiple domains including NLP, Computer Vision, OCR and Large Language Models (LLMs). This is a structured list of the tools, frameworks and platforms I've worked on real projects with:

Programming & Core Technologies:
Python is my main programming language when building ML and AI systems. I also use SQL for querying and managing structured data. I have used FastAPI extensively to build production ready APIs and services that help to create scalable and efficient backend services.

IV. Machine Learning & AI Frameworks:
I have hands-on experience with Scikit-learn in classical machine learning tasks like classification and anomaly detection. I have worked on deep learning applications with Pytorch and Tensorflow. I have experience working across the Natural Language Processing (NLP), Computer Vision and OCR pipelines. I have developed models for text extraction, face detection and document processing.

GenAI & LLM Ecosystem:
I have experience with Large Language Models including Gemini, and have built systems using frameworks such as LangChain and LangGraph to develop RAG (Retrieval Augmented Generation) pipelines and agent-based workflows. I have also used Olama and Qwen models for local LLM based applications. I have also implemented prompt engineering techniques and built systems like Natural Language to SQL generators in enterprise scenarios.

MLOps & Deployment :
I have experience deploying ML models into production using Docker for containerization and building REST-based microservices architectures. I have experience with model serving, API deployment and integration of ML systems in backend applications. I have experience with CI/CD practices as well, for maintaining and updating production systems.

Cloud Platforms & Data Services:
I have worked with Google Cloud Platform (GCP) to deploy and manage ML systems. I have worked on model workflows using Vertex AI, data analysis using BigQuery and datasets and model artifacts using Cloud Storage.

Data Processing and Analysis:
I use Pandas and NumPy regularly for data preprocessing, transformation and feature engineering. These tools have been critical for preparing data pipelines for training and inference.

Development Tools & Workflow:
I work with Git and GitHub for version control and collaboration. I have used Jira for tracking tasks and project management. I also leverage Jupyter Notebooks for experimentation and Linux based environments for development and deployment.

Real World Applications:
In my projects, I have built LLM-powered Natural Language to SQL applications, OCR-based document intelligence pipelines, AI-powered video KYC verification systems with computer vision and speech processing, and compliance automation systems with LLMs. I have also deployed scalable ML solutions on cloud infrastructure using API based architecture.

Generally my experience has been more on building practical production-ready AI systems than just experimental models.

## Tech Stack Used

Python
FastAPI
Scikit learn
Node.js
Docker
Google Cloud Platform
Pandas and NumPy

## Approach and Design Philosophy

The overall approach followed in this assignment is based on the following principles

Focus on real world applicability
Keep solutions simple and efficient
Design with scalability in mind
Ensure modular and maintainable architecture
Balance between implementation and system thinking

## How to Run the Code

Each question folder contains its own instructions and can be executed independently.

For Python based services install dependencies using pip install and run using uvicorn.

For Node.js services install dependencies using npm install and run using node.

If docker is used run docker compose up to start all services.

## Key Highlights

Designed lightweight ML components that can be easily integrated into a SaaS platform
Used microservices architecture for ML model serving
Focused on production concerns such as scalability latency and monitoring
Provided clear and structured explanations for each solution

## Conclusion

This assignment demonstrates the ability to think in systems design ML powered features and build practical solutions that can be integrated into real world products like KeaBuilder. The focus has been on clarity efficiency and production readiness.

## Author

Keshav Bhardwaj
Senior AI Engineer
