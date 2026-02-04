# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceQuotaRequest(DaraModel):
    def __init__(
        self,
        quota_type: str = None,
    ):
        # Quota 配额的唯一标识。
        # 
        # This parameter is required.
        self.quota_type = quota_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')

        return self

