# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the source code
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
