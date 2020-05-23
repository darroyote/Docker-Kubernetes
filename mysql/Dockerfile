FROM oraclelinux:7-slim

ARG MYSQL_SERVER_PACKAGE=mysql-community-server-minimal-5.7.30
ARG MYSQL_SHELL_PACKAGE=mysql-shell-8.0.20

# Install server
RUN yum install -y https://repo.mysql.com/mysql-community-minimal-release-el7.rpm \
      https://repo.mysql.com/mysql-community-release-el7.rpm \
  && yum-config-manager --enable mysql57-server-minimal \
  && yum install -y \
      $MYSQL_SERVER_PACKAGE \
      $MYSQL_SHELL_PACKAGE \
      libpwquality \
  && yum clean all \
  && mkdir /docker-entrypoint-initdb.d

ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=db
#ENV MYSQL_USER=user
#ENV MYSQL_PASSWORD=primera
ENV DB_HOST=172.17.0.2
ENV MYSQL_USER=root
ENV MYSQL_ALLOW_EMPTY_PASSWORD=True
ENV MYSQL_ROOT_HOST=%

VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /entrypoint.sh
COPY healthcheck.sh /healthcheck.sh
ENTRYPOINT ["/entrypoint.sh"]
HEALTHCHECK CMD /healthcheck.sh
EXPOSE 3306 33060
CMD ["mysqld"]
