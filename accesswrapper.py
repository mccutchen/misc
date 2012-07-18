import win32com.client

class AccessWrapper:
    def __init__(self, path, table):
        self.path = path
        self.table = table
        self.conn = win32com.client.Dispatch(r'ADODB.Connection')
        self.conn.Open('PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=%s;' % self.path)
        self.rs = win32com.client.Dispatch(r'ADODB.Recordset')
        self.execute("[%s]" % self.table)

    def execute(self, query):
        self.rs.Open(query, self.conn, 1, 3)
        self.rs.MoveFirst()

    def columns(self):
        columns = list()
        for i in range(self.rs.Fields.Count):
            columns.append(self.rs.Fields.Item(i).Name)
        return columns

    def __iter__(self):    
        return self

    def next(self):
        row = list()
        for i in range(self.rs.Fields.Count):
            row.append(self.rs.Fields.Item(i).Value)
        return row

        if rs.EOF:
            raise StopIteration
        else:
            rs.MoveNext()


if __name__ == "__main__":
    path = "C:\Documents and Settings\wrm2110\My Documents\cce-database\database.mdb"
    table = "web_schedule"
    db = AccessWrapper(path, table)

    print db.columns()
    r = db.next()
    for field in r:
        print "%s (%s)" % (field, type(field))