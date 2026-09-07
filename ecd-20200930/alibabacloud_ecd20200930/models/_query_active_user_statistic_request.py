# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryActiveUserStatisticRequest(DaraModel):
    def __init__(
        self,
        biz_type: int = None,
        end_time: str = None,
        office_site_id: str = None,
        period: str = None,
        start_time: str = None,
    ):
        # The business channel type code. Valid values:
        # 
        # - 1 (default): Enterprise Edition.
        # - 3: Cloud Office.
        # - 10: Standard Edition.
        # - 20: Business Edition.
        # - 30: Education Business Edition.
        # - 40: Cloud Phone isolated resources.
        # - 50: AgentBay.
        self.biz_type = biz_type
        # The end time of the query. The format is the same as StartTime. If the value is later than the current time, it is automatically truncated to the current time.
        self.end_time = end_time
        # The workspace ID. If specified, only active users of cloud desktops in this workspace are counted.
        self.office_site_id = office_site_id
        # The aggregation interval for statistics. Valid values:
        # 
        # - ONE_MINUTE: 1 minute.
        # - TWO_MINUTE: 2 minutes.
        # - FIVE_MINUTE (default): 5 minutes.
        # - ONE_HOUR: 1 hour.
        # - ONE_DAY: 1 day.
        self.period = period
        # The start time of the query. The following formats are supported:
        # 
        # - UTC format: yyyy-MM-ddTHH:mm:ssZ.
        # - Standard format: yyyy-MM-dd HH:mm:ss.
        # 
        # The value cannot be earlier than 6 months before the current time or later than EndTime.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.period is not None:
            result['Period'] = self.period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

