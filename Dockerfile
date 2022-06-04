FROM python:latest

ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /api
COPY . .
RUN pip install --upgrade pip

# Install dependencies:
RUN pip install --no-cache-dir -r /api/requirements.txt

EXPOSE 80
