# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResourceUsageTotalRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id: int = None,
        end_period: str = None,
        period_type: str = None,
        resource_type: str = None,
        start_period: str = None,
    ):
        # The ID of the resource ownership account. The resource ownership account is the account that actually uses the resource. Only one account ID can be specified.
        self.bill_owner_id = bill_owner_id
        # The end time. Format: yyyy-MM-dd HH:mm:ss. The query excludes data at this time. If this parameter is left empty, the query range extends to the current time. This value specifies the end time of the query range.
        self.end_period = end_period
        # The time granularity. Valid values:
        # 
        # - MONTH: month
        # - DAY: day
        # - HOUR: hour
        # 
        # This parameter is required.
        self.period_type = period_type
        # The resource plan type. Valid values:
        # 
        # - RI: reserved instance.
        # - SCU: storage capacity unit.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The start time. Format: yyyy-MM-dd HH:mm:ss. The query includes data at this time. This value specifies the start time of the query range.
        # 
        # This parameter is required.
        self.start_period = start_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id

        if self.end_period is not None:
            result['EndPeriod'] = self.end_period

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_period is not None:
            result['StartPeriod'] = self.start_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')

        if m.get('EndPeriod') is not None:
            self.end_period = m.get('EndPeriod')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartPeriod') is not None:
            self.start_period = m.get('StartPeriod')

        return self

