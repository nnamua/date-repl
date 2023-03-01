# date-repl

A tool to quickly calculate the difference between dates, add offsets to dates and more.

## Usage

Type an expression using dates (formatted as `dd.mm.yyyy`), days (integer with suffix `d`) or regular integers. You can also assign variables and use them later!

### Supported operations

All operations between `datetime.datetime`, `datetime.timedelta` and `int` are supported. See the Python documentation for more information: [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) and [timedelta](https://docs.python.org/3/library/datetime.html#timedelta-objects)

## Usecases

### Calculate difference between two dates:

```
> 04.08.1999 - 19.03.1999
138d
```

### Add offset to date
```
> 19.03.1999 + 138d
04.08.1999
```

### Assign and use variables
```
> x = 04.08.1999 - 19.03.1999
> x + 10d
148d
```