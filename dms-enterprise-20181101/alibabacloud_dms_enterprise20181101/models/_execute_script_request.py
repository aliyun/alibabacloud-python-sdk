# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteScriptRequest(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
        real_login_user_uid: str = None,
        script: str = None,
        tid: int = None,
    ):
        # The ID of the database.
        # 
        # >  This parameter is equivalent to the DatabaseId parameter in the SearchDatabase, ListDatabases, and GetDatabase operations. You can call one of these operations to obtain the required database ID. For more information, see [SearchDatabase](https://help.aliyun.com/document_detail/141876.html), [ListDatabases](https://help.aliyun.com/document_detail/141873.html), and [GetDatabase](https://help.aliyun.com/document_detail/141869.html).
        # 
        # This parameter is required.
        self.db_id = db_id
        # Specifies whether the database is a logical database.
        # 
        # This parameter is required.
        self.logic = logic
        self.real_login_user_uid = real_login_user_uid
        # The SQL statements to be executed. Data query language (DQL) statements, data definition language (DDL) statements, and data manipulation language (DML) statements are supported. The control mode of the instance that you want to query determines whether you can execute DDL and DML statements.
        # 
        # This parameter is required.
        self.script = script
        # The ID of the tenant.
        # 
        # >  To obtain the tenant ID, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see [Tenant information](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.real_login_user_uid is not None:
            result['RealLoginUserUid'] = self.real_login_user_uid

        if self.script is not None:
            result['Script'] = self.script

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

