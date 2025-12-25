# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetryDataCorrectPreCheckRequest(DaraModel):
    def __init__(
        self,
        order_id: int = None,
        real_login_user_uid: str = None,
        tid: int = None,
    ):
        # The ID of the data change ticket. You can call the [ListOrders](https://help.aliyun.com/document_detail/144643.html) operation to query the ID of the data change ticket.
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
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.real_login_user_uid is not None:
            result['RealLoginUserUid'] = self.real_login_user_uid

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

