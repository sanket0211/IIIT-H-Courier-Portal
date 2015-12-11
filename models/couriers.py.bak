# -*- coding: utf-8 -*-
from plugin_notemptymarker import mark_not_empty, unmark_not_empty
sn = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
sn.define_table('courier',
                Field('first_name',requires=IS_NOT_EMPTY()),
                Field('last_name',requires=IS_NOT_EMPTY()),
                Field('Courier_Company',requires=IS_NOT_EMPTY()),
                Field('Hostel',requires=IS_IN_SET({'OBH','OBH-D','OBH-E','NBH','BAKUL','GH','GHEB','NBH Cellar'})),
                Field('time_stamp','datetime',requires=IS_NOT_EMPTY()),
                Field('Collected','boolean'))
