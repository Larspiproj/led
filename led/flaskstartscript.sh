#!/bin/bash

export FLASK_APP=ledcontrol.py
export FLASK_DEBUG=True

flask run --host=0.0.0.0
