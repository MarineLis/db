import psycopg2
import os


def get_env(name):
    return os.environ.get(name)


if __name__ == "__main__":
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        host="192.168.99.100",
        password="postgres",
        #password="xu40e5",
        #host="localhost",
    )
    cursor = conn.cursor()
    cursor.execute("DROP TABLE ZNO_RESULTS_19_20, Buffer_table;")
    conn.commit()
    cursor.close()
    conn.close()

#Buffer_table