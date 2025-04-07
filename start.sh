#! /bin/bash

env PYTHONASYNCIODEBUG=1 uvicorn main:app --log-level debug