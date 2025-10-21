# Python Flask Application

A friendly Flask-based web service that provides system information and health monitoring with encouraging messages.

## Overview

This application is a lightweight Python Flask service designed to provide system information, health monitoring, and positive user interaction. It's containerized and ready for deployment on Kubernetes platforms with a touch of personality!

## Features

- **Enhanced System Information**: Provides hostname, date, encouraging messages, and deployment info
- **Health Monitoring**: Reliable health check endpoint for service monitoring
- **Kubernetes Optimized**: Specifically designed for Kubernetes deployment
- **Containerized**: Docker support for easy deployment
- **CI/CD Ready**: GitHub Actions workflow for automated builds
- **User Friendly**: Includes encouraging messages for developers

## API Endpoints

### Information Endpoint

```
GET /api/v1/info
```

Returns enhanced system information with encouraging messaging.

**Response:**
```json
{
  "time": "21-10-2025",
  "hostname": "python-app-pod-12345",
  "message": "You are doing a good job human!! :-)",
  "deployed_on": "kubernetes"
}
```

**Fields Description:**
- `time`: Current date in DD-MM-YYYY format
- `hostname`: Container/pod hostname
- `message`: Encouraging message for developers
- `deployed_on`: Deployment platform identifier

### Health Check Endpoint

```
GET /api/v1/healthz
```

Returns the service health status for monitoring systems.

**Response:**
```json
{
  "status": "up"
}
```

**HTTP Status:** `200 OK`
