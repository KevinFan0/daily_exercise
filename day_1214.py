def sql_db_table(db,
                 table,
                 alias='',
                 with_nolock=1,
                 format_to_ol=1  # 默认等于1时，把库名和表名按照规律替换成线上的形式
                 ):
    if format_to_ol == 0:
        db_table = db + '..' + table
    else:
        db_table = table.replace('_dw_', '..')
        n = db_table.find('..')
        # 特殊名称的表的处理，必须加上[表名]
        if db_table[n+2:] in ['user']:
            db_table = db_table[:n+2] + '[' + db_table[n+2:] + ']'
    if alias != '':
        db_table += ' as ' + alias
    if with_nolock == 1:
        db_table += ' with (nolock)'
    return db_table


if __name__ == '__main__':
    print(sql_db_table('ppdai_riskdata', 'antifraudstatus', format_to_ol=0))