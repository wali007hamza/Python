import sys
import sqlite3


location_of_chrome_cookie = "C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"
if __name__ == "__main__":
    if(len(sys.argv) != 3):
        raise ValueError(
            "Need the computer username and hostname as the command line arguments")
    username = sys.argv[1]
    hostname = sys.argv[2]
    cookie_path = str.format(location_of_chrome_cookie, username=username)
    print(cookie_path)
    query = str.format("SELECT * FROM cookies WHERE host_key LIKE '%{hostname}%'", hostname=hostname)
    print(query)
    conn = sqlite3.connect(cookie_path)

    c = conn.cursor()
    # for row in c.execute(query):
    #     print(row)

    delete_query = str.format("DELETE FROM cookies WHERE host_key LIKE '%{hostname}%'", hostname=hostname)
    response = c.execute(delete_query)
    print(response)
    conn.close()
