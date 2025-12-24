# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserBusinessBehaviorResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        status_value: str = None,
    ):
        self.request_id = request_id
        self.status_value = status_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status_value is not None:
            result['StatusValue'] = self.status_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StatusValue') is not None:
            self.status_value = m.get('StatusValue')

        return self

