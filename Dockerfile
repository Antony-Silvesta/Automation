# Step 1: Use an official Python runtime as a base image
FROM python:3.9-slim
# Step 2: Set the working directory inside the container
WORKDIR /app
# Step 3: Copy the requirements.txt file into the container
COPY requirements.txt /app/
# Step 4: Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Step 5: Copy the rest of the project code into the container
COPY . /app

# Step 6: Specify the command to run your tests 
CMD ["pytest", "--maxfail=5", "--disable-warnings"]
