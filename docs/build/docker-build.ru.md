## Требования
Вам понадобится установленный и запущенный [Docker](https://docs.docker.com/) (с плагином Compose).

Рекомендуем использовать Docker Desktop на [macOS](https://docs.docker.com/desktop/install/mac-install/) / [Windows](https://docs.docker.com/desktop/install/windows-install/), а также использовать [Docker Server](https://docs.docker.com/engine/install/#server) дистрибутив для выбранного Вами Linux дистрибутива. Инструкции по установке можно найти по ссылкам сверху.

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
  Данная команда запустит 2 следующих web-интерфейса:
  
    - sc-web - `localhost:8000`
    - диалоговый web-интерфейс - `localhost:3033`

Мы настроили нашу систему на пересборку БЗ (базы знаний) при каждом повторном запуске. Если Вы разрабатываете какой-то конкретный фрагмент своей базы знаний, то можете изменить repo.path, чтобы убрать ненужные Вам папки.

Если Вы не хотите пересобирать БЗ при повторном запуске, то закомментируйте переменную окружения `REBUILD_KB` в `docker-compose.yml`.
Вы можете использовать `docker compose run --rm problem-solver build`, чтобы пересобрать БЗ вручную.
