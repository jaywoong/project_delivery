class Sql:
    userlist = "SELECT * FROM user";
    userlistone = "SELECT * FROM user WHERE id= '%s' ";
    userinsert = "INSERT INTO user VALUES ('%s','%s','%s','%s','%s',CURRENT_DATE())";
    userdelete = "DELETE FROM user WHERE id= '%s' ";
    userupdate = "UPDATE user SET pwd='%s',name='%s', imgname='%s',email='%s' WHERE id= '%s' ";
