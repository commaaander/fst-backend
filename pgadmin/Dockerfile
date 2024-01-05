FROM dpage/pgadmin4

ARG POSTGRES_DB
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD

USER root
RUN echo "${POSTGRES_DB}:*:*:${POSTGRES_USER}:${POSTGRES_PASSWORD}" > /pgpass

COPY ./servers.json /pgadmin4/
RUN sed -i "s/POSTGRES_USER/${POSTGRES_USER}/" /pgadmin4/servers.json