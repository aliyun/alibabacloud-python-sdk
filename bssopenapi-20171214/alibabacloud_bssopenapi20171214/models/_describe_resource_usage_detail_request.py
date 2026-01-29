# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResourceUsageDetailRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id: int = None,
        end_period: str = None,
        max_results: int = None,
        next_token: str = None,
        period_type: str = None,
        resource_type: str = None,
        start_period: str = None,
    ):
        # The ID of the account whose data you want to query. If you do not specify this parameter, the data of the current Alibaba Cloud account and its Resource Access Management (RAM) users is queried. To query the data of a RAM user, specify the ID of the RAM user.
        self.bill_owner_id = bill_owner_id
        # The end of the time range to query. The end is excluded from the time range. If you do not set this parameter, the end time is the current time. Specify the time in the format of yyyy-MM-dd HH:mm:ss.
        self.end_period = end_period
        # The maximum number of entries to return. Default value: 20. The maximum value is 300.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The time granularity at which usage details are queried. Valid values: MONTH, DAY, and HOUR.
        # 
        # This parameter is required.
        self.period_type = period_type
        # The type of deduction plan whose usage details are queried. Valid values: RI and SCU.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The beginning of the time range to query. The beginning is included in the time range. Specify the time in the yyyy-MM-dd HH:mm:ss format.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartPeriod') is not None:
            self.start_period = m.get('StartPeriod')

        return self

