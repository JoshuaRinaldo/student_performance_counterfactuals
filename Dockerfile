# Specify the base image
FROM amazonlinux:latest

# Set the working directory
WORKDIR /app

RUN yum install -y python3 python3-pip

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .
COPY student_performance_regressor.pk1 .
COPY Transformed_Student_Performance.csv .

CMD ["python3", "app.py"]
