FROM python:3.8.6

WORKDIR app/

COPY game.py game.py

CMD ["python","game.py"]
