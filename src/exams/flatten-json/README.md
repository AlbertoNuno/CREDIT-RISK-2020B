# EX01: Flatten JSON

This is the practical section of the first exam.

## Instructions

1. [Sync your repository](https://www.youtube.com/watch?v=59PaqRdbCx8&list=PLIbTa97DHk7jHdOW7Jb2dozV59bOWc58O&index=7)!
2. Create a branch called: `EX01-FLATTEN`
3. Solve the problem!
    * (3 pts) Your solution has a `__main__.py` & `main.py` that work correctly.
    * (6 pts) Your solution contains a recursive function called `flatten_dict` on `utils.py` file that works as expected.
    * (6 pts) There are two commands on your python app:
        * `show`: display the json.
        * `flatten`: flattens the json.
4. Add, commit & push your solution to github.
5. Create a PR from `EX01-FLATTEN` into `solutions`.

The `flatten_dict` function takes a dictionary and returns a flat version of that dictionary.

```python
example_input = {
    "a": 1,
    "b": {
        "c": 2
    }
}

example_output = flatten_dict(example_input)
```

In this case, the `example_output` should be:

```text
{
    "a": 1,
    "b.c": 2
}
```

**Note**: be sure that your code works as expected since the execution should run without any errors to get the corresponding points.

## Execution!

**(4 pts) EX 1**

This is a nested dictionary (i.e., a dictionary that potentially contains more dictionaries):

```text
$ python -m flatten-json show --file flatten-json/ex-1.json
{
    "a": 1,
    "b": 2,
    "c": {
        "d": 5,
        "e": 6
    }
}
```

Flat version:

```text
$ python -m flatten-json flatten --file flatten-json/ex-1.json
{
    "a": 1,
    "b": 2,
    "c.d": 5,
    "c.e": 6
}
```
**(4 pts) EX 2**

Assume that the dictionary can contain an arbitrary number of nested levels.

```text
$ python -m flatten-json show --file flatten-json/ex-2.json
{
    "a": 1,
    "b": 2,
    "c": {
        "d": 5,
        "e": 6
    },
    "f": {
        "g": 7,
        "h": {
            "i": {
                "j": 8
            }
        }
    }
}
```

Flat version:

```text
$ python -m flatten-json flatten --file flatten-json/ex-2.json
{
    "a": 1,
    "b": 2,
    "c.d": 5,
    "c.e": 6,
    "f.g": 7,
    "f.h.i.j": 8
}
```

**(4 pts) EX 3**
If the dictionary contains a list with values, the flat version should use the "index" as a key:
```text
$ python -m flatten-json show --file flatten-json/ex-3.json
{
    "a": 1,
    "b": 2,
    "c": [
        3,
        4,
        5
    ]
}
```

Flat version:

```text
$ python -m flatten-json flatten --file flatten-json/ex-3.json
{
    "a": 1,
    "b": 2,
    "c.0": 3,
    "c.1": 4,
    "c.2": 5
}
```

**(4 pts) EX 4**

Note that a list can contain more dictionaries and/or more lists. Everything should be flatten out in the final result.

```text
$ python -m flatten-json show --file flatten-json/ex-4.json
{
    "a": 1,
    "b": [
        {
            "c": 2
        },
        {
            "d": 3,
            "e": {
                "f": 4,
                "g": 5
            }
        }
    ]
}
```

Flat version:

```text
$ python -m flatten-json flatten --file flatten-json/ex-4.json
{
    "a": 1,
    "b.0.c": 2,
    "b.1.d": 3,
    "b.1.e.f": 4,
    "b.1.e.g": 5
}
```

**(4 pts) EX 5**

```text
$ python -m flatten-json show --file flatten-json/ex-5.json
{
    "a": 1,
    "b": [
        {
            "c": 2
        },
        {
            "d": 3,
            "e": [
                4,
                5,
                {
                    "f": {
                        "g": 6
                    }
                }
            ]
        }
    ]
}

```
Flat version:
```text
$ python -m flatten-json flatten --file flatten-json/ex-5.json
{
    "a": 1,
    "b.0.c": 2,
    "b.1.d": 3,
    "b.1.e.0": 4,
    "b.1.e.1": 5,
    "b.1.e.2.f.g": 6
}
```

**(5 pts) Secret tests**

Your code will also be tested against a set of secret tests.
