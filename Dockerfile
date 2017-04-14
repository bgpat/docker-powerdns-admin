FROM python:2-alpine

RUN apk add --update --no-cache git gcc musl-dev libffi-dev openldap-dev mysql-dev && \
	git clone https://github.com/ngoduykhanh/PowerDNS-Admin --depth=1 && \
	pip install mysql-python && pip install -r /PowerDNS-Admin/requirements.txt && \
	rm -rf /usr/lib/mysqld* && rm -rf /usr/bin/mysql*
ADD docker-entrypoint.sh /PowerDNS-Admin/docker-entrypoint.sh
ADD config.py /PowerDNS-Admin/config.py

ENV PDNS_VERSION=4.0.3

WORKDIR /PowerDNS-Admin
CMD ["./docker-entrypoint.sh"]
