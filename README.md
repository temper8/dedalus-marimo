# dedalus-marimo
Dedalus and marimo

## Clone this repo
```
git clone ...
```

### Установите пакеты, нужные для dedalus:
```
sudo apt install libopenmpi-dev openmpi-bin libfftw3-mpi-dev
```
## Найдите расположение mpi.h
```
find /usr -name "mpi.h" 2>/dev/null
```
## Установите переменные окружения для компилятора
```
export C_INCLUDE_PATH=/usr/lib/x86_64-linux-gnu/openmpi/include:$C_INCLUDE_PATH
```

## иницализация окружения питона

```
uv sync
```

## можно запускать
```
uv run marimo edit
```
### или прямо из windows c помощью `wsl-run.bat`