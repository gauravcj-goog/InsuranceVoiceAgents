#!/bin/bash
rsync -av . /usr/local/google/home/gauravcj/dev/InsuranceVoiceAgents/ --exclude .git --exclude .venv --exclude node_modules --exclude __pycache__ --exclude .pytest_cache --exclude .DS_Store
echo "Clone complete!"
