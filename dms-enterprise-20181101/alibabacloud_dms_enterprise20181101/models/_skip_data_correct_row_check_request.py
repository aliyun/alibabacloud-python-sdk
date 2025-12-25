# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SkipDataCorrectRowCheckRequest(DaraModel):
    def __init__(
        self,
        order_id: int = None,
        real_login_user_uid: str = None,
        reason: str = None,
        tid: int = None,
    ):
        # The ticket ID. You can call the [ListOrders](https://help.aliyun.com/document_detail/144643.html) operation to obtain the ticket ID.
        # 
        # This parameter is required.
        self.order_id = order_id
        self.real_login_user_uid = real_login_user_uid
        # The reason for skipping the verification on the number of rows in the precheck for data change.
        # 
        # This parameter is required.
        self.reason = reason
        # The tenant ID. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
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

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

