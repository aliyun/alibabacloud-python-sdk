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
        # The ID of the account whose data you want to query. If you do not specify this parameter, the data of the current account and its linked accounts is queried. To query the data of a linked account, specify the ID of the linked account. You can specify only one account ID.
        self.bill_owner_id = bill_owner_id
        # The end of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format. The specified time is excluded from the time range. If you do not specify this parameter, this parameter is set to the current time.
        self.end_period = end_period
        # The time granularity at which the data is queried. Valid values: MONTH, DAY, and HOUR.
        # 
        # This parameter is required.
        self.period_type = period_type
        # The type of the resource plan. Valid values: RI and SCU.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The beginning of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format. The specified time is included in the time range.
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

