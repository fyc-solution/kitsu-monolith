#!/usr/bin/env bash

SWD=$(cd "$(dirname "$0")"; pwd)

# Source common functions and helper scripts
source "$SWD/common.sh"
source "$SWD/scripts/lib/version.sh"
source "$SWD/scripts/lib/docker.sh"

echo "${BLUE}PARSE ARGS"

BUILD=false
DOWN=false
DEVELOP=false
KEEP_DB=false

# Handle subcommands: local and down
case $1 in
  local)
    BUILD=true
    echo "${CYAN}USE LOCAL BUILD"
    shift
    ;;
  down)
    DOWN=true
    echo "${CYAN}STOP INSTANCE"
    shift
    ;;
esac

# Set default ENV file
export ENV_FILE="$SWD/env"

# Additional flag parsing
for i in "$@"; do
    case $i in
        -e=* | --env=*)
            export ENV_FILE="${i#*=}"
            echo "${CYAN}USE CUSTOM ENV FILE"
            shift
            ;;
        --develop)
            if ! $BUILD && ! $DOWN ; then
                echo "${ERROR}Develop flag works only with 'local' and 'down' commands"
                exit 1
            fi
            DEVELOP=true
            echo "${MAGENTA}DEV MODE"
            shift
            ;;
        --keep-db)
            KEEP_DB=true
            echo "${MAGENTA}KEEP DEV DB DATA"
            shift
            ;;
        -h | --help)
            echo "
Usage:

    build.sh [subcommand] [options]

Subcommand:
    local                   Use local build of Kitsu and Zou containers
    down                    Compose Down the stack

Options:
    -e, --env=ENV_FILE      Set custom env file. If not set, ./env is used

        --develop           [local, down] Gives access to running code on the host. Clean DB every time it's rebuilt.
        --keep-db           [local] Combined with '--develop'. Keep DB data.

    -h, --help              Show this help
            "
            exit 0
        ;;
        *)
            echo "${ERROR}Invalid flag ${i} // Use -h or --help to print help"
            exit 1
        ;;
    esac
done

if $KEEP_DB && ! $DEVELOP; then
    echo "${ERROR}Keep-DB flag works with 'develop' flag only"
    exit 1
fi

# Source environment variables (from common.sh or another file)
source_env "${ENV_FILE}"

if $DEVELOP; then
    export COMPOSE_PROJECT_NAME="${COMPOSE_PROJECT_NAME}-dev"
fi

compose_down

if ! $DOWN; then
    if $BUILD; then
        build_images
    fi

    compose_up
    init_zou
fi