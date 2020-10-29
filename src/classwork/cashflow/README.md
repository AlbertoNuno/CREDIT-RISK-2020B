# CashFlow

Python CLI application that allows you to calculate
the future and present value of a cashflow.

## Instructions

1. [Sync your repository](https://www.youtube.com/watch?v=59PaqRdbCx8&list=PLIbTa97DHk7jHdOW7Jb2dozV59bOWc58O&index=7)!
2. Create a branch called: `CW-CASHFLOW`
3. Complete the `CashFlow` class located at: `fintools/src/fintools/cashflow`.
4. Complete the `Main` class located at: `src/classwork/cashflow`
5. Add/commit/push your implementation.
4. Create a PR from `CW-CASHFLOW` into `solutions`.

Note: you can open an interactive python console with: `fintools console`

## Execution

**(2.5 pts)** CLI APP: You should be able to calculate the present value.
* Your implementation should use the `CashFlow` class.

```commandline
$ python -m cashflow present-value --amount 112.68 --n 12 --r 0.01
{
    "amount": 100.0,
    "n": 0
}
```

**(2.5 pts)** CLI APP: You should be able to calculate the future value.
* Your implementation should use the `CashFlow` class.

```commandline
$ python -m cashflow future-value --amount 100.00 --n 12 --r 0.01
{
    "amount": 112.68,
    "n": 12
}
```

**(1 pts)** Python: You should be able to calculate the present value of a cashflow using the `pv` method.
* The `pv` method should return a new cashflow instance.

```python
from fintools import CashFlow

cf = CashFlow(112.68, 12)

# Calculate present value
res = cf.pv(r=0.01)
# The result should be an instance of a cashflow
assert isinstance(res, CashFlow)
# Expected result as json
assert res.to_dict() == {"amount": 100.0, "n": 0}
```

**(2 pts)** Python: You should be 'shift' a cashflow to a new "n" value (similar to future value).
* The `shift` method should return a new cashflow instance.

```python
from fintools import CashFlow

cf = CashFlow(112.68, 12)

# Shift to n=24
res = cf.shift(n=24, r=0.01)
# The result should be an instance of a cashflow
assert isinstance(res, CashFlow)
# Expected result as json
assert res.to_dict() == {"amount": 126.97, "n": 24}
```

```python
from fintools import CashFlow

cf = CashFlow(112.68, 12)

# Shift to n=6
res = cf.shift(n=6, r=0.01)
# The result should be an instance of a cashflow
assert isinstance(res, CashFlow)
# Expected result as json
assert res.to_dict() == {"amount": 106.15, "n": 6}
```

**(2 pts)** Python: You should be able to merge two different cashflows.
* The merge should return a new cashflow instance.
* The merge should combine (sum) the amount values adjusted by the interest rate.
* The merge should get the second cashflow (other) at the time of the first one. Unless `reverse` is enabled.


```python
from fintools import CashFlow

cf_a = CashFlow(100, 0)
cf_b = CashFlow(112.68, 12)

# Merge a with b
res = cf_a.merge(other=cf_b, r=0.01)
# The result should be an instance of a cashflow
assert isinstance(res, CashFlow)
# Expected result as json
assert res.to_dict() == {"amount": 200.0, "n": 0}
```

```python
from fintools import CashFlow

cf_a = CashFlow(100, 0)
cf_b = CashFlow(112.68, 12)

# Merge a with b
res = cf_a.merge(other=cf_b, r=0.01, reverse=True)
# The result should be an instance of a cashflow
assert isinstance(res, CashFlow)
# Expected result as json
assert res.to_dict() == {"amount": 225.36, "n": 12}
```
