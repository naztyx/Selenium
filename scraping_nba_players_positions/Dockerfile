# Step 1: Use a base image with Python and Chrome installed
FROM python:3.9-slim

# Step 2: Install dependencies (Chrome, WebDriver, etc.)
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    chromium \
    chromium-driver

# Step 3: Install Python dependencies
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy your test script into the Docker image
COPY test_script.py /app/test_script.py

# Step 5: Define entry point to run the Selenium test
CMD ["python", "test_script.py"]
