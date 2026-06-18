# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPurgeQuotaResponseBody(DaraModel):
    def __init__(
        self,
        quota: str = None,
        quota_30day: str = None,
        request_id: str = None,
        usage: str = None,
        usage_30day: str = None,
    ):
        # The total quota.
        self.quota = quota
        # The total quota available in a 30-day period. A value of 0 indicates that this quota is not configured.
        self.quota_30day = quota_30day
        # The request ID.
        self.request_id = request_id
        # The used quota.
        self.usage = usage
        # The quota used within the 30-day period.
        self.usage_30day = usage_30day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota is not None:
            result['Quota'] = self.quota

        if self.quota_30day is not None:
            result['Quota30Day'] = self.quota_30day

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.usage is not None:
            result['Usage'] = self.usage

        if self.usage_30day is not None:
            result['Usage30Day'] = self.usage_30day

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('Quota30Day') is not None:
            self.quota_30day = m.get('Quota30Day')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        if m.get('Usage30Day') is not None:
            self.usage_30day = m.get('Usage30Day')

        return self

