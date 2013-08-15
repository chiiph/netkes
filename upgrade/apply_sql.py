import glob
from netkes import common
from netkes.account_mgr import get_cursor

def apply_sql():
    common.set_config(common.read_config_file())
    sql_files = glob.glob('/opt/openmanage/net_kes/sql/*.sql') 
    sql_files = [(x.split('/')[-1], open(x).readlines()) for x in sql_files]
    sql_files = sorted(sql_files, key=lambda x: x[0])

    for sql_file in sql_files:
        with get_cursor(common.get_config()) as cur:
            cur.execute('select * from sql_updates where name=%s', (sql_file[0], ))
            if cur.rowcount == 0:
                cur.execute(''.join(sql_file[1]))
                cur.execute('insert into sql_updates (name) values (%s)', (sql_file[0], ))

if __name__ == '__main__':
    apply_sql()