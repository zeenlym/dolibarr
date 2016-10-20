FROM php:5.6-apache

RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libldap2-dev \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-install gd \
    && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
    && docker-php-ext-install ldap \
    && docker-php-ext-install mysqli \
    && apt-get purge -y libpng12-dev libjpeg-dev libldap2-dev

COPY htdocs/ /var/www/html/

RUN chown -hR www-data:www-data /var/www/html

VOLUME /var/www/html/conf
VOLUME /var/www/html/documents

ENV TIMEZONE=Europe/Paris
RUN echo $TIMEZONE > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata
RUN echo "date.timezone = $TIMEZONE" >> ${PHP_INI_DIR}/conf.d/date.ini

EXPOSE 80

