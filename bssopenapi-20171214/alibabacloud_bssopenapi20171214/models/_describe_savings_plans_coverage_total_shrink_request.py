# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSavingsPlansCoverageTotalShrinkRequest(DaraModel):
    def __init__(
        self,
        bill_owner_id: int = None,
        end_period: str = None,
        filter_param_shrink: str = None,
        period_type: str = None,
        start_period: str = None,
    ):
        # The ID of the resource ownership account. The resource ownership account is the account that actually uses the resource.
        self.bill_owner_id = bill_owner_id
        # Format: yyyy-MM-dd HH:mm:ss. The query excludes this time. If this parameter is left empty, the query covers data up to the current time.
        self.end_period = end_period
        self.filter_param_shrink = filter_param_shrink
        # Valid values:
        # - MONTH: month granularity.
        # - DAY: day granularity.
        # - HOUR: hour granularity.
        # 
        # This parameter is required.
        self.period_type = period_type
        # Format: yyyy-MM-dd HH:mm:ss. The query includes this time.
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

        if self.filter_param_shrink is not None:
            result['FilterParam'] = self.filter_param_shrink

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        if self.start_period is not None:
            result['StartPeriod'] = self.start_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')

        if m.get('EndPeriod') is not None:
            self.end_period = m.get('EndPeriod')

        if m.get('FilterParam') is not None:
            self.filter_param_shrink = m.get('FilterParam')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        if m.get('StartPeriod') is not None:
            self.start_period = m.get('StartPeriod')

        return self

