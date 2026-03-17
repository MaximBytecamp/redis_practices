### Windows — пошагово

#### Шаг 1. Установи Docker Desktop

1. Скачай: https://www.docker.com/products/docker-desktop/
2. Запусти установщик, согласись со всем
3. Перезагрузи компьютер (обязательно!)
4. Открой Docker Desktop — дождись пока иконка в трее станет зелёной
5. Проверь в PowerShell:


```powershell
docker --version
# → Docker version 27.x.x (если видишь версию — всё ок)

docker compose version
# → Docker Compose version v2.x.x
```

> Если пишет "не найдена команда" — перезагрузи ещё раз и убедись что Docker Desktop запущен.

#### Шаг 2. Скачай проект

Вариант А — через Git:
```powershell
git clone <url_репозитория>
cd redis_start_practice
```

Вариант Б — скопируй папку на рабочий стол и открой в терминале:
```powershell
cd C:\Users\ТвоёИмя\Desktop\redis_start_practice
```

#### Шаг 3. Запусти одной командой

```powershell
docker compose up --build
```

Что произойдёт:
- Docker скачает образ Redis (~15 МБ) и Python (~50 МБ)
- Соберёт контейнер с твоим приложением
- Запустит Redis и FastAPI
- В консоли появится: `Uvicorn running on http://0.0.0.0:8000`

#### Шаг 4. Открой в браузере

```
http://127.0.0.1:8000/docs
```

Готово!


#### Остановить:
```powershell
# Ctrl+C в терминале где запущен docker compose
# Или в новом терминале:
docker compose down
```

---

### macOS — пошагово

#### Вариант А: Через Docker (универсальный)

```bash
# 1. Установи Docker Desktop
# Скачай: https://www.docker.com/products/docker-desktop/
# Открой .dmg, перетащи в Applications, запусти

# 2. Проверь
docker --version
docker compose version

# 3. Перейди в папку проекта
cd ~/Desktop/redis_start_practice  # или где лежит проект

# 4. Запусти
docker compose up --build

# 5. Открой http://127.0.0.1:8000/docs
```

#### Вариант Б: Без Docker (нативно)

```bash
# 1. Установи Homebrew (если ещё нет)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Установи Redis
brew install redis
brew services start redis

# Проверь:
redis-cli ping
# → PONG

# 3. Установи Python-зависимости
cd ~/Desktop/redis_start_practice
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 4. Запусти
python main.py

# 5. Открой http://127.0.0.1:8000/docs
```

---

### Linux (Ubuntu/Debian) — пошагово

#### Вариант А: Через Docker

```bash
# 1. Установи Docker
sudo apt update
sudo apt install docker.io docker-compose-plugin -y
sudo systemctl start docker
sudo usermod -aG docker $USER
# Перелогинься (или: newgrp docker)

# 2. Запусти
cd ~/redis_start_practice
docker compose up --build

# 3. Открой http://127.0.0.1:8000/docs
```

#### Вариант Б: Без Docker

```bash
# 1. Redis
sudo apt update && sudo apt install redis-server -y
sudo systemctl start redis
redis-cli ping  # → PONG

# 2. Python
sudo apt install python3 python3-venv -y
cd ~/redis_start_practice
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Запусти
python main.py
```

---