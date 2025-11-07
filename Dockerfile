FROM python:3-alpine

LABEL org.label-schema.name="kpnnl/cz-kpn"
LABEL org.label-schema.description="KPN'S COMMITIZEN"
LABEL org.opencontainers.image.source="https://github.com/kpn/cz-kpn"
WORKDIR /app

RUN set -eux; \
    apk add --no-cache \
        git \
        git-lfs \
        gpg \
        alpine-sdk \
        bash \
        libffi-dev \
    ; \
    git lfs install;

RUN pip install -U --no-cache-dir pip && \
    pip install -U --no-cache-dir cz-kpn==4.1.0 && \
    git config --global --add safe.directory /app

##### run
ENTRYPOINT [ "/bin/sh", "-c" ]
CMD [ "cz", "-n", "cz_kpn", "--help" ]