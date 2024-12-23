# Use a compatible Python version
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies (assuming requirements.txt exists)
RUN pip install -r requirements.txt

# Expose Flask's default port (5000)
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
