from dataclasses import dataclass
from environs import Env

@dataclass
class DatabaseConfig:
    name: str         # Название базы данных
    host: str         # URL-адрес базы данных
    user: str         # Username пользователя базы данных
    password: str     # Пароль к базе данных

@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту

@dataclass
class LogSettings:
    level: str
    format: str

@dataclass
class Config:
    bot: TgBot
    log: LogSettings

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        bot=TgBot(token=env('BOT_TOKEN')),
        log=LogSettings(level=env("LOG_LEVEL"), format=env("LOG_FORMAT"))
    )