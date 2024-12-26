# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory
WORKDIR /app

COPY ./app /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

# Copy the application
COPY . .

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
