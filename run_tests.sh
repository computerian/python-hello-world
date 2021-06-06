#!/usr/bin/env bash
docker build .
if [ $? -eq 0 ]
then
  echo "All tests passed! Congratulations the project is done!"
  exit 0
else
  echo "Tests did not pass. See the log output on what to fix." >&2
  exit 1
fi