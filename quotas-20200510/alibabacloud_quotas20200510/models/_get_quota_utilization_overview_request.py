# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQuotaUtilizationOverviewRequest(DaraModel):
    def __init__(
        self,
        quota_category: str = None,
    ):
        self.quota_category = quota_category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')

        return self

