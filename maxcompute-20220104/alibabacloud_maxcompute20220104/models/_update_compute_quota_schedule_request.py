# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class UpdateComputeQuotaScheduleRequest(DaraModel):
    def __init__(
        self,
        body: List[main_models.UpdateComputeQuotaScheduleRequestBody] = None,
        schedule_timezone: str = None,
    ):
        # The request body parameters.
        self.body = body
        # The time zone.
        # 
        # > The default value is UTC+8.
        self.schedule_timezone = schedule_timezone

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        if self.schedule_timezone is not None:
            result['scheduleTimezone'] = self.schedule_timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.UpdateComputeQuotaScheduleRequestBody()
                self.body.append(temp_model.from_map(k1))

        if m.get('scheduleTimezone') is not None:
            self.schedule_timezone = m.get('scheduleTimezone')

        return self

class UpdateComputeQuotaScheduleRequestBody(DaraModel):
    def __init__(
        self,
        condition: main_models.UpdateComputeQuotaScheduleRequestBodyCondition = None,
        plan: str = None,
        type: str = None,
    ):
        # The condition for the plan to take effect.
        self.condition = condition
        # The name of the quota plan.
        # 
        # This parameter is required.
        self.plan = plan
        # The type.
        # 
        # >Notice: 
        # 
        # Only daily is supported.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.condition:
            self.condition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['condition'] = self.condition.to_map()

        if self.plan is not None:
            result['plan'] = self.plan

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            temp_model = main_models.UpdateComputeQuotaScheduleRequestBodyCondition()
            self.condition = temp_model.from_map(m.get('condition'))

        if m.get('plan') is not None:
            self.plan = m.get('plan')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateComputeQuotaScheduleRequestBodyCondition(DaraModel):
    def __init__(
        self,
        at: str = None,
    ):
        # The time when the plan takes effect.
        # 
        # This parameter is required.
        self.at = at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.at is not None:
            result['at'] = self.at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('at') is not None:
            self.at = m.get('at')

        return self

