### Cache

```bash
$ pip3 cache dir

$ pip3 cache info

$ pip3 cache list <pattern>

$ pip3 cache remove <pattern>

$ pip3 cache purge

$ pip3 install package_name --no-cache-dir
```


### Install Tensorflow


```
$ mkdir -p $TMPDIR
```

```
$ export TMPDIR=$HOME/tmp
```

```
$ TMPDIR=tmp pip3 install <package>
```

```
$ pip3 install -b $HOME/build
```

```
$ pip3 install tensorflow --no-cache-dir
```


### Install packages


```bash
$ (env) pip3 install flask flask-sqlalchemy pillow tensorflow --no-cache-dir
```


### Streamlit


```
streamlit run my_app.py --server.enableCORS=false --server.headless=true --global.developmentMode=false

streamlit run my_app.py --server.port=80

python -m http.server [port]

streamlit run my_app.py --server.enableCORS=false

streamlit run my_app.py --server.enableWebsocketCompression=false
```

unable to uplaod file

```
streamlit run my_app.py --server.enableXsrfProtection=false`

export PATH="$HOME/.local/bin:$PATH"
```
