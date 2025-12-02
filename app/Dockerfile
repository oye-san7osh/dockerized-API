# Use an Official Python Runtime as a Parent Image
FROM python:3.11-slim


# Prevent Python From writing .pyc file
ENV PYTHONDONTWRITEBYTECODE=1


# Prevent Python From Buffering stdout & stderr
ENV PYTHONUNBUFFERED=1


# Set Working Directory Inside the Container
WORKDIR /app


# Install Python Dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


# Copy Project File into Container Folder
COPY . /app/


# Expose Port (for Django)
EXPOSE 8000


# Run Entrypoint Script
ENTRYPOINT ["/app/entrypoint.sh"]


# Run the Application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
