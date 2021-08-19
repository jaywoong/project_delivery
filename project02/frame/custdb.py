from frame.db import Db
from frame.sql import Sql
from frame.value import User


class UserDB(Db):
    def update(self, id, pwd, name, imgname, email):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userupdate % ( pwd, name,imgname,email, id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
            print(ErrorCode.e0002)
        finally:
            super().close(conn, cursor);
    def delete(self,id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userdelete % id);
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
            print(ErrorCode.e0002)
        finally:
            super().close(cursor, conn)
    def insert(self,id, pwd, name,imgname,email):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userinsert % (id, pwd, name,imgname,email));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor, conn)
    def selectone(self,id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlistone % id);
        c = cursor.fetchone()
        user = User(c[0],c[1],c[2],c[3],c[4],c[5])
        super().close(cursor, conn)
        return user;


    def select(self):
        all = [];
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlist);
        result = cursor.fetchall();
        for c in result:
            user = User(c[0],c[1],c[2],c[3],c[4],c[5])
            all.append(user)

        super().close(cursor,conn);
        return all;

# userlist Test Function ................
def userlist_test():
    users = UserDB().select();
    for u in users:
        print(u);

def userlistone_test():
    users = UserDB().selectone('test03');
    print(users);
def userinsert_test():
    UserDB().insert('test04','pwd04','정우성','jws.jpg','test04@gmail.com');

def userupdate_test():
    UserDB().update('test04','pwd04','감우성','test04','test04@gmail.com');

def userdel_test():
    UserDB().delete('test07');

if __name__ == '__main__':
    userinsert_test()
