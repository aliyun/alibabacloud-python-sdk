# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PauseDataCorrectSQLJobRequest(DaraModel):
    def __init__(
        self,
        job_id: int = None,
        order_id: int = None,
        tid: int = None,
        type: str = None,
    ):
        # The ID of the SQL task. You can call the [GetDataCorrectTaskDetail](https://help.aliyun.com/document_detail/208481.html) or [ListDBTaskSQLJob](https://help.aliyun.com/document_detail/207049.html) operation to obtain the value of this parameter.
        # 
        # >  If Type is set to SINGLE, you must pass in the value of JobId to confirm the ID of the SQL task that you want to pause.
        self.job_id = job_id
        # The ID of the data change ticket. You can call the [ListOrders](https://help.aliyun.com/document_detail/144643.html) operation to query the ID of the data change ticket.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The tenant ID. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to query the tenant ID.
        self.tid = tid
        # The type of the pause operation. Valid values:
        # 
        # *   ALL: pauses all SQL tasks.
        # *   SINGLE: pauses a single SQL task.
        # 
        # This parameter is required.
        self.type = type

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

