import logging
from IPython.core.magic import register_cell_magic
from pandas.io import gbq
import pandas_gbq


def add_bq_magic(project_id, parent_globals):
  # Silence annoying warning logs
  logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)
  logging.getLogger('google.auth._default').setLevel(logging.ERROR)


  @register_cell_magic
  def run_bq(line, cell):
    """Quickly runs a query on BigQuery.
    
    The supported syntax is:
    
      %%run_bq <(Optional) df_var_name> <(Optional) head_rows = 5>
      SELECT
        ...
      FROM
        ...
    
    The magic returns the query result as a dataframe. To assign that dataframe to
    a variable, simply pass it as the first parameter to the cell magic. Pass
    the number of rows (as head) as a second parameter if you do not want the
    whole dataframe to be displayed.
    """
    # TODO: Refactor args parsing below
    args = line.split()
    df_var_name = args[0] if len(args) > 0 else None
    head_rows = int(args[1]) if len(args) > 1 else None
    
    try:
      df = gbq.read_gbq(cell, project_id=project_id, verbose=False, dialect='standard')
    except pandas_gbq.gbq.GenericGBQException as e:
      print('BQ ERROR')
      print(e.args[0])
      return

    if df_var_name:
      parent_globals[df_var_name] = df

    if head_rows is None:
      return df
    elif head_rows == 0:
      print('done')
    else:
      print('{} rows:'.format(head_rows))
      return df.head(head_rows)  
