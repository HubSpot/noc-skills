#!/bin/sh

### BEGIN INIT INFO
# Provides:          gunicorn
# Required-Start:    $all
# Required-Stop:     $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts the gunicorn server
# Description:       starts gunicorn using start-stop-daemon
### END INIT INFO

# Gunicorn init.d script for redhat/centos
# Written originally by Wojtek 'suda' Siudzinski <admin@suda.pl>
# Adapted to redhat/centos by Daniel Lemos <xspager@gmail.com>
# Gist: https://gist.github.com/1511911
# Original: https://gist.github.com/748450

#
# Sample config (/etc/gunicorn/gunicorn.conf):
#
# SERVERS=(
#   'server_name    socket_or_url   project_path    number_of_workers'
# )
# RUN_AS='www-data'
#
# WARNING: user $RUN_AS must have +w on /var/run/gunicorn

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
DAEMON=/usr/bin/gunicorn_django
NAME=gunicorn
DESC=gunicorn
SERVER="$2"
VE_PATH=/data/env

test -x $DAEMON || exit 0

# Source function library.
. /etc/rc.d/init.d/functions

# Source networking configuration.
. /etc/sysconfig/network

# Check that networking is up.
[ "$NETWORKING" = "no" ] && exit 0

if [ -f /etc/gunicorn/gunicorn.conf ] ; then
    . /etc/gunicorn/gunicorn.conf
fi

if [ ! -d /var/run/gunicorn ]; then
    mkdir /var/run/gunicorn
fi

start () {
    for i in "${SERVERS[@]}"
    do
        :
        set -- "$i"
        IFS="   "; declare -a data=($*)

        if [ "$SERVER" ]; then
            if [ "$SERVER" != ${data[0]} ]; then
                continue
            fi
        fi
        echo "Spawning ${data[0]}"
                cd ${data[2]}
        daemon --user $RUN_AS --pidfile /var/run/gunicorn/${data[0]}.pid $DAEMON -b ${data[1]} -w ${data[3]} -D -p /var/run/gunicorn/${data[0]}.pid
    done
    return
}

stop () {
    for i in "${SERVERS[@]}"
    do
        :
        set -- "$i"
        IFS="   "; declare -a data=($*)
        if [ "$SERVER" ]; then
            if [ "$SERVER" != ${data[0]} ]; then
                continue
            fi
        fi
        if [ -f /var/run/gunicorn/${data[0]}.pid ]; then
            echo "Killing ${data[0]}"
            kill $(cat /var/run/gunicorn/${data[0]}.pid)
        fi
    done
}

case "$1" in
  start)
        echo "Starting $DESC"
        start
        ;;
  stop)
        echo "Stopping $DESC"
        stop
        ;;
  restart)
        echo "Restarting $DESC"
        stop
        sleep 1
        start
        ;;
  *)
        N=/etc/init.d/$NAME
        echo "Usage: $N {start|stop|restart} [particular_server_to_restart]" >&2
        exit 1
        ;;
esac

exit 0