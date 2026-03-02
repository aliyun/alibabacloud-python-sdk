# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MonitorSlsAlertRule(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        query_condition: str = None,
        trigger_interval: int = None,
        trigger_interval_unit: str = None,
        trigger_operator: str = None,
        trigger_threshold: int = None,
        trigger_threshold_upper: int = None,
    ):
        self.id = id
        self.name = name
        self.query_condition = query_condition
        self.trigger_interval = trigger_interval
        self.trigger_interval_unit = trigger_interval_unit
        self.trigger_operator = trigger_operator
        self.trigger_threshold = trigger_threshold
        self.trigger_threshold_upper = trigger_threshold_upper

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.query_condition is not None:
            result['queryCondition'] = self.query_condition

        if self.trigger_interval is not None:
            result['triggerInterval'] = self.trigger_interval

        if self.trigger_interval_unit is not None:
            result['triggerIntervalUnit'] = self.trigger_interval_unit

        if self.trigger_operator is not None:
            result['triggerOperator'] = self.trigger_operator

        if self.trigger_threshold is not None:
            result['triggerThreshold'] = self.trigger_threshold

        if self.trigger_threshold_upper is not None:
            result['triggerThresholdUpper'] = self.trigger_threshold_upper

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('queryCondition') is not None:
            self.query_condition = m.get('queryCondition')

        if m.get('triggerInterval') is not None:
            self.trigger_interval = m.get('triggerInterval')

        if m.get('triggerIntervalUnit') is not None:
            self.trigger_interval_unit = m.get('triggerIntervalUnit')

        if m.get('triggerOperator') is not None:
            self.trigger_operator = m.get('triggerOperator')

        if m.get('triggerThreshold') is not None:
            self.trigger_threshold = m.get('triggerThreshold')

        if m.get('triggerThresholdUpper') is not None:
            self.trigger_threshold_upper = m.get('triggerThresholdUpper')

        return self

