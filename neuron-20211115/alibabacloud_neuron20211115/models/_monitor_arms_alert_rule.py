# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MonitorArmsAlertRule(DaraModel):
    def __init__(
        self,
        id: int = None,
        metric_key: str = None,
        metric_type: str = None,
        name: str = None,
        trigger_aggregate: str = None,
        trigger_interval: int = None,
        trigger_operator: str = None,
        trigger_threshold: int = None,
    ):
        self.id = id
        self.metric_key = metric_key
        self.metric_type = metric_type
        self.name = name
        self.trigger_aggregate = trigger_aggregate
        self.trigger_interval = trigger_interval
        self.trigger_operator = trigger_operator
        self.trigger_threshold = trigger_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.metric_key is not None:
            result['metricKey'] = self.metric_key

        if self.metric_type is not None:
            result['metricType'] = self.metric_type

        if self.name is not None:
            result['name'] = self.name

        if self.trigger_aggregate is not None:
            result['triggerAggregate'] = self.trigger_aggregate

        if self.trigger_interval is not None:
            result['triggerInterval'] = self.trigger_interval

        if self.trigger_operator is not None:
            result['triggerOperator'] = self.trigger_operator

        if self.trigger_threshold is not None:
            result['triggerThreshold'] = self.trigger_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('metricKey') is not None:
            self.metric_key = m.get('metricKey')

        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('triggerAggregate') is not None:
            self.trigger_aggregate = m.get('triggerAggregate')

        if m.get('triggerInterval') is not None:
            self.trigger_interval = m.get('triggerInterval')

        if m.get('triggerOperator') is not None:
            self.trigger_operator = m.get('triggerOperator')

        if m.get('triggerThreshold') is not None:
            self.trigger_threshold = m.get('triggerThreshold')

        return self

