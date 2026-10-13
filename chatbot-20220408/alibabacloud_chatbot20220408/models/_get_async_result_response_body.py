# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAsyncResultResponseBody(DaraModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The execution result data of the customer service.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The execution status.
        # | Value | Description |
        # |----|----|
        # | Success | The task is executed. |
        # | Runninig | The task is being executed. |
        # | Fail | The task failed to be executed. |
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

