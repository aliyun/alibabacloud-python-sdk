# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataCorrectTaskDetailRequest(DaraModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        # The ID of the ticket. You can call the [CreateDataCorrectOrder](https://help.aliyun.com/document_detail/208388.html), [CreateDataImportOrder](https://help.aliyun.com/document_detail/208387.html), or [CreateFreeLockCorrectOrder](https://help.aliyun.com/document_detail/208386.html) operation to obtain the ticket ID.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The ID of the tenant.
        # 
        # > : To view the ID of the tenant, log on to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the "View information about the current tenant" section of the [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html) topic.
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

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

