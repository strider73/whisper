FROM python:3.10-slim

WORKDIR /python-docker

COPY requirements.txt requirements.txt

# Install Git
RUN apt-get update && apt-get install -y git

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Install OpenAI Whisper directly from GitHub
RUN pip install "git+https://github.com/openai/whisper.git"

# Install FFmpeg (required for audio processing)
RUN apt-get update && apt-get install -y ffmpeg

# Copy all project files into the container
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Start the FastAPI application using Uvicorn
CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]
