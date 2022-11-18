import ibm_db
conn = ibm_db.connect("DATABASE=budb;HOSTNAME=9938aec0-8105-433e-8bf9-0fbb7e483086.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud")
print(conn)
print("Connection Successful....")