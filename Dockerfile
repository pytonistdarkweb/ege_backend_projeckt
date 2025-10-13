FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml ./

RUN apk add --no-cache build-base libffi-dev \
    && pip install uv \
    && uv pip install --system -e .

COPY . .

EXPOSE 8080

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]