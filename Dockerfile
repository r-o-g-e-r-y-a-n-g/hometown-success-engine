# Use the official lightweight Python image.
FROM python:3.11-slim

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Run the web service on container startup using gunicorn.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app