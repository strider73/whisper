 Build a Containerized Transcription API using Whisper Model and FastAPI
 https://youtu.be/NU406wZz1eU?si=JN-kvK7kZ-tJ1zul

 # 📜 Containerized Transcription API using Whisper & FastAPI

## 🚀 Overview
This project provides a **containerized** API for **speech-to-text transcription** using OpenAI's **Whisper model** and **FastAPI**. The API runs inside a **Docker container**, making it easy to deploy and use.

## 🛠️ Features
- 🏗 **FastAPI-based API** for handling audio transcription
- 🎙 **Whisper (Base Model)** for speech-to-text conversion
- 📦 **Containerized with Docker** for easy deployment
- 📄 **Supports multiple audio file uploads** via POST request
- 🎛 **Includes Swagger UI** for easy API testing (`/docs`)

---

## 📂 Project Structure
```
├── Dockerfile               # Docker configuration
├── requirements.txt         # Python dependencies
├── app.py                   # FastAPI application
├── README.md                # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/your-repo/containerized-whisper-api.git
 cd containerized-whisper-api
```

### 2️⃣ Build the Docker Image
```sh
docker build -t whisper-api-img .
```

### 3️⃣ Run the Docker Container
```sh
docker run -p 8000:8000 whisper-api-img
```

### 4️⃣ Access the API
- Open **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- Test the `/whisper` endpoint by uploading an **audio file**.

---

## 🛠️ API Endpoints
| Method | Endpoint  | Description |
|--------|----------|-------------|
| **POST** | `/whisper` | Upload an audio file to transcribe |
| **GET**  | `/docs` | Open API documentation |

### Example `curl` request:
```sh
curl -X 'POST' \
  'http://localhost:8000/whisper' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@sample.mp3'
```

---

## 🏗 Deployment Options
You can deploy this API using:
- **Docker Compose**
- **AWS Fargate** (serverless containers)
- **Azure App Services**
- **Google Cloud Run**

---

## 🤝 Contributing
Feel free to open issues or submit PRs if you find ways to improve this project.

---

## 📜 License
This project is **open-source** under the MIT License.

---

### 📧 Contact
If you have any questions, feel free to reach out via **GitHub Issues** or on **strider.lee@gmail.com**.


