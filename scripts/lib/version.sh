#!/usr/bin/env bash

function get_kitsu_version() {
    if [[ $KITSU_VERSION == "latest" ]]; then
        export KITSU_VERSION=$(curl https://api.github.com/repos/cgwire/kitsu/commits | jq -r '.[].commit.message | select(. | test("[0-9]+(\\.[0-9]+)+"))?' | grep -m1 "")
        echo "${GREEN}Set KITSU_VERSION to $KITSU_VERSION"
    fi
}

function get_zou_version(){
    if [[ $ZOU_VERSION == "latest" ]]; then
        export ZOU_VERSION=$(curl https://api.github.com/repos/cgwire/zou/commits | jq -r '.[].commit.message | select(. | test("[0-9]+(\\.[0-9]+)+"))?' | grep -m1 "")
        echo "${GREEN}Set ZOU_VERSION to $ZOU_VERSION"
    fi
}