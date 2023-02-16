FROM python:3.10-slim-bullseye

WORKDIR /usr/src/app

COPY pyproject.toml /usr/src/app
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . /usr/src/app
RUN apt-get update && \
  apt-get install -y libsm6 libxrender1 libxrender-dev libxxf86vm-dev xorg libxkbcommon-x11-0 libx11-dev libxxf86vm-dev libxcursor-dev \ 
  libxi-dev libxrandr-dev libxinerama-dev libegl-dev libgomp1
CMD ["python", "-u", "main.py"]