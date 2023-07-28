## Требования
Вам понадобится [Docker](https://docs.docker.com/) (с плагином Compose), установленный и запущенный на Вашем устройстве.

Мы рекомендуем использовать Docker Desktop на [macOS](https://docs.docker.com/desktop/install/mac-install/) / [Windows](https://docs.docker.com/desktop/install/windows-install/), а также использовать [Docker Server](https://docs.docker.com/engine/install/#server) дистрибутив для выбранного Вами Linux дистрибутива. Инструкции по установке можно найти по ссылкам сверху.

## Установка

```sh
git clone -c core.longpaths=true -c core.autocrlf=true https://github.com/ostis-apps/nika # для избежания проблем файловой системы Windows
cd nika
git submodule update --init --recursive
docker compose pull
```

## Сборка
  ```sh
  docker compose build
  ```

## 🚀 Запуск
  ```sh
  docker compose up --no-build
  ```
  Эта команда запустит 2 Web UIs на Вашем устройстве:
    - sc-web - `localhost:8000`
    - dialogue web UI - `localhost:3033`

Мы настроили нашу систему на пересборку KB при каждом повторном запуске. Если вы разрабатываете какой-то конкретный фрагмент своей базы знаний, вы можете изменить repo.path, чтобы убрать ненужные Вам папки.

Если Вы не хотите пересобирать KB при повторном запуске, то закомментируйте переменную окружения `REBUILD_KB` в `docker-compose.yml`.
Вы можете использовать `docker compose run --rm problem-solver build`, чтобы пересобрать KB вручную.
