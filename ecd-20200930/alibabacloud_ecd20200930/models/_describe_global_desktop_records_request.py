# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeGlobalDesktopRecordsRequest(DaraModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        desktop_name: str = None,
        desktop_type: str = None,
        end_time: str = None,
        end_user_id: str = None,
        office_site_id: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        scope: str = None,
        sort_type: str = None,
        start_time: str = None,
        sub_pay_type: str = None,
    ):
        # The cloud computer IDs. You can specify 1 to 100 office network IDs.
        self.desktop_id = desktop_id
        # The name of the cloud computer.
        self.desktop_name = desktop_name
        # The cloud computer type. You can call the [DescribeDesktopTypes](https://help.aliyun.com/document_detail/188882.html) operation to query the IDs of the specifications supported by the cloud computer.
        self.desktop_type = desktop_type
        # The end time. The interval between the start time and end time can be up to 30 days. Supported formats:
        # 
        # *   Format: YYYY-MM-DDThh:mm:ssZ.
        self.end_time = end_time
        # The end user ID.
        self.end_user_id = end_user_id
        # The office network IDs.
        self.office_site_id = office_site_id
        # The sorting field. If this parameter is not provided, results are sorted by creation time in descending order. Valid values:
        # 
        # *   uptime: indicates that the cloud computers are sorted by startup duration.
        self.order_by = order_by
        # The page number of the current page.\\
        # Default value: 1
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 1 to 100.
        self.page_size = page_size
        # The region ID.
        # 
        # *   China (Shanghai)
        # *   Singapore
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The query range. This parameter is empty by default. Optional values are:
        # 
        # *   ADVANCED: indicates that statistics such as the connection duration are queried.
        self.scope = scope
        # The sorting method. Default value: ascending. Valid value:
        # 
        # *   Asc: ascending order
        # *   Desc: descending.
        self.sort_type = sort_type
        # The start time. Supported formats:
        # 
        # *   Format: YYYY-MM-DDThh:mm:ssZ.
        self.start_time = start_time
        # The way to purchase cloud computers. Valid values:
        # 
        # *   prePaid: The monthly purchase is unlimited.
        # *   postPaid: pay-as-you-go
        # *   monthPackage: monthly duration.
        self.sub_pay_type = sub_pay_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        return self

