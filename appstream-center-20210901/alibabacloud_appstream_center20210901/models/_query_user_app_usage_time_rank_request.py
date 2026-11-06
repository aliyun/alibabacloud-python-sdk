# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUserAppUsageTimeRankRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        end_date: str = None,
        region_id: str = None,
        start_date: str = None,
        user_id: str = None,
    ):
        # The app instance group ID, which is used to filter data for a specified app instance group. If this parameter is not provided, data is not filtered by app instance group.
        self.app_instance_group_id = app_instance_group_id
        # The business region ID, which is used to filter application usage data. If this parameter is not provided, data is not filtered by business region. You can call the [ListRegions](~~ListRegions~~) operation to obtain the ID.
        self.biz_region_id = biz_region_id
        # The end date of the statistical period, in `yyyyMMdd` format. If this parameter is not provided, it defaults to yesterday. The date cannot be earlier than `StartDate`, and cannot be earlier than 90 days before the call date. The query range includes this date. The date is interpreted as a calendar date in the Asia/Shanghai (UTC+8) time zone.
        self.end_date = end_date
        # The region ID for OpenAPI access, which is used for request authentication and routing. To filter business data by region, use `BizRegionId`.
        self.region_id = region_id
        # The start date of the statistical period, in `yyyyMMdd` format. If this parameter is not provided, it defaults to yesterday. The date cannot be earlier than 90 days before the call date. The query range includes this date. The date is interpreted as a calendar date in the Asia/Shanghai (UTC+8) time zone.
        self.start_date = start_date
        # The ID of the end user to be queried. This parameter must be explicitly provided. If it is not provided, no matching records are usually returned.
        self.user_id = user_id

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

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

