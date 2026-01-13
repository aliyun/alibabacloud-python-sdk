# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ServiceConfigResult(DaraModel):
    def __init__(
        self,
        poi_search_total_quota: str = None,
        poi_search_used_quota: str = None,
        search_total_quota: str = None,
        search_used_quota: str = None,
        status: str = None,
    ):
        self.poi_search_total_quota = poi_search_total_quota
        self.poi_search_used_quota = poi_search_used_quota
        self.search_total_quota = search_total_quota
        self.search_used_quota = search_used_quota
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.poi_search_total_quota is not None:
            result['poiSearchTotalQuota'] = self.poi_search_total_quota

        if self.poi_search_used_quota is not None:
            result['poiSearchUsedQuota'] = self.poi_search_used_quota

        if self.search_total_quota is not None:
            result['searchTotalQuota'] = self.search_total_quota

        if self.search_used_quota is not None:
            result['searchUsedQuota'] = self.search_used_quota

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('poiSearchTotalQuota') is not None:
            self.poi_search_total_quota = m.get('poiSearchTotalQuota')

        if m.get('poiSearchUsedQuota') is not None:
            self.poi_search_used_quota = m.get('poiSearchUsedQuota')

        if m.get('searchTotalQuota') is not None:
            self.search_total_quota = m.get('searchTotalQuota')

        if m.get('searchUsedQuota') is not None:
            self.search_used_quota = m.get('searchUsedQuota')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

