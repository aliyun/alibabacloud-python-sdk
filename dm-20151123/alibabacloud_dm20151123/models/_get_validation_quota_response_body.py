# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetValidationQuotaResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_quota: int = None,
        used_quota: int = None,
    ):
        self.request_id = request_id
        self.total_quota = total_quota
        self.used_quota = used_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota

        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')

        if m.get('UsedQuota') is not None:
            self.used_quota = m.get('UsedQuota')

        return self

