# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUnionTaskRequest(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        charge_ploy: int = None,
        end_time: str = None,
        optimization_switch: int = None,
        proxy_user_id: int = None,
        quota: int = None,
        quota_day: int = None,
        start_time: str = None,
        task_id: int = None,
    ):
        self.channel_id = channel_id
        self.charge_ploy = charge_ploy
        self.end_time = end_time
        self.optimization_switch = optimization_switch
        # This parameter is required.
        self.proxy_user_id = proxy_user_id
        self.quota = quota
        self.quota_day = quota_day
        self.start_time = start_time
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.charge_ploy is not None:
            result['ChargePloy'] = self.charge_ploy

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.optimization_switch is not None:
            result['OptimizationSwitch'] = self.optimization_switch

        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.quota_day is not None:
            result['QuotaDay'] = self.quota_day

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ChargePloy') is not None:
            self.charge_ploy = m.get('ChargePloy')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OptimizationSwitch') is not None:
            self.optimization_switch = m.get('OptimizationSwitch')

        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('QuotaDay') is not None:
            self.quota_day = m.get('QuotaDay')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

