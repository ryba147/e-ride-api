FROM python:3.9.6-alpine

ENV WORKDIR /opt/code
WORKDIR ${WORKDIR}

COPY requirements.txt ${WORKDIR}/requirements.txt

COPY alembic ${WORKDIR}/alembic
COPY alembic.ini ${WORKDIR}/alembic.ini

COPY app ${WORKDIR}/app

RUN pip install -U pip setuptools wheel && \
    pip install -r requirements.txt

ENV PORT "8000"

EXPOSE $PORT

CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT