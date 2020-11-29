import logging
from argparse import ArgumentParser, RawTextHelpFormatter

import psycopg2

def createscore(conn, name, score):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS scores (name STRING, score INT)"
        )
        cur.execute("INSERT INTO scores VALUES (?,?)", (str(name), int(score)))
    conn.commit()

def printscores(conn):
    with conn.cursor() as cur:
        cur.exectue("SELECT name, score FROM scores")
        rows = cur.fetchall()
        conn.commit()
        for row in rows:
            print(row)

def main():
    name = "Bob"
    score = "10"
    opt = parse_cmdline()
    logging.basicConfig(level=logging.DEBUG if opt.verbose else logging.INFO)

    conn = psycopg2.connect(opt.dsn)
    createscore(conn,name,score)
    printscores(conn)

    # Close communication with the database.
    conn.close()



def parse_cmdline():
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        "dsn",
        help="database connection string\n\n"
             "For cockroach demo, use postgresql://<username>:<password>@<hostname>:<port>/bank?sslmode=require,\n"
             "with the username and password created in the demo cluster, and the hostname and port listed in the\n"
             "(sql/tcp) connection parameters of the demo cluster welcome message."
    )

    parser.add_argument("-v", "--verbose",
                        action="store_true", help="print debug info")

    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    main()