# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnUserSecDropRequest(DaraModel):
    def __init__(
        self,
        data: str = None,
        metric: str = None,
        sec_func: str = None,
    ):
        # The date or month that you want to query.
        # 
        # *   If data is collected every day, set Data in the format of yyyymmdd, such as 20201203.
        # *   If data is collected every month, set Data in the format of yyyymm, such as 202012.
        # 
        # This parameter is required.
        self.data = data
        # The time interval at which data is collected.
        # 
        # *   If data is collected every day, the number of blocked packets on the specified day is calculated.
        # *   If data is collected every month, the number of blocked packets in the specified month is calculated.
        # 
        # This parameter is required.
        self.metric = metric
        # The security feature. Valid values:
        # 
        # *   waf: WAF
        # *   tmd: rate limiting
        # *   robot: bot traffic recognition
        # *   l4_dm_drop: domain name blocking at Layer 4
        # 
        # This parameter is required.
        self.sec_func = sec_func

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.sec_func is not None:
            result['SecFunc'] = self.sec_func

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('SecFunc') is not None:
            self.sec_func = m.get('SecFunc')

        return self

