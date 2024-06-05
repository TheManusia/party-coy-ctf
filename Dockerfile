FROM python:slim AS app
RUN python -m pip install --no-cache-dir pycryptodome

FROM pwn.red/jail
COPY --from=app / /srv

COPY /src/start.sh /srv/app/run
COPY /src/chall.py /srv/app/chall.py
COPY /src/flag.py /srv/app/flag.py

ENV JAIL_MEM=20M JAIL_ENV_NUM=5

RUN chmod 755 /srv/app/run