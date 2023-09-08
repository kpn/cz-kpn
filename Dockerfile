FROM python:3-alpine

LABEL org.label-schema.name="kpnnl/cz-kpn"
LABEL org.label-schema.description="KPN'S COMMITIZEN"

WORKDIR /app

RUN apk add --update -t --no-cache git curl alpine-sdk

RUN ["pip", "install", "-U", "--no-cache-dir", "pip"]
RUN ["pip", "install", "-U", "--no-cache-dir", "cz-kpn==3.2.2"]

##### run
ENTRYPOINT [ "/bin/sh", "-c" ]
CMD [ "cz -n cz_kpn --help" ]
