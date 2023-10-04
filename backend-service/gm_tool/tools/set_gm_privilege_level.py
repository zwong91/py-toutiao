#encoding=utf-8
import sys
import pymysql
pymysql.install_as_MySQLdb()

db_addr = "127.0.0.1"
db_user = 'dgame'
db_pwd = "123456"
db_name = 'dgame'

def set_gm_privilege_level(roleid, level):
	db = MySQLdb.connect(db_addr, db_user, db_pwd, db_name)
	cursor = db.cursor()
	
	sqlquery = "update player set gm_previllege = " + level + " where roleid = " + roleid
	cursor.execute(sqlquery)
	db.commit()
	
	
if __name__ == "__main__":
	if len(sys.argv) < 3:
		print sys.argv[0] + " [roleid] [privilege_level]"
		exit()
	roleid = sys.argv[1]
	level = sys.argv[2]
	set_gm_privilege_level(roleid, level)