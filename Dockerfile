FROM python:2-alpine

RUN apk add --update --no-cache git gcc musl-dev libffi-dev openldap-dev mysql-dev && \
	git clone https://github.com/ngoduykhanh/PowerDNS-Admin --depth=1 && \
	pip install mysql-python && pip install -r /PowerDNS-Admin/requirements.txt && \
	rm -rf /usr/lib/mysqld* && rm -rf /usr/bin/mysql*
COPY docker-entrypoint.sh /PowerDNS-Admin/docker-entrypoint.sh
COPY config.py /PowerDNS-Admin/config.py

WORKDIR /PowerDNS-Admin
CMD ["./docker-entrypoint.sh"]
