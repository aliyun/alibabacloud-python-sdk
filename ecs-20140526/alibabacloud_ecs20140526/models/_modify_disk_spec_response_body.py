# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDiskSpecResponseBody(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The order ID.
        # 
        # > An order ID is returned only when you change or modify a subscription disk.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id
        # The task ID for the disk type change.
        # 
        # > This parameter is not returned if you only modified the performance level (PL) of an ESSD.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

