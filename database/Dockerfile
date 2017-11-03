FROM ubuntu:latest

# Install dependencies.
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# Copy the code into the container.
COPY ./ /app
WORKDIR /app

# Install python dependencies.
RUN pip install python-etcd

# Set the entrypoint to execute the code.
ENTRYPOINT ["python"]
CMD ["loaddata.py"]