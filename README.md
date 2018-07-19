# TM ML Tools

Tools for ML work with Google Colab. Commonly used in conjunction with [TM Colab Enhancement Suite](https://github.com/thinkingmachines/colab-enhancement-suite).

## Features

### IAM key authentication

See the [TM Colab Enhancement Suite](https://github.com/thinkingmachines/colab-enhancement-suite) documentation on how to use this.

### BigQuery magic

Colab cells that start with `%%run_bq` allow for running SQL against BigQuery and are parsed like so:

```
%%run_bq {DATAFRAME} {MAX-ROWS}
{QUERY}
```

- `DATAFRAME` is the name of the dataframe in which the query results will be stored.
- `MAX-ROWS` (optional) is the maximum number of rows to display in the UI.
- `QUERY` is the SQL query to run
