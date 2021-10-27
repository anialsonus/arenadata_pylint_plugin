# Arenadata Pylint Plugin

## Overview

Plugin for `pylint` with custom checkers used in tests in Arenadata projects.

## Requirements

- `pylint`
- `astroid`

## Installation

Via GitHub

`pip install git+https://github.com/arenadata/adcm_pytest_plugin`

Then add to your `pylint` configuration `arenadata_pylint_plugin` to `load-plugins` list.

Or if you want a specific checker, then `arenadta_pylint_plugin.{checker_name}`.

## Tests

To run tests manually you need to follow the steps:

1. Install required packages with
`pip install -r ./tests/requirements.txt`
2. Run tests
`pytest ./tests/`

## Checkers

### Assertion message checker

Name | Checks
--- | ---
`assertion_message` | assertion message is provided and is not an empty string

## Contribution

### How to run tests?
