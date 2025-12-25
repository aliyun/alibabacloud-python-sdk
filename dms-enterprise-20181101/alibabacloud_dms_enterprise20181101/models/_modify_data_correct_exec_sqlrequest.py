# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDataCorrectExecSQLRequest(DaraModel):
    def __init__(
        self,
        exec_sql: str = None,
        order_id: int = None,
        real_login_user_uid: str = None,
        tid: int = None,
    ):
        # The new SQL script.
        # 
        # This parameter is required.
        self.exec_sql = exec_sql
        # The ID of the data change ticket.
        # 
        # This parameter is required.
        self.order_id = order_id
        self.real_login_user_uid = real_login_user_uid
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exec_sql is not None:
            result['ExecSQL'] = self.exec_sql

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.real_login_user_uid is not None:
            result['RealLoginUserUid'] = self.real_login_user_uid

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecSQL') is not None:
            self.exec_sql = m.get('ExecSQL')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

