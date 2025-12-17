# dedalus-marimo
Как установить Dedalus and marimo под Ubumtu. Так же работает под WSL

### Clone this repo
```
git clone https://github.com/temper8/dedalus-marimo.git
```

### Установите пакеты, нужные для dedalus:
```
sudo apt install libopenmpi-dev openmpi-bin libfftw3-dev libfftw3-mpi-dev
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