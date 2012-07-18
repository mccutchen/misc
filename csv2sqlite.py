import sys
import sqlite

def convert(schemapath, csvpath, csvseparator, dbpath):
    schema = file(schemapath).read()
    
    db = sqlite.connect(dbpath)
    cursor = db.cursor()
    try:
        cursor.execute(schema)
    except sqlite.Error, e:
        print "Oops! Database error:"
        print e
        print "Query:\n%s" % schema
        sys.exit(0)

    data = CSVFile(csvpath, csvseparator)
    columns = data.next()

    insert = "insert into web_schedule %s values " % repr(tuple(columns)).replace("'","")

    for row in data:
        try:
            query = insert + repr(tuple(row))
            cursor.execute(query)
            db.commit()
        except sqlite.Error, e:
            print "Database error: %s" % e
            print "\nQuery:\n%s" % query
            sys.exit(0)

    print "Finished importing data..."

    cursor.execute("select class_number from web_schedule")
    print "Number of records in db: %s" % cursor.rowcount
    print "Ich bin ein strudel"

def CSVFile(path, separator):
    try:
        fp = file(path)
    except IOError, e:
        print e

    for line in fp:
        yield line.replace("\n","").split(separator)


if __name__ == "__main__":

    print "Beginning my run..."
    
    schema = "C:\Documents and Settings\wrm2110\My Documents\cce-database\schema.sql"
    csv = "C:\Documents and Settings\wrm2110\My Documents\cce-database\data.txt"
    sep = "\t"
    db = "C:\Documents and Settings\wrm2110\My Documents\cce-database\db.db"
    convert(schema, csv, sep, db)

    print "\nWas ist los?"    
