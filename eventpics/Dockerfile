FROM docker.io/python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Make the entrypoint.sh script executable
RUN chmod +x entrypoint.sh

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
