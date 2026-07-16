# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeGlobalDesktopRecordsRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        desktop_id: List[str] = None,
        desktop_name: str = None,
        desktop_status_list: List[str] = None,
        desktop_type: str = None,
        end_time: str = None,
        end_user_id: str = None,
        exclude_desktop_status_list: List[str] = None,
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
        self.business_channel = business_channel
        # The IDs of the cloud desktops. You can specify up to 100 IDs.
        self.desktop_id = desktop_id
        # The name of the cloud desktop.
        self.desktop_name = desktop_name
        # The ID of the resource group.
        self.desktop_status_list = desktop_status_list
        # The desktop type. You can call the [DescribeDesktopTypes](https://help.aliyun.com/document_detail/188882.html) operation to query the IDs of the supported desktop types.
        self.desktop_type = desktop_type
        # The end time of the query. The time must be in UTC and in the `YYYY-MM-DDThh:mm:ssZ` format. The interval between the start and end times cannot exceed 30 days.
        # 
        # - Format: YYYY-MM-DDThh:mm:ssZ.
        self.end_time = end_time
        # The ID of the end user.
        # 
        # - Asc: ascending order
        # 
        # - Desc: descending order
        self.end_user_id = end_user_id
        self.exclude_desktop_status_list = exclude_desktop_status_list
        # The ID of the office site.
        # 
        # - China (Shanghai)
        # 
        # - Singapore
        self.office_site_id = office_site_id
        # The field by which to sort the results. If you do not specify this parameter, the results are sorted by creation time in descending order. Valid value:
        # 
        # - `uptime`: Sorts the results by cloud desktop uptime.
        self.order_by = order_by
        # The page number to return.<br>Default value: 1.<br>
        # 
        # - Format: YYYY-MM-DDThh:mm:ssZ.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size
        # The ID of the region.
        # 
        # - Shanghai
        # 
        # - Singapore
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The query scope. This parameter is empty by default. Valid value:
        # 
        # - `ADVANCED`: Queries statistical records, such as connection duration.
        # 
        # - postPaid: Pay-as-you-go.
        # 
        # - monthPackage: monthly time-based package.
        self.scope = scope
        # The sort order. The default is `Asc`. Valid values:
        # 
        # - `Asc`: ascending order
        self.sort_type = sort_type
        # The start time of the query. The time must be in UTC and in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.start_time = start_time
        # The billing method of the cloud desktop. Valid values:
        self.sub_pay_type = sub_pay_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_status_list is not None:
            result['DesktopStatusList'] = self.desktop_status_list

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.exclude_desktop_status_list is not None:
            result['ExcludeDesktopStatusList'] = self.exclude_desktop_status_list

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
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopStatusList') is not None:
            self.desktop_status_list = m.get('DesktopStatusList')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('ExcludeDesktopStatusList') is not None:
            self.exclude_desktop_status_list = m.get('ExcludeDesktopStatusList')

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

