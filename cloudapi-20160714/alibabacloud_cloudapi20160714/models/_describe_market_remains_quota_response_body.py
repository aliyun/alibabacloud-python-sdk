# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMarketRemainsQuotaResponseBody(DaraModel):
    def __init__(
        self,
        remains_quota: int = None,
        request_id: str = None,
    ):
        # The remaining quota.
        self.remains_quota = remains_quota
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remains_quota is not None:
            result['RemainsQuota'] = self.remains_quota

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemainsQuota') is not None:
            self.remains_quota = m.get('RemainsQuota')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

