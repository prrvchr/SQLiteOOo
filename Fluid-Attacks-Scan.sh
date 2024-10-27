#!/bin/bash
docker run -v ~/github/SQLiteOOo:/src -v ./_fascan.yml:/fascan.yml fluidattacks/cli:latest skims scan /fascan.yml
#docker system prune -f
