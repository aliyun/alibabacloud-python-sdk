# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PauseDataExportJobRequest(DaraModel):
    def __init__(
        self,
        job_id: int = None,
        order_id: int = None,
        tid: int = None,
    ):
        # The ID of the SQL result set export task. You can call the [GetDataExportOrderDetail](https://help.aliyun.com/document_detail/465911.html) operation to obtain the value of this parameter. If you set this parameter to Null, no SQL result set export task is suspended.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The ticket ID. You can call the [ListOrders](https://help.aliyun.com/document_detail/144643.html) operation to query the ticket ID.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the DMS console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

