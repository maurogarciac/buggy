# buggy

![buggy](/images/buggy.jpg)


# Introduction 

An http API that recieves, validates and saves test actions, and returns formatted test-case data.

## Requirements:

* Python 3.11.2

## Optional *recommended* requirements:

* Make 4.4.1
* Docker 26.1.1

## Local setup steps:

1. Create a Virtual Environment and name it `.venv`:
    ```shell
    python -m venv .venv
    ```
2. Activate the Environment:
    - Linux
    ```shell
    chmod +x .venv/bin/activate
    source .venv/bin/activate
    ```
    - MacOs
    ```shell
    source .venv/Scripts/activate
    ```
3. Install the required Packages:
    ```shell
    python -m pip install -r requirements/requirements.txt
    ``` 

## Docker setup steps:
Run `docker-compose up`
    
#### Alternative execution methods:

- Locally with uvicorn:
    ```shell
    uvicorn main:app --reload
    ```
- Locally with Make:
    ```shell
    make start
    ```

## Structure: tbd
