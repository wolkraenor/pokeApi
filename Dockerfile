# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.7

WORKDIR /var/www

COPY requirements.txt /requirements.txt
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN pip install -r /requirements.txt

ENTRYPOINT ["sh"]
CMD ["/entrypoint.sh"]