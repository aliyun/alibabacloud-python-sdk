# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUserUsageReportRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        connection_status: str = None,
        end_date: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        start_date: str = None,
        user_id: str = None,
    ):
        # The ID of the app instance group. This parameter is used to filter data for a specified app instance group. You can call the [ListAppInstanceGroup](~~ListAppInstanceGroup~~) operation to obtain the ID. If you do not specify this parameter, data is not filtered by app instance group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the business region. This parameter is used to filter report data. You can call the [ListRegions](~~ListRegions~~) operation to obtain the ID.
        self.biz_region_id = biz_region_id
        # The filter condition for the user connection status. The value is not case-sensitive. An unrecognized value is equivalent to not filtering by connection status.
        # 
        # Valid values:
        # 
        # - `Connected`: At least one currently connected session exists.
        # - `Disconnected`: The session binding is retained, but no currently connected session exists.
        # - `Unbound`: No session binding exists.
        self.connection_status = connection_status
        # The end time of the statistics. **Required**. Format: `yyyy-MM-dd HH:mm:ss`. The end time cannot be earlier than StartDate. The service converts the time to `yyyyMMdd` and calculates the statistics by natural days in a closed interval. The hours, minutes, and seconds are not involved in the day-level filtering. The time span cannot exceed 60 months. The string itself does not carry a time zone and is interpreted as Asia/Shanghai (UTC+8).
        self.end_date = end_date
        # The page number to query. Specify a value starting from 1. If you do not specify this parameter, the service processes the request as the first page, but the response may return 0.
        self.page_number = page_number
        # The number of entries per page. Default value: 200. If the value is greater than 1,500, it is processed as 1,500.
        self.page_size = page_size
        # The product type. **Required**.
        # 
        # Valid values:
        # 
        # - `CloudApp`: WUYING Cloud App.
        # - `CloudBrowser`: Cloud Browser.
        # - `WuyingServer`: Enterprise Edition workstation.
        # - `WuyingWorkstation`: Personal Edition Linggou container workstation.
        # - `WuyingWorkstationTeam`: Team Edition Linggou container workstation.
        # - `WuyingWorkstationBusiness`: Dedicated Edition Linggou container workstation.
        # - `AndroidCloud`: Cloud Phone.
        # - `AIAgent`: AgentBay (AI agent).
        self.product_type = product_type
        # The start time of the statistics. **Required**. Format: `yyyy-MM-dd HH:mm:ss`. The service converts the time to `yyyyMMdd` and calculates the statistics by natural days in a closed interval. The hours, minutes, and seconds are not involved in the day-level filtering. The time span cannot exceed 60 months. The string itself does not carry a time zone and is interpreted as Asia/Shanghai (UTC+8).
        self.start_date = start_date
        # The ID of the end user. This parameter is used to accurately filter users. If you do not specify this parameter, data is not filtered by user.
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

        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

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

        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

