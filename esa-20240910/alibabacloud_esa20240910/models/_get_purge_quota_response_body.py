# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPurgeQuotaResponseBody(DaraModel):
    def __init__(
        self,
        quota: str = None,
        request_id: str = None,
        usage: str = None,
    ):
        # The total quota.
        self.quota = quota
        # The request ID.
        self.request_id = request_id
        # The quota usage.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota is not None:
            result['Quota'] = self.quota

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

