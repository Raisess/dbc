#! /usr/bin/env bash


sudo cp ./bin/dbc /usr/local/bin/dbc
sudo rm -r /usr/local/lib/dbc
sudo cp -r ./src /usr/local/lib/dbc
