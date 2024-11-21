# Use an official Python runtime as a parent image (or any other language/runtime you prefer)
FROM python:3.8-slim

# Install cron
RUN apt-get update && apt-get -y install cron

# Set the working directory
WORKDIR /usr/src/app

# Copy your script and any other required files
COPY your_script.py .
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Add crontab file in the cron directory
COPY crontab /etc/cron.d/your-cron-job

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/your-cron-job

# Apply cron job
RUN crontab /etc/cron.d/your-cron-job

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log