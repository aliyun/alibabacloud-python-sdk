# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHoneyPotSuspStatisticsRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        lang: str = None,
        statistics_days: int = None,
        statistics_key_type: str = None,
    ):
        # The source of the request. Set the value to **honeypot**.
        # 
        # This parameter is required.
        self.from_ = from_
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        self.lang = lang
        # The time range of the data to query. Unit: days.
        # 
        # This parameter is required.
        self.statistics_days = statistics_days
        # The type of the asset to query. Valid values:
        # 
        # *   **vpcInstanceId**: VPC
        # *   **uuid**: server
        # 
        # This parameter is required.
        self.statistics_key_type = statistics_key_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.statistics_days is not None:
            result['StatisticsDays'] = self.statistics_days

        if self.statistics_key_type is not None:
            result['StatisticsKeyType'] = self.statistics_key_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('StatisticsDays') is not None:
            self.statistics_days = m.get('StatisticsDays')

        if m.get('StatisticsKeyType') is not None:
            self.statistics_key_type = m.get('StatisticsKeyType')

        return self

