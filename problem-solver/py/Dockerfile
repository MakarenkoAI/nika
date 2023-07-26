FROM python:3.11-slim as base

USER root
WORKDIR /nika/problem-solver

RUN apt-get update && apt-get install -y --no-install-recommends tini

COPY ./problem-solver/py/requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt

COPY ./problem-solver/py/ /nika/problem-solver/py/
COPY ./scripts/run_py_sc_server.sh ./scripts/
COPY ./scripts/set_vars.sh .

ENTRYPOINT [ "/usr/bin/tini", "--", "./scripts/run_py_sc_server.sh" ]