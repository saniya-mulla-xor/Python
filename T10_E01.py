from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    def reset():
        instances.pop(cls, None)

    get_instance.reset = reset
    return get_instance


@singleton
class AppConfig:
    def __init__(self, env="dev"):
        self.env = env
        self.values = {}

    def set(self, key, value):
        self.values[key] = value

    def get(self, key, default=None):
        return self.values.get(key, default)


a = AppConfig(env="prod")
b = AppConfig(env="test")
print(a is b)
print(b.env)
a.set("debug", False)
print(b.get("debug"))
print(b.get("missing", "n/a"))
AppConfig.reset()
c = AppConfig(env="test")
print(c is a, c.env, c.get("debug", "gone"))
print(type(c).__name__)