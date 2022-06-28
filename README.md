# [Get Started from Pytest Docs](https://docs.pytest.org/en/7.1.x/getting-started.html)

## Install pytest

*pytest requires: Python 3.7+ or PyPy3.*

Run the following command in your command line:

```shell
pip install -U pytest
```

Check that you installed the correct version:

```shell
$ pytest --version
# pytest 7.1.2
```

## Create your first test
Create a new file called `test_sample.py`, containing a function, and a test:

```python
# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
```
