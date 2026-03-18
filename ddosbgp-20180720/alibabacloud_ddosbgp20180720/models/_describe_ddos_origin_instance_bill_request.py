# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDdosOriginInstanceBillRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        is_show_list: bool = None,
        start_time: int = None,
        type: str = None,
    ):
        # The end of the time range to query. The value is a timestamp. Unit: milliseconds. The time span between StartTime and EndTime cannot exceed 30 days.
        self.end_time = end_time
        # Specifies whether to display the bill details. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_show_list = is_show_list
        # The beginning of the time range to query. The value is a timestamp. Unit: milliseconds.
        self.start_time = start_time
        # The bill type. Valid values:
        # 
        # *   **flow_cn**: the bill for the clean bandwidth of elastic IP addresses (EIPs) with Anti-DDoS (Enhanced) enabled in the Chinese mainland.
        # *   **flow_ov**: the bill for the clean bandwidth of EIPs with Anti-DDoS (Enhanced) enabled outside the Chinese mainland.
        # *   **standard_assets_flow_cn**: the bill for the clean bandwidth of regular Alibaba Cloud services in the Chinese mainland.
        # *   **standard_assets_flow_ov**: the bill for the clean bandwidth of regular Alibaba Cloud services outside the Chinese mainland.
        # *   **function**: the bill for the basic fee.
        # *   **ip_count**: the bill for protected IP addresses.
        # *   **monthly_summary**: the monthly summary bill.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.is_show_list is not None:
            result['IsShowList'] = self.is_show_list

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IsShowList') is not None:
            self.is_show_list = m.get('IsShowList')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

