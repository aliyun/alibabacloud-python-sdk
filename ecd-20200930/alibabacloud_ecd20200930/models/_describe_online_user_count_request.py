# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOnlineUserCountRequest(DaraModel):
    def __init__(
        self,
        biz_type: int = None,
        office_site_id: str = None,
        region_id: str = None,
        search_region_id: str = None,
    ):
        # > This parameter is for internal use only.
        self.biz_type = biz_type
        # The office site ID.
        self.office_site_id = office_site_id
        # The region ID.
        self.region_id = region_id
        # The ID of the region to search. This filters the results to show only resources from the specified region.
        self.search_region_id = search_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_region_id is not None:
            result['SearchRegionId'] = self.search_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchRegionId') is not None:
            self.search_region_id = m.get('SearchRegionId')

        return self

