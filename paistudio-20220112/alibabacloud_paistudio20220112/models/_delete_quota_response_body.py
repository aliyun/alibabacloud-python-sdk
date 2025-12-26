# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteQuotaResponseBody(DaraModel):
    def __init__(
        self,
        quota_id: str = None,
        request_id: str = None,
    ):
        # Quota Id
        self.quota_id = quota_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

