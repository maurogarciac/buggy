FROM python:3.11-bookworm

WORKDIR /work
COPY . /work

# Install required packages
RUN pip install -r requirements.txt --no-compile --no-cache-dir

CMD ["uvicorn" "src.main:app"]