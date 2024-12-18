FROM python:3.11-bookworm

WORKDIR /src
COPY . /src

# Install required packages
RUN pip install -r requirements.txt --no-compile --no-cache-dir

CMD ["uvicorn" "main:app"]