#!/usr/bin/env bash

# Make sure SWD is set to the project root
SWD=$(cd "$(dirname "$0")/../.."; pwd)

function check_dependencies(){
    failed=false
    if [ ! -e "$SWD/kitsu/Dockerfile" ]; then
        echo "${ERROR}Kitsu Dockerfile required"
        failed=true
    fi
    if [ ! -e "$SWD/zou/Dockerfile" ]; then
        echo "${ERROR}Zou Dockerfile required"
        failed=true
    fi
    if $DEVELOP && [ ! -e "$SWD/kitsu-dev/.git" ]; then
        echo "${ERROR}Kitsu repo required"
        failed=true
    fi
    if $DEVELOP && [ ! -e "$SWD/zou-dev/.git" ]; then
        echo "${ERROR}Zou repo required"
        failed=true
    fi

    if $failed; then
        exit 1
    fi
}

function build_images() {
    echo "${MAGENTA}BUILD CONTAINERS"

    check_dependencies

    if $DEVELOP; then
        COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
        dc -f "$SWD/docker-compose.yml" -f "$SWD/docker-compose.develop.yml" build --force-rm --pull
    else
        command -v curl 1>/dev/null || { echo "${ERROR}curl required" && exit 1; }
        command -v jq 1>/dev/null || { echo "${ERROR}jq required" && exit 1; }

        # The following functions should be available via functions_versions.sh
        get_kitsu_version
        get_zou_version
        COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
        dc -f "$SWD/docker-compose.yml" -f "$SWD/docker-compose.build.yml" build --force-rm --pull
    fi
}

function compose_up() {
    echo "${YELLOW}START CONTAINERS"
    if $DEVELOP ; then
        dc -f "$SWD/docker-compose.yml" -f "$SWD/docker-compose.develop.yml" up -d
    elif $BUILD ; then
        dc -f "$SWD/docker-compose.yml" \
           -f "$SWD/docker-compose.prod.yml" \
           -f "$SWD/docker-compose.build.yml" up -d
    else
        dc pull --include-deps
        dc -f "$SWD/docker-compose.yml" \
           -f "$SWD/docker-compose.prod.yml" up -d
    fi
    if [[ "${ENABLE_JOB_QUEUE}" != "True" ]]; then
        echo "${YELLOW}DISABLE ZOU ASYNC JOBS"
        dc stop zou-jobs
    fi
    
    until dc exec -T db pg_isready ; do
        sleep 3
        echo "${YELLOW}Waiting for db..."
    done
}

function compose_down() {
    echo "${YELLOW}STOP CONTAINERS"
    dc down
}

function init_zou() {
    local dbowner=postgres
    local dbname=zoudb

    if $DEVELOP && ! $KEEP_DB; then
        echo "${MAGENTA}DROP DEV DB"
        dc exec db su - postgres -c "dropdb ${dbname}"
    fi

    if dc exec db psql -U ${dbowner} ${dbname} -c '' 2>&1; then
        echo "${GREEN}UPGRADE ZOU"
        dc exec zou-app sh /upgrade_zou.sh
    else
        echo "${GREEN}INIT ZOU"
        dc exec db su - postgres -c "createdb -T template0 -E UTF8 --owner ${dbowner} ${dbname}"
        dc exec zou-app zou reset-search-index
        dc exec zou-app sh /init_zou.sh
    fi
}