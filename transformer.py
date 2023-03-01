from datetime import datetime, timedelta

from lark import Token, Tree, v_args
from lark.visitors import Discard, Transformer


class TransformError(Exception):
    ...


@v_args(inline=True)
class REPLTransformer(Transformer):
    from operator import add, mul, sub
    from operator import truediv as div

    number = int

    def __init__(self):
        self.vars = {}

    def days(self, value: str):
        n = int(value.rstrip("d"))
        return timedelta(days=n)

    def date(self, value: str):
        if value.count(".") == 1:
            return datetime.strptime(value, "%d.%m").replace(year=datetime.now().year)
        else:
            for pattern in ("%d.%m.%Y", "%d.%m.%y"):
                try:
                    return datetime.strptime(value, pattern)
                except:
                    pass
        raise TransformError(f"unknown date format: '{value}'")

    def assignment(self, name: str, value: int | timedelta | datetime):
        self.vars[name] = value

    def var(self, name: str):
        try:
            return self.vars[name]
        except KeyError:
            raise TransformError(f"unknown variable '{name}'")
