# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySessionDataRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        region_id: str = None,
        stat_date: str = None,
    ):
        # The delivery group ID, used to filter session data for a specified delivery group. If not provided, the summary of session data for all delivery groups under the current account is returned.
        self.app_instance_group_id = app_instance_group_id
        # The business region ID, which specifies the region for which to query session data. The server uses this value as the region filter condition for session data. If not provided, no region filtering is applied, and the summary of session data for all regions is returned.
        self.biz_region_id = biz_region_id
        # The region ID, which is a common request parameter for the gateway. The actual region used to filter session data in this operation is specified by BizRegionId.
        self.region_id = region_id
        # The statistical date in the yyyyMMdd format (without hyphens), such as 20261106. If not provided, the data for yesterday is queried by default. Only dates within the last 90 days are supported. If the date exceeds 90 days or the format is invalid, a parameter error is returned.
        self.stat_date = stat_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stat_date is not None:
            result['StatDate'] = self.stat_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StatDate') is not None:
            self.stat_date = m.get('StatDate')

        return self

