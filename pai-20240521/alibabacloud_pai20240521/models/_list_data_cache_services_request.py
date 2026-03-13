# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataCacheServicesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        quota_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.quota_id = quota_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        return self

