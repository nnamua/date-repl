from datetime import datetime, timedelta

from lark import Lark

from transformer import REPLTransformer, TransformError

if __name__ == "__main__":

    with open("grammar.lark", "r") as grammar_file:
        grammar = grammar_file.read()

    transformer = REPLTransformer()
    parser = Lark(grammar, parser="lalr", transformer=transformer)

    try:
        while True:
            line = input("> ")
            try:
                result = parser.parse(line)
            except Exception as te:
                print(te)
                continue

            if isinstance(result, datetime):
                print(f"{result:%d.%m.%Y}")
            elif isinstance(result, timedelta):
                print(f"{result.days}d")
            elif isinstance(result, int):
                print(result)
            elif result != None:
                print("Unknown error encountered.")
                exit(1)

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
