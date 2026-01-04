# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEnsRegionIdResourceRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        isp: str = None,
        order_by_params: str = None,
        page_number: int = None,
        page_size: str = None,
        start_time: str = None,
    ):
        # The end time of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The Internet service provider (ISP). Valid values:
        # 
        # *   cmcc: China Mobile
        # *   telecom: China Telecom
        # *   unicom: China Unicom
        # *   multiCarrier: multi-line ISP
        self.isp = isp
        # The order in which the resources to return are sorted. Valid values:
        # 
        # *   InstanceCount: desc
        # *   Area: asc
        # *   InternetBandwidth: asc
        self.order_by_params = order_by_params
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Maximum value: **100**. Default value: **10**.
        self.page_size = page_size
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.order_by_params is not None:
            result['OrderByParams'] = self.order_by_params

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('OrderByParams') is not None:
            self.order_by_params = m.get('OrderByParams')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

