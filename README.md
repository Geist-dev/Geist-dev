<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg">
  <img src="assets/header-light.svg" alt="Geist-dev — разработчик. Веб-приложения, автоматизация и полезные инструменты." width="960">
</picture>

**Python · Веб-приложения · Автоматизация · GIS · Разработка с LLM**

Разрабатываю личные проекты для практических задач: хранение файлов, организация командных игр, автоматизация повторяющейся работы и публикация геоданных в браузере. Работаю с серверной логикой, веб-интерфейсами, плагинами для настольных приложений, тестами и настройкой запуска.

Использую **Codex и Claude** как инструменты разработки: от разбора идеи и прототипа до отладки, рефакторинга, тестирования и документации. Моя цель — превращать идеи в приложения, которые другой человек сможет запустить и понять.

[Основные проекты](#основные-проекты) · [Технологии](#технологии-и-инструменты) · [Работа с LLM](#работа-с-llm) · [Контакты](#контакты)

## Основные проекты

### [File Storage](https://github.com/Geist-dev/File-Storage)

Личное файловое хранилище с изоляцией аккаунтов, загрузкой файлов, папками, тегами, поиском, предпросмотром изображений и восстановлением из корзины.

**Python · FastAPI · SQLAlchemy · SQLite · JavaScript**

- JWT-авторизация, хеширование паролей через bcrypt и серверная проверка владельца файлов.
- Файлы на диске, метаданные в SQLite, миниатюры изображений через Pillow.
- API-тесты, браузерный сценарий и одна команда для подготовки и запуска приложения.

[Код и инструкция запуска](https://github.com/Geist-dev/File-Storage#readme) · [Скриншоты](https://github.com/Geist-dev/File-Storage#скриншоты) · [CI](https://github.com/Geist-dev/File-Storage/actions)

<details>
<summary>Посмотреть библиотеку файлов</summary>

![Библиотека File Storage](https://raw.githubusercontent.com/Geist-dev/File-Storage/main/docs/screenshots/02-library.png)

</details>

### [Close Bot](https://github.com/Geist-dev/close-discord)

Discord-бот для организации командных матчей и турниров в CS2, Dota 2 и Valorant.

**Python · disnake · asyncio · SQLite · Discord API**

- Slash-команды, кнопки, регистрация игроков, распределение по командам и каналы матчей.
- Сохранение настроек матчей и временных ограничений с восстановлением после сбоев.
- Проверка конфигурации, режим отдельного тестового сервера и автоматические тесты.

[Код и инструкция запуска](https://github.com/Geist-dev/close-discord#readme) · [Скриншоты](https://github.com/Geist-dev/close-discord#скриншоты) · [CI](https://github.com/Geist-dev/close-discord/actions)

### [Alias](https://github.com/Geist-dev/Alias)

Сетевая браузерная игра: участники собираются в команды, объясняют слова и набирают очки за ограниченное время.

**Node.js · Express · WebSocket · JavaScript · HTML / CSS**

- Слово получает только активный объясняющий; права ведущего и игровые действия проверяются сервером.
- Пауза, корректировка счёта, смена хода и восстановление сессии после переподключения.
- Тесты игровых правил, настоящих WebSocket-соединений и браузерный сценарий на четырёх клиентах.

[Код и инструкция запуска](https://github.com/Geist-dev/Alias#readme) · [Скриншоты](https://github.com/Geist-dev/Alias#скриншоты) · [CI](https://github.com/Geist-dev/Alias/actions)

<details>
<summary>Посмотреть ход объясняющего</summary>

![Интерфейс объясняющего в Alias](https://raw.githubusercontent.com/Geist-dev/Alias/main/docs/screenshots/02-explainer.png)

</details>

### GIS-инструменты для QGIS

Также разрабатываю Python-плагины для работы с геоданными и автоматизации повторяющегося ввода.

| Проект | Задача | Технологии |
| --- | --- | --- |
| [AttributeTemplateFiller](https://github.com/Geist-dev/AttributeTemplateFiller) | Шаблоны атрибутов, автозаполнение новых векторных объектов, импорт и экспорт JSON. | Python · PyQGIS · PyQt · QSettings |
| [HTML Web Map Exporter](https://github.com/Geist-dev/html-web-map-exporter) | Экспорт проектов QGIS в интерактивные HTML-карты со слоями, подписями и легендой. | Python · PyQGIS · PyQt · HTML / JavaScript |

## Технологии и инструменты

Здесь собраны инструменты, которые использую в проектах и процессе разработки. Конкретную реализацию и объём возможностей можно посмотреть в соответствующем репозитории.

| Направление | Технологии и задачи |
| --- | --- |
| Языки и интерфейсы | Python, JavaScript, HTML5, CSS3; адаптивная вёрстка, DOM, события, формы, браузерные хранилища, тёмная и светлая темы. |
| Backend и API | FastAPI, Uvicorn, Pydantic, Express, Node.js, HTTP / REST, JSON, валидация запросов, WebSocket, асинхронный Python. |
| Данные и файлы | SQLite, SQLAlchemy, SQL-запросы, хранение файлов на диске, метаданные, фильтры, пагинация, миниатюры изображений через Pillow. |
| Авторизация и проверки приложения | JWT, bcrypt, проверка владельца и ролей, валидация ввода, ограничения загрузки, переменные окружения, `.env`, безопасный вывод текста. |
| Боты и интеграции | Discord API, disnake, slash-команды, интерактивные компоненты, каналы и роли; проекты Telegram-ботов и автоматизация. |
| GIS и настольные инструменты | QGIS, PyQGIS, PyQt, Qt-виджеты, QSettings, шаблоны атрибутов, векторные и растровые слои, преобразование координат, экспорт HTML-карт. |
| Тестирование и отладка | pytest, unittest, встроенный test runner Node.js, проверки API и WebSocket, Playwright / Chromium, инструменты разработчика браузера, регрессионные сценарии. |
| Разработка и публикация | Git, GitHub, ветки, pull request, GitHub Actions, CI, Bash, Python `venv`, pip, npm, lockfile, скрипты запуска, GitHub Pages. |
| LLM-инструменты | Codex, Claude, декомпозиция задач, промпты, работа с контекстом репозитория, последовательная реализация и проверка изменений. |

<details>
<summary>Дополнительный опыт и рабочие среды</summary>

В мой более широкий опыт также входят React, Docker и Java. Работаю с Linux, macOS и Windows; учитываю различия оболочек и окружений в инструкциях запуска.

Среди интересующих меня задач — Telegram-боты, инструменты для сообществ, VPN-инструменты и небольшие утилиты. Основные репозитории выше — самые наглядные примеры, с которых стоит начать знакомство.

</details>

## Работа с LLM

Использую LLM-инструменты в последовательном процессе разработки:

1. Разбираю идею на конкретное поведение, ограничения и небольшие задачи.
2. Работаю с существующим кодом и передаю модели нужный контекст репозитория.
3. Реализую и дорабатываю функции, разбираю ошибки и проверяю предложенные изменения.
4. Проверяю поведение автоматическими тестами и запуском приложения.
5. Подготавливаю инструкции, скриншоты, примеры конфигурации и изменения для GitHub.

Мой текущий фокус — **создание и улучшение приложений с Codex и Claude**. Мне интересны практические применения LLM и повышение надёжности такого процесса через понятные задачи и проверку результата.

## Что можно проверить в проектах

В основных репозиториях есть инструкции запуска, примеры конфигурации, реальные скриншоты и тесты. В README описаны архитектура и текущие ограничения. Стараюсь делать проекты воспроизводимыми: скачать код, выполнить инструкцию и попробовать результат.

<details>
<summary>Все публичные репозитории</summary>

Каталог обновляется автоматически из публичных репозиториев GitHub.

<!-- PROJECTS:START -->
| Репозиторий | Что делает | Технологии |
| --- | --- | --- |
| [File-Storage](https://github.com/Geist-dev/File-Storage) | Личное файловое хранилище: авторизация, загрузка, теги, поиск и восстановление из корзины. | Python · FastAPI · SQLite · JavaScript |
| [close-discord](https://github.com/Geist-dev/close-discord) | Discord-бот для командных матчей и турниров в CS2, Dota 2 и Valorant. | Python · disnake · SQLite |
| [Alias](https://github.com/Geist-dev/Alias) | Браузерная игра: команды, приватные слова, таймер, очки и восстановление соединения. | Node.js · Express · WebSocket |
| [AttributeTemplateFiller](https://github.com/Geist-dev/AttributeTemplateFiller) | Плагин QGIS: шаблоны атрибутов и автоматическое заполнение новых векторных объектов. | Python · PyQGIS · PyQt |
| [html-web-map-exporter](https://github.com/Geist-dev/html-web-map-exporter) | Плагин QGIS для экспорта проектов в интерактивные HTML-карты. | Python · PyQGIS · HTML / JavaScript |
| [geist-dev.github.io](https://github.com/Geist-dev/geist-dev.github.io) | Личный сайт с информацией о разработчике, проектами и контактами. | HTML · CSS · JavaScript |
| [geist-discord.github.io](https://github.com/Geist-dev/geist-discord.github.io) | Портфолио с двумя темами, живым статусом Discord и музыкой Spotify. | HTML · CSS · JavaScript · Express |
<!-- PROJECTS:END -->

</details>

## Контакты

Интересуют предложения по разработке и совместная работа над полезными проектами.

**Telegram:** [@flipgood](https://t.me/flipgood)

**Почта:** [aeromax.live@mail.ru](mailto:aeromax.live@mail.ru)

**GitHub:** [Geist-dev](https://github.com/Geist-dev)
