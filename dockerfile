FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY app/requirements.txt ./
RUN pip install -r requirements.txt

# Copy the Flask application script into the container
COPY app/app.py ./

# Expose the port the app runs on
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]
