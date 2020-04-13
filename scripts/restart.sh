#!/bin/bash

echo '正在重启服务器'

REMOTE_DIR="/opt/swiper"

PID=`cat $REMOTE_DIR/logs/gunicorn.pid`
kill -HUP $PID

echo '服务器重启完毕'



