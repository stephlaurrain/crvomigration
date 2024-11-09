FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND noninteractive
ENV LSB_RELEASE=bookworm
ADD /sql/createdb.sql /tmp/createdb.sql
# ADD /sql/training2voice.sql /tmp/training2voice.sql
WORKDIR "/root"
RUN apt-get update && apt-get install -y nano wget apt-utils xz-utils gnupg ca-certificates apt-transport-https \ 
    nginx \
    supervisor; \
    systemctl; \
    apt install -y mariadb-server --no-install-recommends; \ 
RUN chown -R www-data:www-data /var/www/html && chmod -R g+s /var/www/html;\
    chmod -R 777 /var/www/html; \
    /etc/init.d/mariadb start; \
    mysql -u root < /tmp/createdb.sql; \
#    mysql --user="adm" --password="kr4K0vKq" --database="training2v"  < /tmp/training2voice.sql; \
    apt autoclean; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*;

EXPOSE 80 3306
ENTRYPOINT ["/usr/bin/supervisord"]