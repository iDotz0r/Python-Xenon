from os import environ as env
import logging

log = logging.getLogger(__name__)


class Config:
    token = "NzUxMDYzOTkwOTg1MjkzOTE1.X1Do2Q.qLh9grQVD13K8T6BjqSBRH5xCjI"
    shard_count = 1
    per_cluster = 1

    prefix = "x!"

    dbl_token = None

    support_guild = 750456371610386443
    owner_id = 672878279291699250
    invite_url = None  # Set to None to generate one automatically

    identifier = "xenon"

    db_host = "mongodb+srv://Python:sYtQzjKSEjhvMe0H@cluster0.env5u.mongodb.net/Python?retryWrites=true&w=majority"
    db_user = "sYtQzjKSEjhvMe0H"
    db_password = "Python"

    redis_host = "localhost"

    template_approval = 633228946875482112
    template_list = 633228950998614037
    template_featured = 633228948251082752

    extensions = [
        "errors",
        "help",
        "admin",
        "backups",
        "templates",
        "users",
        "basics",
        "sharding",
        "botlist",
        "api",
        "builder"
    ]


def __getattr__(name):
    default = getattr(Config, name, None)
    value = env.get(name.upper())

    if value is not None:
        if isinstance(default, int):
            return int(value)

        if isinstance(default, float):
            return float(value)

        if isinstance(default, bool):
            valid = ["y", "yes", "true"]
            return value.lower() in valid

        if isinstance(default, list):
            return value.split(",")

        return value

    return default
