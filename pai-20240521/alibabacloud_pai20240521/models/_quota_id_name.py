# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuotaIdName(DaraModel):
    def __init__(
        self,
        quota_id: str = None,
        quota_name: str = None,
    ):
        self.quota_id = quota_id
        self.quota_name = quota_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        return self

