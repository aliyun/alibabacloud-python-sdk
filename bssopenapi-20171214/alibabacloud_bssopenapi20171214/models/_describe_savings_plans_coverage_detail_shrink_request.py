# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSavingsPlansCoverageDetailShrinkRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id: int = None,
        end_period: str = None,
        filter_param_shrink: str = None,
        max_results: int = None,
        period_type: str = None,
        start_period: str = None,
        token: str = None,
    ):
        # The ID of the account for which you want to query coverage details.
        self.bill_owner_id = bill_owner_id
        # The end of the time range to query. The end is excluded from the time range. If you do not set this parameter, the end time is the current time. Specify the time in the format of yyyy-MM-dd HH:mm:ss.
        self.end_period = end_period
        self.filter_param_shrink = filter_param_shrink
        # The maximum number of entries to return. Default value: 20. Maximum value: 300.
        self.max_results = max_results
        # The time granularity at which coverage details are queried. Valid values: MONTH, DAY, and HOUR.
        # 
        # This parameter is required.
        self.period_type = period_type
        # The beginning of the time range to query. The beginning is included in the time range. Specify the time in the format of yyyy-MM-dd HH:mm:ss.
        # 
        # This parameter is required.
        self.start_period = start_period
        # The token that is used to retrieve the next page of results. You do not need to set this parameter if you query coverage details within a specific time range for the first time. The response returns a token that you can use to query coverage details that are displayed on the next page. If a null value is returned for the NextToken parameter, no more coverage details can be queried.
        self.token = token

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

        if self.filter_param_shrink is not None:
            result['FilterParam'] = self.filter_param_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        if self.start_period is not None:
            result['StartPeriod'] = self.start_period

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')

        if m.get('EndPeriod') is not None:
            self.end_period = m.get('EndPeriod')

        if m.get('FilterParam') is not None:
            self.filter_param_shrink = m.get('FilterParam')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        if m.get('StartPeriod') is not None:
            self.start_period = m.get('StartPeriod')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

