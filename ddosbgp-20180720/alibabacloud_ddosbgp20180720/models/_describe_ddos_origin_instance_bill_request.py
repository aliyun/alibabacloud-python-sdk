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
        # The end timestamp of the query. Unit: milliseconds. The time span cannot exceed 30 days.
        self.end_time = end_time
        # Specifies whether to display billing details. Valid values:
        # - **true**: Displays billing information.
        # - **false**: Displays only global instance information without billing details.
        self.is_show_list = is_show_list
        # The start timestamp of the query. Unit: milliseconds.
        self.start_time = start_time
        # The bill type. Valid values:
        # - **flow_cn**: clean traffic bill for EIPs with Anti-DDoS (Enhanced) enabled in the Chinese mainland.
        # - **flow_ov**: clean traffic bill for EIPs with Anti-DDoS (Enhanced) enabled outside the Chinese mainland.
        # - **standard_assets_flow_cn**: clean traffic bill for Regular Alibaba Cloud services in the Chinese mainland.
        # - **standard_assets_flow_ov**: clean traffic bill for Regular Alibaba Cloud services outside the Chinese mainland.
        # - **function**: feature activation bill.
        # - **ip_count**: protected IP address count bill.
        # - **monthly_summary**: monthly summary bill.
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

