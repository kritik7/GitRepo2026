# GitRepo2026

## Statistical experimentation

`experiments/ab_test.py` is a small, dependency-free example of comparing
conversion rates in a two-group A/B test. It uses synthetic counts to show the
absolute conversion-rate difference and a two-sided pooled z-test p-value.

Run the example with `python experiments/ab_test.py`, and run its tests with
`python -m unittest discover -s experiments -p "test_*.py"`.

This is educational sample code, not an analysis of real experiment data. The
test assumes independent observations, a suitable random assignment, and
sufficient sample sizes; statistical significance alone does not establish
practical importance or prove a causal effect.