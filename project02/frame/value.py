class User:
    def __init__(self, id, pwd, name,imgname,email,regdate):
        self.id = id;
        self.pwd = pwd;
        self.name = name;
        self.imgname = imgname;
        self.email = email;
        self.regdate = regdate;
    def __str__(self):
        return self.id+' '+self.pwd+' '+self.name+ ' '+str(self.imgname)+ ' '+self.email+' '+ str(self.regdate) ;