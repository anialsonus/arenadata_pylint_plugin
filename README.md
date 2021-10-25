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

## Checkers

### Assertion message checker

Name: `assertion_message`

Checks: assertion message is provided, and it's not an empty string.
