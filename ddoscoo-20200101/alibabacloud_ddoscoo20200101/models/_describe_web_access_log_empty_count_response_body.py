# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWebAccessLogEmptyCountResponseBody(DaraModel):
    def __init__(
        self,
        available_count: int = None,
        request_id: str = None,
    ):
        # The remaining quota that you can clear the Logstore.
        self.available_count = available_count
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_count is not None:
            result['AvailableCount'] = self.available_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableCount') is not None:
            self.available_count = m.get('AvailableCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

