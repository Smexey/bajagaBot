# vim: set ft=dockerfile:
FROM python:3.10-slim

# USER root
RUN apt-get update && apt-get upgrade -y && \
    apt-get install --no-install-recommends -y\
    ffmpeg

RUN addgroup --system app && adduser --system --group app

WORKDIR /app
COPY --chown=app:app requirements.txt requirements.txt

USER app

RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

COPY --chown=app:app . .

CMD [ "python", "./src/client.py" ]
