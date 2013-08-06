#!/bin/bash
#
# chkconfig: 345 95 95
# description: Start / Stop HubSpot process ContactsApiWeb-2724-a-web
#

## Source function library.
. /etc/rc.d/init.d/functions

export LANG="en_US.UTF-8"
export PATH="/usr/bin:$PATH"

for i in /etc/profile.d/*.sh; do
    . $i >/dev/null 2>&1
done

export PID_FILE="/var/run/NocSkillsAPI.pid"

function start() {
    echo -n "Starting NocSkillsAPI: "

    daemon-runner -d -w "/usr/share/hubspot/NocSkillsAPI/lib"    \
                     -e "/usr/share/hubspot/NocSkillsAPI/logs/NocSkillsAPI.err" \
                     -o "/usr/share/hubspot/NocSkillsAPI/logs/NocSkillsAPI.out" \
                     -p "$PID_FILE"    \
                     -c java -Xmx256m -Xms256m -jar /usr/share/hubspot/NocSkillsAPI/lib/NocSkillsAPI-0.1-SNAPSHOT.jar \
                           server /usr/share/hubspot/NocSkillsAPI/conf/noc_skills_api.yml
                     #-c /usr/share/hubspot/NocSkillsAPI/bin/dropwizard-init

    RETVAL=$?

    if [[ $RETVAL -ne 0 ]]; then
        failure
        echo
        return $RETVAL
    fi

    sleep 2

    if ! kill -0 $(cat "$PID_FILE") &>/dev/null; then
        failure
        echo
        return 1
    fi

    success
    echo
    return 0
}

function stop() {
    echo -n "Stopping NocSkillsAPI: "

    if [ ! -f "${PID_FILE}" ]; then
        failure
        echo
        return 1
    fi

    PID=$(cat $PID_FILE)

    for i in {1..15}; do
        if [[ $i -lt 10 ]]; then
            kill $PID
        elif [[ $i -lt 13 ]]; then
            kill -6 $PID
        else
            kill -9 $PID
        fi
        sleep 1
        if ! kill -0 $PID &>/dev/null; then
            success
            echo
            return 0
        fi
    done

    failure
    echo
    return 0
}

# See how we were called.
case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        start
        ;;
    condrestart|try-restart)
        if [ -f "$PID_FILE" ]; then
            stop
            start
        fi
        ;;
    reload)
        RETVAL="3"
        ;;
    force-reload)
        if [ -f "$PID_FILE" ]; then
            stop
            start
        fi
        ;;
    status)
    status -p "${PID_FILE}" "NocSkillsAPI"
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|condrestart|try-restart|reload|force-reload|status}"
        RETVAL="2"
esac

exit $RETVAL