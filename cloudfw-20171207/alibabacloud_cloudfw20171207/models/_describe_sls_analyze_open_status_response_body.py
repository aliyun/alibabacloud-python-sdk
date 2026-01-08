# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSlsAnalyzeOpenStatusResponseBody(DaraModel):
    def __init__(
        self,
        open_status: str = None,
        request_id: str = None,
    ):
        self.open_status = open_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_status is not None:
            result['OpenStatus'] = self.open_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenStatus') is not None:
            self.open_status = m.get('OpenStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

