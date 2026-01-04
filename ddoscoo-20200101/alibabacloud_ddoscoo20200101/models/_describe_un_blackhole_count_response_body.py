# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUnBlackholeCountResponseBody(DaraModel):
    def __init__(
        self,
        remain_count: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The remaining quota that you can deactivate blackhole filtering.
        self.remain_count = remain_count
        # The ID of the request.
        self.request_id = request_id
        # The total quota that you can deactivate blackhole filtering.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remain_count is not None:
            result['RemainCount'] = self.remain_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemainCount') is not None:
            self.remain_count = m.get('RemainCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

