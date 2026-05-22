# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserDeliveryTaskResponseBody(DaraModel):
    def __init__(
        self,
        data_center: str = None,
        request_id: str = None,
        status: str = None,
        task_name: str = None,
    ):
        # The data center. Valid values:
        # 
        # *   cn: the Chinese mainland.
        # *   sg: outside the Chinese mainland.
        self.data_center = data_center
        # The request ID.
        self.request_id = request_id
        # The status of the delivery task.
        self.status = status
        # The name of the delivery task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

