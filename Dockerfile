FROM --platform=$BUILDPLATFORM python:3.11-alpine

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0"]