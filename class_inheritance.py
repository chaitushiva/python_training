class myrouter(object):
    ''' class for router'''
    def __init__(self,router_name,model,serial_no,ios):
        self.router_name=router_name
        self.model=model
        self.serial_no=serial_no
        self.ios=ios
    def print_routerinfo(self,manu_date):
        print("routername and manufacturing date:",self.router_name,self.manu_date)

router1 = myrouter('first_router','1234','456','ios')
print(router1.router_name)

class new_router(myrouter):
    '''inheretence'''
    def __init__(self,router_name,model,serial_no,ios,part_no):
            myrouter.__init__(self,router_name,model,serial_no,ios)
            self.part_no=part_no
    def print_new_router_partno(self,part_no):
        print(self.part_no)

router2 = new_router('r2','newrouter','12','34','134536')
print(router2.model)
print(router2.part_no)

print (issubclass(new_router,myrouter))  #way to find if new_router is the childclass of myrouter(parentclass)
