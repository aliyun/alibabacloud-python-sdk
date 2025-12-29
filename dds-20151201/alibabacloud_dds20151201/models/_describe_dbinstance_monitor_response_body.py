# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceMonitorResponseBody(DaraModel):
    def __init__(
        self,
        granularity: str = None,
        request_id: str = None,
    ):
        # The collection frequency of monitoring data for the instance. Valid value: **5**. Unit: seconds.
        self.granularity = granularity
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

