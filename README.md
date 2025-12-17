# dedalus-marimo
Dedalus and marimo

clone this repo
```
sudo apt install libopenmpi-dev openmpi-bin libfftw3-mpi-dev
```
# Найдите расположение mpi.h
```
find /usr -name "mpi.h" 2>/dev/null
```
# Установите переменные окружения для компилятора
```
export C_INCLUDE_PATH=/usr/lib/x86_64-linux-gnu/openmpi/include:$C_INCLUDE_PATH
```

```
uv sync
```

```
uv run marimo edit
```