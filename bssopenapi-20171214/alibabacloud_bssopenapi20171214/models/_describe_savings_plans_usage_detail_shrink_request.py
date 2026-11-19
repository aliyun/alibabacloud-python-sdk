# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSavingsPlansUsageDetailShrinkRequest(DaraModel):
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
        # The ID of the account whose data you want to query. If this parameter is left empty, the data of the current account and its trusteeship linked accounts is queried. You can specify the ID of a trusteeship linked account to query only the data of that account.
        self.bill_owner_id = bill_owner_id
        # The end time of the query. Format: yyyy-MM-dd HH:mm:ss. The specified time is excluded from the query. If this parameter is left empty, the current time is used.
        self.end_period = end_period
        # The filter parameters.
        self.filter_param_shrink = filter_param_shrink
        # The maximum number of data records to return in the current request. Default value: 20. Maximum value: 300.
        self.max_results = max_results
        # The time granularity for querying the usage summary. Valid values:
        # - MONTH: monthly
        # - DAY: daily
        # - HOUR: hourly
        # 
        # This parameter is required.
        self.period_type = period_type
        # The start time of the query. Format: yyyy-MM-dd HH:mm:ss. The specified time is included in the query.
        # 
        # This parameter is required.
        self.start_period = start_period
        # The pagination token. Leave this parameter empty when you query the first page. The token for the next page is returned in the response. If the returned token is empty, all results are returned.
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

