# Python Flask Application

A friendly Flask-based web service that provides system information and health monitoring with encouraging messages.

## Overview

This application is a lightweight Python Flask service designed to provide system information, health monitoring, and positive user interaction. It's containerized and ready for deployment on Kubernetes platforms with a touch of personality! 🎉

## Features

- **Enhanced System Information**: Provides hostname, date, encouraging messages, and deployment info
- **Health Monitoring**: Reliable health check endpoint for service monitoring
- **Kubernetes Optimized**: Specifically designed for Kubernetes deployment
- **Containerized**: Docker support for easy deployment
- **CI/CD Ready**: GitHub Actions workflow for automated builds
- **User Friendly**: Includes encouraging messages for developers

## API Endpoints

### 📊 Information Endpoint

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

### 🔍 Health Check Endpoint

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

## Quick Start

### Local Development

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application:**
   ```bash
   python src/app.py
   ```

3. **Test the Endpoints:**
   ```bash
   # Get system info with encouraging message
   curl http://localhost:5000/api/v1/info
   
   # Check service health
   curl http://localhost:5000/api/v1/healthz
   ```

### Docker Deployment

1. **Build Image:**
   ```bash
   docker build -t python-app .
   ```

2. **Run Container:**
   ```bash
   docker run -p 5000:5000 python-app
   ```

3. **Access Endpoints:**
   - Info: http://localhost:5000/api/v1/info
   - Health: http://localhost:5000/api/v1/healthz

### Kubernetes Deployment

#### Using Kubectl (Direct Manifests)

```bash
kubectl apply -f k8s/
```

#### Using Helm Chart

```bash
helm install python-app ./charts/python-app
```

## Configuration

### Application Settings

| Setting | Value | Description |
|---------|-------|-------------|
| Host | `0.0.0.0` | Server bind address |
| Port | `5000` | Server port |
| Platform | `kubernetes` | Target deployment platform |

### Kubernetes Configuration

- **Service Type**: ClusterIP
- **Internal Port**: 5000  
- **Ingress Host**: `python-app.test.com`
- **Health Endpoint**: `/api/v1/healthz`
- **Readiness Check**: Uses health endpoint

## Response Examples

### Successful Info Request

```bash
$ curl http://localhost:5000/api/v1/info
```

```json
{
  "time": "21-10-2025",
  "hostname": "python-app-deployment-abc123-xyz789",
  "message": "You are doing a good job human!! :-)",
  "deployed_on": "kubernetes"
}
```

### Health Check Response

```bash
$ curl http://localhost:5000/api/v1/healthz
```

```json
{
  "status": "up"
}
```

## CI/CD Pipeline

Automated deployment pipeline using GitHub Actions:

### Pipeline Features
- **Trigger**: Push to `main` branch with changes in `src/`
- **Build**: Creates Docker image with 6-character commit SHA tag
- **Deploy**: Pushes to Docker Hub and syncs via ArgoCD

### Workflow Overview
1. Checkout source code
2. Generate short commit ID
3. Login to Docker Hub
4. Build and push container image
5. Sync ArgoCD application

## Monitoring & Health Checks

### Kubernetes Probes

Configure your deployment with health checks:

```yaml
livenessProbe:
  httpGet:
    path: /api/v1/healthz
    port: 5000
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /api/v1/healthz  
    port: 5000
  initialDelaySeconds: 5
  periodSeconds: 5
```

### Monitoring Information

The `/api/v1/info` endpoint provides valuable monitoring data:
- **Hostname**: Identifies specific pod/container instances
- **Timestamp**: Shows service responsiveness
- **Platform**: Confirms deployment environment
- **Status Message**: Indicates service personality/version

## Development

### Project Structure

```
e163442-python-app/
├── src/
│   └── app.py              # Enhanced Flask application
├── k8s/
│   └── ingress.yaml        # Kubernetes ingress
├── charts/
│   └── python-app/         # Helm chart with values
├── .github/
│   └── workflows/
│       └── ci.yaml         # CI/CD pipeline
├── Dockerfile              # Container definition
├── requirements.txt        # Python dependencies
└── docs/
    └── index.md           # This documentation
```

### Testing Commands

```bash
# Local testing
python src/app.py &
curl http://localhost:5000/api/v1/info
curl http://localhost:5000/api/v1/healthz

# Docker testing  
docker build -t test-app .
docker run -p 5000:5000 test-app &
curl http://localhost:5000/api/v1/info

# Kubernetes testing
kubectl port-forward svc/python-app 5000:5000 &
curl http://localhost:5000/api/v1/info
```

## Deployment Targets

- **Local**: Flask development server (`flask run`)
- **Docker**: Containerized deployment
- **Kubernetes**: Production-ready with Helm charts
- **ArgoCD**: GitOps continuous deployment

## Contributing

1. Fork the repository
2. Create a feature branch
3. Update the application code
4. Test all endpoints locally
5. Update documentation if needed
6. Submit a pull request

The encouraging message in the info endpoint reminds us that development is a collaborative effort! 😊

## License

MIT License - Feel free to use and modify!
