# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetDataCorrectBackupFilesRequest(DaraModel):
    def __init__(
        self,
        action_detail: Dict[str, Any] = None,
        order_id: int = None,
        tid: int = None,
    ):
        # The parameters that are required to perform the operation. You do not need to specify this parameter.
        self.action_detail = action_detail
        # The ID of the ticket. You can call the [ListOrders](https://help.aliyun.com/document_detail/144643.html) operation to obtain the ticket ID.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_detail is not None:
            result['ActionDetail'] = self.action_detail

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionDetail') is not None:
            self.action_detail = m.get('ActionDetail')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

