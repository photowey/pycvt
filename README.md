# `pycvt`
A simple command line tool for image size conversion.



## 1.`Install`

```shell
$ pip install -r requirements.txt
```



## 2.`Build`

```shell
$ pyinstaller --onefile pycvt.py
```



## 3.`Usage`

> Add `pycvt` executable to `$PATH`

```shell
# Magnify 2x (+2x)
$ pycvt -i input.png -o output.png -f 2[.0]

# - 2x
$ pycvt -i input.png -o output.png -f -2[.0]
```

