# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryAppInstanceGroupReportListRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        biz_region_id: str = None,
        end_date: str = None,
        end_user_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_date: str = None,
        stat_date: str = None,
        status: List[str] = None,
    ):
        # The filter condition for the app instance group ID, which matches the exact ID. If this parameter is not specified, the results are not filtered by ID. You can call [ListAppInstanceGroup](~~ListAppInstanceGroup~~) to obtain the ID.
        self.app_instance_group_id = app_instance_group_id
        # The filter condition for the app instance group name, which supports inclusion matching. If this parameter is not specified, the results are not filtered by name.
        self.app_instance_group_name = app_instance_group_name
        # The ID of the business region to which the app instance group belongs. You can call [ListRegions](~~ListRegions~~) to obtain the ID. If this parameter is not specified, the results are not filtered by business region.
        self.biz_region_id = biz_region_id
        # The end date of the statistics. Format: `yyyyMMdd`. This parameter must be specified in pairs with `StartDate` and cannot be earlier than the start date. The string itself does not carry a time zone and is interpreted as a natural date in the Asia/Shanghai (UTC+8) time zone.
        self.end_date = end_date
        # The ID of the end user, which is used to filter app instance groups based on the current valid authorization relationship. Before the call, make sure that the user has at least one valid authorization. If no valid authorization exists, the current version does not narrow down the results based on this parameter. If this parameter is not specified, the results are not filtered by user.
        self.end_user_id = end_user_id
        # The page number to query. Specify a value starting from `1`. If this parameter is not specified, the service processes the request as the first page, but the response may return `0`.
        self.page_number = page_number
        # The number of entries per page. Default value: 200. The current operation does not have an additional upper limit for a single page.
        self.page_size = page_size
        # The region ID for OpenAPI access, which is used for request authentication and routing. To filter business data by region, use `BizRegionId`.
        self.region_id = region_id
        # The start date of the statistics. Format: `yyyyMMdd`. This parameter must be specified in pairs with `EndDate`, and the interval includes the start and end dates. The string itself does not carry a time zone and is interpreted as a natural date in the Asia/Shanghai (UTC+8) time zone.
        self.start_date = start_date
        # The statistical date for a single day. Format: `yyyyMMdd`. If this parameter is specified along with `StartDate` and `EndDate`, the results must meet both the single-day and interval conditions. The string itself does not carry a time zone and is interpreted as a natural date in the Asia/Shanghai (UTC+8) time zone.
        self.stat_date = stat_date
        # The list of app instance group statuses. Multiple values have an OR relationship. Unrecognized values do not participate in filtering. If all values are unrecognized, the results are not filtered by status.
        # 
        # Valid values:
        # 
        # - `DEPLOYING`: Deploying.
        # - `DEPLOYED`: Deployed but not published.
        # - `PUBLISHED`: Published and available to provide services based on the current configurations.
        # - `STOPPING`: Stopping.
        # - `STOPPED`: Stopped.
        # - `MAINTAINING`: Maintaining.
        # - `FAILED`: Deployment or running failed.
        # - `MAINTAIN_FAILED`: Maintenance failed.
        # - `DELETING`: Deleting.
        # - `DELETED`: Deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.stat_date is not None:
            result['StatDate'] = self.stat_date

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('StatDate') is not None:
            self.stat_date = m.get('StatDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

