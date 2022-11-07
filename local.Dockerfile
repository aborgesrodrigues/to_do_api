# Use West Creek's Gradient Python base image
FROM python:3.8

# Set up a safe working directory to put the code in
WORKDIR /root/work

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# Do not copy anything other than reqs because this is a dev container and so we are using Docker volumes instead.
COPY requirements.txt .
# NOTE: this is a dev container so we should use a docker volume mount instead of copying in files

# Install python deps, both dev and regular
RUN pip install -r requirements.txt
# Install curl into container, because it's a useful dev tool for troubleshooting
RUN apt-get update --allow-releaseinfo-change
RUN apt-get install --yes curl

EXPOSE 8000

CMD ["gunicorn", "--reload", "--worker-tmp-dir", "/dev/shm", "--workers=2", "--threads=4", "--worker-class=gthread", "--log-file=-", "-b", ":8000", "to_do.wsgi"]
