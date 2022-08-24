#! /bin/bash

JS_PATH=/home/bzx/Django_App/game/static/js/
JS_PATH_DIST=${JS_PATH}dist/
JS_PAHT_SRC=${JS_PATH}src/

find ${JS_PATH_SRC} -type f -name '*.js' | sort | xargs cat > ${JS_PATH_DIST}game.js
