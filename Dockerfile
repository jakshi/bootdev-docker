FROM debian:stable-slim

COPY bootdev-docker /bin/goserver

ENV PORT=8991

CMD ["/bin/goserver"]
