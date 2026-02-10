# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAlarmEventStackInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stack_info: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The stack information of the alert details.
        self.stack_info = stack_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stack_info is not None:
            result['StackInfo'] = self.stack_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StackInfo') is not None:
            self.stack_info = m.get('StackInfo')

        return self

