
# Use a compatible Python version
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies (assuming requirements.txt exists)
RUN pip install -r requirements.txt

# Expose the application port (FastAPI default is 8000)
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
