FROM python:3-alpine

LABEL org.label-schema.name="kpnnl/cz-kpn"
LABEL org.label-schema.description="KPN'S COMMITIZEN"
LABEL org.opencontainers.image.source="https://github.com/kpn/cz-kpn"
WORKDIR /app

RUN apk add --update -t --no-cache git curl alpine-sdk

RUN ["pip", "install", "-U", "--no-cache-dir", "pip"]
RUN ["pip", "install", "-U", "--no-cache-dir", "git+https://github.com/grahamhar/commitizen.git@regex-tags"]
RUN ["git", "config", "--global", "--add", "safe.directory", "/app"]

##### run
ENTRYPOINT [ "/bin/sh", "-c" ]
CMD [ "cz", "-n", "cz_kpn", "--help" ]