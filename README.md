Generate maps of candidate routes for build-your-own Te Araroa

# Set up development environment

```
python3 -m venv env
. env/bin/activate
pip3 install -r requirements.in
vim LINZ_API_KEY  # this file is gitignore'd - should be one line with your API key
mkdir html
PYTHONPATH=. python3 main.py
open html/map.html
```
