FROM python:3.12-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir uv
RUN uv sync
CMD ["uv", "run", "main.py"]