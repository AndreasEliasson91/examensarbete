# -slim = slimmer Docker image, need to manually install tools
FROM python:3.7.5-slim


# Set up and activate venv
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

WORKDIR /usr/src/app

RUN python -m pip install \
            parse \
            realpython-reader

COPY headlines.py .
CMD ["python", "headlines.py"]
