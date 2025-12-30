# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIspFlushCacheRemainQuotaResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        telecom_remain_quota: int = None,
    ):
        self.request_id = request_id
        self.telecom_remain_quota = telecom_remain_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.telecom_remain_quota is not None:
            result['TelecomRemainQuota'] = self.telecom_remain_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TelecomRemainQuota') is not None:
            self.telecom_remain_quota = m.get('TelecomRemainQuota')

        return self

