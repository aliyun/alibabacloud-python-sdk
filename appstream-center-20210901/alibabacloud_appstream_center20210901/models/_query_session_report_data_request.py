# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySessionReportDataRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        end_date: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        start_date: str = None,
        stat_date_type: str = None,
    ):
        # The ID of the app instance group, which is used to filter data for a specified app instance group. You can call the [ListAppInstanceGroup](~~ListAppInstanceGroup~~) operation to obtain the ID. If you do not specify this parameter, data is not filtered by app instance group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the business region, which is used to filter report data. You can call the [ListRegions](~~ListRegions~~) operation to obtain the ID.
        self.biz_region_id = biz_region_id
        # The end time of the statistics. This parameter is required. Format: `yyyy-MM-dd HH:mm:ss`. The end time cannot be earlier than `StartDate`. The query span must meet the limit corresponding to `StatDateType`. The string itself does not carry a time zone and is interpreted in the Asia/Shanghai (UTC+8) time zone.
        self.end_date = end_date
        # The page number of the page to query. Specify this parameter starting from `1`. If you do not specify this parameter, the first page is queried, but the response may return `0`.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 200. If the specified value is greater than 1500, 1500 is used.
        self.page_size = page_size
        # The product type. This parameter is optional. If you do not specify this parameter, data is queried based on the Wuying Cloud App caliber.
        # 
        # Specify the value in the exact case shown below. Data that does not match the specified value is not returned.
        # 
        # Valid values:
        # 
        # - `CloudApp`: Wuying Cloud App.
        # - `CloudBrowser`: Cloud Browser.
        # - `WuyingServer`: Enterprise Edition workstation.
        # - `WuyingWorkstation`: Personal Edition Linggou container workstation.
        # - `WuyingWorkstationTeam`: Team Edition Linggou container workstation.
        # - `WuyingWorkstationBusiness`: Dedicated Edition Linggou container workstation.
        # - `AndroidCloud`: Cloud Phone.
        # - `AIAgent`: AgentBay (AI agent).
        self.product_type = product_type
        # The start time of the statistics. This parameter is required. Format: `yyyy-MM-dd HH:mm:ss`. The `1d` granularity aggregates data by date, while other granularities aggregate data down to the minute. The query includes both the start and end boundaries. The string itself does not carry a time zone and is interpreted in the Asia/Shanghai (UTC+8) time zone.
        self.start_date = start_date
        # The statistical granularity. This parameter is required.
        # 
        # Valid values:
        # 
        # - `1m`: aggregates data by 1 minute. The maximum query span is 1 day.
        # - `30m`: aggregates data by 30 minutes. The maximum query span is 1 day.
        # - `6h`: aggregates data by 6 hours. The maximum query span is 15 days.
        # - `1d`: aggregates data by day. The maximum query span is 180 days.
        self.stat_date_type = stat_date_type

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

        if self.stat_date_type is not None:
            result['StatDateType'] = self.stat_date_type

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

        if m.get('StatDateType') is not None:
            self.stat_date_type = m.get('StatDateType')

        return self

