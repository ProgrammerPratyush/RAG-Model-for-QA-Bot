# Use the official Python image as a base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Check if sources.list exists and update mirrors only if the file is present
RUN echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/99force-ipv4 && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    apt-get update && apt-get install -y ca-certificates && update-ca-certificates


# Install dependencies listed in the requirements.txt file
RUN pip install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org && \
    pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port the app runs on
EXPOSE 8501

# Command to run the app when the container starts
CMD ["streamlit", "run", "query_chat.py", "--server.port=8501", "--server.address=0.0.0.0"]
