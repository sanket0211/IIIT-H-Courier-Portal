# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

###CAS LOGIN

CAS.login_url='https://login.iiit.ac.in/cas/login'
CAS.check_url='https://login.iiit.ac.in/cas/validate'
CAS.logout_url='https://login.iiit.ac.in/cas/logout'
CAS.my_url='127.0.0.1:8000/IIIT_courier_portal/default/manage'

#########################################################################
# To make sure everyone logins
#if not session.token and not request.function=='login':
 #       redirect(URL(r=request, f='login'))


@auth.requires_login()
def index():
    nam=sn().select(sn.courier.ALL).as_list()
    total=len(nam)
    coll=0
    notcoll=0
    for i in nam:
        if i['Collected']==True:
            coll=coll+1
        else:
            notcoll=notcoll+1
    
    ##redirect(URL('manage'))
    return locals()

@auth.requires_membership('managers')
def new_courier():
    nam=sn().select(sn.courier.ALL).as_list()
    total=len(nam)
    coll=0
    notcoll=0
    for i in nam:
        if i['Collected']==True:
            coll=coll+1
        else:
            notcoll=notcoll+1
    mark_not_empty(sn.courier)
    sn.courier.time_stamp.default=request.now
    sn.courier.time_stamp.writable=False
    sn.courier.Collected.writable=False
    sn.courier.Collected.readable=False
    sn.courier.time_stamp.readable=False
    form=SQLFORM(sn.courier).process()
    if form.accepted:
        session.flash="Entered!"
        redirect(URL('test2'))
    return locals()
@auth.requires_login()
def faq():
    return locals()

@auth.requires_membership('managers')
def cash():
    nam=sn().select(sn.courier.ALL).as_list()
    total=len(nam)
    coll=0
    notcoll=0
    for i in nam:
        if i['Collected']==True:
            coll=coll+1
        else:
            notcoll=notcoll+1
    form=SQLFORM(db.cash).process()
    if form.accepted:
        session.flash="Entered!"
        redirect(URL('te'))
    return locals()
@auth.requires_membership('managers')
def userprofileform():
    form=SQLFORM(db.anonymousprofile).process()
    if form.accepted:
        redirect(URL('userprofile'))
    return locals()
@auth.requires_membership('managers')
def userprofile():
    flag=0
    name=db().select(db.anonymousprofile.ALL).as_list()[-1]
    first=name['first_name']
    first=first.lower()
    last=name['last_name']
    user = db.auth_user
    r = user.first_name
    q = r==first
    s = db(q)
    for row in db(db.auth_user.first_name.lower()==first.lower() and db.auth_user.last_name.lower()==last.lower()).select():
        user=row.email
        first=row.first_name
        last=row.last_name
        flag=1
    if flag!=1:
        session.flash="No Such User"
        redirect(URL('userprofileform'))
    
    #cash1=auth.user.Wallet
    email=user
    nam=sn().select(sn.courier.ALL).as_list()
    coll=0
    notcoll=0
    for i in nam:
        if i['first_name'].lower()==first.lower() and i['last_name'].lower()==last.lower():
            if i['Collected']==True:
                coll=coll+1
            else:
                notcoll=notcoll+1
    total=coll+notcoll
    name=db().select(db.auth_user.ALL).as_list()
    for i in name:
        if i['email']==email:
            cash1=i['Wallet']
            p=i['Photo']
            room=i['Room_No']
            hostel=i['Hostel']
            contact=i['Contact_No']
            roll=i['Roll_No']
    return locals()
        
        
    

        
@auth.requires_login()
def profile():
    
    form3=SQLFORM(db.edit1).process()
    user=auth.user.email
    row=db(db.auth_user.email==user).select().first()
    if form3.accepted:
        name=db().select(db.edit1.ALL).as_list()[-1]
        photo=name['Edit_Photo']
        row.update_record(Photo=photo)
        redirect(URL('profile'))
    form4=SQLFORM(db.roo).process()
    user=auth.user.email
    row=db(db.auth_user.email==user).select().first()
    if form4.accepted:
        name=db().select(db.roo.ALL).as_list()[-1]
        photo=name['Edit_Room_No']
        row.update_record(Room_No=photo)
        redirect(URL('profile'))
    form5=SQLFORM(db.hoste).process()
    user=auth.user.email
    row=db(db.auth_user.email==user).select().first()
    if form5.accepted:
        name=db().select(db.hoste.ALL).as_list()[-1]
        photo=name['Edit_Hostel']
        row.update_record(Hostel=photo)
        redirect(URL('profile'))
    form6=SQLFORM(db.contac).process()
    user=auth.user.email
    row=db(db.auth_user.email==user).select().first()
    if form6.accepted:
        name=db().select(db.contac.ALL).as_list()[-1]
        photo=name['Edit_Number']
        row.update_record(Contact_No=photo)
        redirect(URL('profile'))
    first=auth.user.first_name
    last=auth.user.last_name
    
    #cash1=auth.user.Wallet
    email=auth.user.email
    nam=sn().select(sn.courier.ALL).as_list()
    coll=0
    notcoll=0
    for i in nam:
        if i['first_name'].lower()==first.lower() and i['last_name'].lower()==last.lower():
            if i['Collected']==True:
                coll=coll+1
            else:
                notcoll=notcoll+1
    total=coll+notcoll
    name=db().select(db.auth_user.ALL).as_list()
    for i in name:
        if i['email']==email:
            cash1=i['Wallet']
            p=i['Photo']
            room=i['Room_No']
            hostel=i['Hostel']
            contact=i['Contact_No']
            roll=i['Roll_No']
    return locals()
@auth.requires_login()
def profile1():
    
    form3=SQLFORM(db.edit1).process()
    user=auth.user.email
    row=db(db.auth_user.email==user).select().first()
    if form3.accepted:
        name=db().select(db.edit1.ALL).as_list()[-1]
        photo=name['Edit_Photo']
        row.update_record(Photo=photo)
        redirect(URL('profile'))
    form4=SQLFORM(db.roo).process()
    user=auth.user.email
    row=db(db.auth_user.email==user).select().first()
    if form4.accepted:
        name=db().select(db.roo.ALL).as_list()[-1]
        photo=name['Edit_Room_No']
        row.update_record(Room_No=photo)
        redirect(URL('profile'))
    form5=SQLFORM(db.hoste).process()
    user=auth.user.email
    row=db(db.auth_user.email==user).select().first()
    if form5.accepted:
        name=db().select(db.hoste.ALL).as_list()[-1]
        photo=name['Edit_Hostel']
        row.update_record(Hostel=photo)
        redirect(URL('profile'))
    form6=SQLFORM(db.contac).process()
    user=auth.user.email
    row=db(db.auth_user.email==user).select().first()
    if form6.accepted:
        name=db().select(db.contac.ALL).as_list()[-1]
        photo=name['Edit_Number']
        row.update_record(Contact_No=photo)
        redirect(URL('profile'))
    first=auth.user.first_name
    last=auth.user.last_name
    
    #cash1=auth.user.Wallet
    email=auth.user.email
    nam=sn().select(sn.courier.ALL).as_list()
    coll=0
    notcoll=0
    for i in nam:
        if i['first_name'].lower()==first.lower() and i['last_name'].lower()==last.lower():
            if i['Collected']==True:
                coll=coll+1
            else:
                notcoll=notcoll+1
    total=coll+notcoll
    name=db().select(db.auth_user.ALL).as_list()
    for i in name:
        if i['email']==email:
            cash1=i['Wallet']
            p=i['Photo']
            room=i['Room_No']
            hostel=i['Hostel']
            contact=i['Contact_No']
            roll=i['Roll_No']
    return locals()

def te():
    name=db().select(db.auth_user.ALL).as_list()
    ca=db().select(db.cash.ALL).as_list()[-1]
    emai=ca['email']
    su=ca['Add_Or_Subtract']
    if su=='-':
        var='subtracted'
        d='from'
    else:
        var='added'
        d='to'
    f=ca['Transaction_Amount']
    row=db(db.auth_user.email==emai).select().first()
    for i in name:
        if i['email']==emai:
            j=i['Wallet']
            if su=='-':
                f=int(f)
                f=-f
            s=int(j)+int(f)
            if s<0:
                session.flash="Not enough money in Wallet. Try again."
                redirect(URL('cash'))
            elif s>3000:
                session.flash="Sorry. You have exceeded your Wallet Limit(Rs. 3000)."
                redirect(URL('cash'))
            else:
             row.update_record(Wallet=s)
            #for row in db(db.auth_user.first_name.lower()==first).select():
             if su=='-':
                f=-f
             mail.send(to=[emai],
             subject='Wallet Update',
             message="Amount of Rs. "+str(f)+" has been "+var+" "+d+" your Wallet."+" At present, the total amount in your Wallet is Rs. "+str(s)+".",
             sender=None)
             session.flash="An automated email has been sent to "+emai+"."
             redirect(URL('index'))
        
    return locals()
    

def test2():
    name=sn().select(sn.courier.ALL).as_list()[-1]
    first=name['first_name']
    comp=name['Courier_Company']
    first=first.lower()
    last=name['last_name']
    user = db.auth_user
    r = user.first_name
    q = r==first
    s = db(q)
    comp=str(comp)
    for row in db(db.auth_user.first_name.lower()==first.lower() and db.auth_user.last_name.lower()==last.lower()).select():
        mail.send(to=[row.email],
                  subject='New Courier',
              message='You have recieved a new courier from '+comp,
              sender=None)
        session.flash="An automated email has been sent to "+ first + " " + last + "."
    redirect(URL('index'))
    return locals()
@auth.requires_login()
def manage():
    nam=sn().select(sn.courier.ALL).as_list()
    total=len(nam)
    coll=0
    notcoll=0
    for i in nam:
        if i['Collected']==True:
            coll=coll+1
        else:
            notcoll=notcoll+1
    grid=SQLFORM.smartgrid(sn.courier,
                           editable=auth.has_membership('managers'),
                           deletable=auth.has_membership('none'),
                           create=auth.has_membership('none'),
                           links_in_grid=False,links=None)
    #rows=sn(sn.courier).select()
    return locals()

def user():
    nam=sn().select(sn.courier.ALL).as_list()
    total=len(nam)
    coll=0
    notcoll=0
    for i in nam:
        if i['Collected']==True:
            coll=coll+1
        else:
            notcoll=notcoll+1
    mark_not_empty(db.auth_user)
    mark_not_empty(db.passkey)
    form2=SQLFORM(db.passkey).process()
    if form2.accepted:
        session.flash="Checking..."
        name=db().select(db.passkey.ALL).as_list()[-1]
        if name['passkey']==99799:
            session.flash="Accepted"
            redirect(URL('user2'))
        else:
            session.flash="Rejected. Try Again"
            redirect(URL('user'))
    if 'register' in request.args:
        fields_to_hide = ['Wallet']
        for fieldname in fields_to_hide:
            field = db.auth_user[fieldname]
            field.readable = field.writable = False
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    
    form=auth()
    
    return locals()
    
def user2():
    nam=sn().select(sn.courier.ALL).as_list()
    total=len(nam)
    coll=0
    notcoll=0
    for i in nam:
        if i['Collected']==True:
            coll=coll+1
        else:
            notcoll=notcoll+1
    mark_not_empty(db.auth_user)
    if 'register' in request.args:
        fields_to_hide = ['Wallet']
        for fieldname in fields_to_hide:
            field = db.auth_user[fieldname]
            field.readable = field.writable = False
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    
    form=auth()
    
    
    return locals()
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)


#############################################################
###lOGIN SIGNUP AND VALIDATION USING cas



def login():
    """
        Method to fetch the user detials from CAS
        Redirects to respective user interface
        """
    session.login = 0
    session.token = CAS.login(request)
    
    user_email=session.token
    
    session.email = user_email
    session.login = 2
    redirect(URL('default','index'))


    # check if admin
    #is_admin = db(db.Admins.email==user_email).select(db.Admins.ALL)
    #if is_admin:
    #    session.login = 1
    #    session.username = is_admin[0]['name']
    #    redirect(URL('admin','index'))
    #else:
    #    session.login = 2
    #    redirect(URL('default','index'))


def logout():
    """
    Logout of CAS server.
    """
    session.token = None
    session.login = 0
    CAS.logout()
