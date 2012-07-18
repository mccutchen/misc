from win32com import client

def describe(dbpath, tablename):
    conn = client.Dispatch(r'ADODB.Connection')
    dsn = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=%s;' % dbpath
    conn.Open(dsn)

    rs = client.Dispatch(r'ADODB.Recordset')
    rs.Open('[%s]' % tablename, conn, 1, 3)

    fields = dict()
    for r in range(rs.Fields.Count):
        fields[rs.Fields.Item(r).Name] = (rs.Fields.Item(r).Type, rs.Fields.Item(r).DefinedSize)

    print "Table %s" % tablename
    print
    print "Name, type, size"
    print
    for name in fields.keys():
        print "%s, %s, %s" % (name, fields[name][0], fields[name][1])

if __name__ == "__main__":
    print "Describing a table...\n"

    describe("C:\Documents and Settings\wrm2110\My Documents\cce-database\database.mdb","web_schedule")    



##AdoEnums.DataType.ARRAY
##AdoEnums.DataType.BIGINT
##AdoEnums.DataType.BINARY
##AdoEnums.DataType.BOOLEAN
##AdoEnums.DataType.BSTR
##AdoEnums.DataType.CHAPTER
##AdoEnums.DataType.CHAR
##AdoEnums.DataType.CURRENCY
##AdoEnums.DataType.DATE
##AdoEnums.DataType.DBDATE
##AdoEnums.DataType.DBTIME
##AdoEnums.DataType.DBTIMESTAMP
##AdoEnums.DataType.DECIMAL
##AdoEnums.DataType.DOUBLE
##AdoEnums.DataType.EMPTY
##AdoEnums.DataType.ERROR
##AdoEnums.DataType.FILETIME
##AdoEnums.DataType.GUID
##AdoEnums.DataType.IDISPATCH
##AdoEnums.DataType.INTEGER
##AdoEnums.DataType.IUNKNOWN
##AdoEnums.DataType.LONGVARBINARY
##AdoEnums.DataType.LONGVARCHAR
##AdoEnums.DataType.LONGVARWCHAR
##AdoEnums.DataType.NUMERIC
##AdoEnums.DataType.PROPVARIANT
##AdoEnums.DataType.SINGLE
##AdoEnums.DataType.SMALLINT
##AdoEnums.DataType.TINYINT
##AdoEnums.DataType.UNSIGNEDBIGINT
##AdoEnums.DataType.UNSIGNEDINT
##AdoEnums.DataType.UNSIGNEDSMALLINT
##AdoEnums.DataType.UNSIGNEDTINYINT
##AdoEnums.DataType.USERDEFINED
##AdoEnums.DataType.VARBINARY
##AdoEnums.DataType.VARCHAR
##AdoEnums.DataType.VARIANT
##AdoEnums.DataType.VARNUMERIC
##AdoEnums.DataType.VARWCHAR
##AdoEnums.DataType.WCHAR