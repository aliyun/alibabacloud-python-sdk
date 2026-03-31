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
        self.interval = interval
        self.nickname = nickname
        self.sub_metric = sub_metric
        self.sub_quota_nickname = sub_quota_nickname
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.start_time = start_time
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

