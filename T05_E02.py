import json
from pathlib import Path


def get_nested(data, path, default=None):
    current = data
    for key in path.split("."):
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


config_path = Path(__file__).resolve().parent / "data" / "config.json"
with config_path.open(encoding="utf-8") as file:
    config = json.load(file)

lookups = [
    ("app.name", None),
    ("server.port", None),
    ("server.timeouts.read", None),
    ("database.pool.max", None),
    ("features.beta_dashboard", None),
    ("cache.ttl", 60),
    ("server.host.name", "n/a"),
]

for path, default in lookups:
    print(f"{path} = {get_nested(config, path, default)!r}")

admins = config["admins"]
print(f"admins: {', '.join(admins)} ({len(admins)})")