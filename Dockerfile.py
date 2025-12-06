FROM ghcr.io/astral-sh/uv:debian
COPY main.py main.py
COPY books/ books/
CMD ["uv", "run", "main.py"]
