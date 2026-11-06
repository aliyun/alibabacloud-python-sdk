# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryConnectionReportRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        end_date: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        start_date: str = None,
    ):
        # The ID of the app instance group, which is used to filter data for a specified app instance group. You can call [ListAppInstanceGroup](~~ListAppInstanceGroup~~) to obtain the ID. If you do not specify this parameter, data is not filtered by app instance group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the business region, which is used to filter report data. You can call [ListRegions](~~ListRegions~~) to obtain the ID.
        self.biz_region_id = biz_region_id
        # The end time of the statistics. **Required**. Format: `yyyy-MM-dd HH:mm:ss`. The value cannot be earlier than `StartDate`. The statistical interval includes the start time but excludes the end time. The time span cannot exceed 60 months. The string itself does not carry a time zone and is interpreted in the Asia/Shanghai (UTC+8) time zone.
        self.end_date = end_date
        # The page number to query. We recommend that you explicitly specify a value starting from `1`. If you do not specify this parameter, the service processes the request as the first page, but the response may echo `0`.
        self.page_number = page_number
        # The number of entries per page. Default value: 200. If the value exceeds 1,500, it is processed as 1,500.
        self.page_size = page_size
        # The product type. **Required**.
        # 
        # Valid values:
        # 
        # - `CloudApp`: Wuying cloud app.
        # - `CloudBrowser`: Cloud browser.
        # - `WuyingServer`: Enterprise edition workstation.
        # - `WuyingWorkstation`: Personal edition Linggou container workstation.
        # - `WuyingWorkstationTeam`: Team edition Linggou container workstation.
        # - `WuyingWorkstationBusiness`: Dedicated edition Linggou container workstation.
        # - `AndroidCloud`: Cloud phone.
        # - `AIAgent`: AgentBay (AI agent).
        self.product_type = product_type
        # The start time of the statistics. **Required**. Format: `yyyy-MM-dd HH:mm:ss`. The statistical interval includes the start time but excludes the end time. The time span cannot exceed 60 months. The string itself does not carry a time zone and is interpreted in the Asia/Shanghai (UTC+8) time zone.
        self.start_date = start_date

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

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

        return self

