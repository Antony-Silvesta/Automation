# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y curl unzip && \
    curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb && \
    apt-get install -y ./chrome.deb && \
    rm chrome.deb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    curl -sSL "https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip" -o chromedriver.zip && \
    unzip chromedriver.zip -d /usr/local/bin/ && \
    rm chromedriver.zip && \
    chmod +x /usr/local/bin/chromedriver

# Set up the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary Python packages from requirements.txt
RUN pip install -r requirements.txt

# Specify the command to run the Selenium test script
# Adjust "Google.py" to the actual script you want to run
CMD ["python", "Google.py"]
