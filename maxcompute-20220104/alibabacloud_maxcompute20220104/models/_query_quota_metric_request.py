# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryQuotaMetricRequest(DaraModel):
    def __init__(
        self,
        interval: int = None,
        nickname: str = None,
        sub_metric: str = None,
        sub_quota_nickname: str = None,
        end_time: int = None,
        start_time: int = None,
        strategy: str = None,
    ):
        # The fixed interval in seconds. By default, this parameter is empty, which indicates that the adaptive interval policy of the system is used.
        # - Adaptive interval policy: The interval is 60 seconds if the query time range is within 6 hours, 300 seconds if within 24 hours, 900 seconds if within 72 hours, and 1800 seconds if exceeding 72 hours.
        # - Specified interval: Only 60, 300, and 900 are supported. The query time range must be within 72 hours.
        self.interval = interval
        # The nickname of the level-1 quota. This parameter is required.
        self.nickname = nickname
        self.sub_metric = sub_metric
        # The nickname of the level-2 quota.
        self.sub_quota_nickname = sub_quota_nickname
        # The end time of the query time range. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The start time of the query time range. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The data aggregation policy. Default value: max. Valid values: max and avg.
        # 
        # Data is collected every 1 minute. If the query time range is large, the adaptive step size for data display exceeds 1 minute, and the metrics are aggregated. This parameter specifies the data aggregation logic.
        self.strategy = strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interval is not None:
            result['interval'] = self.interval

        if self.nickname is not None:
            result['nickname'] = self.nickname

        if self.sub_metric is not None:
            result['subMetric'] = self.sub_metric

        if self.sub_quota_nickname is not None:
            result['subQuotaNickname'] = self.sub_quota_nickname

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.strategy is not None:
            result['strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('interval') is not None:
            self.interval = m.get('interval')

        if m.get('nickname') is not None:
            self.nickname = m.get('nickname')

        if m.get('subMetric') is not None:
            self.sub_metric = m.get('subMetric')

        if m.get('subQuotaNickname') is not None:
            self.sub_quota_nickname = m.get('subQuotaNickname')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')

        return self

