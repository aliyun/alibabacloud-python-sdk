# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWebFlowRuleRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        app_name: str = None,
        burst: int = None,
        control_behavior: int = None,
        enable: bool = None,
        max_queueing_time_ms: int = None,
        metric_type: int = None,
        namespace: str = None,
        param_item: str = None,
        region_id: str = None,
        resource: str = None,
        resource_mode: int = None,
        resource_type: int = None,
        stat_interval_ms: int = None,
        threshold: float = None,
    ):
        self.accept_language = accept_language
        self.app_id = app_id
        # This parameter is required.
        self.app_name = app_name
        self.burst = burst
        self.control_behavior = control_behavior
        self.enable = enable
        self.max_queueing_time_ms = max_queueing_time_ms
        self.metric_type = metric_type
        self.namespace = namespace
        self.param_item = param_item
        self.region_id = region_id
        # This parameter is required.
        self.resource = resource
        # This parameter is required.
        self.resource_mode = resource_mode
        self.resource_type = resource_type
        self.stat_interval_ms = stat_interval_ms
        # This parameter is required.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.burst is not None:
            result['Burst'] = self.burst

        if self.control_behavior is not None:
            result['ControlBehavior'] = self.control_behavior

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.max_queueing_time_ms is not None:
            result['MaxQueueingTimeMs'] = self.max_queueing_time_ms

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.param_item is not None:
            result['ParamItem'] = self.param_item

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_mode is not None:
            result['ResourceMode'] = self.resource_mode

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.stat_interval_ms is not None:
            result['StatIntervalMs'] = self.stat_interval_ms

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Burst') is not None:
            self.burst = m.get('Burst')

        if m.get('ControlBehavior') is not None:
            self.control_behavior = m.get('ControlBehavior')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('MaxQueueingTimeMs') is not None:
            self.max_queueing_time_ms = m.get('MaxQueueingTimeMs')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ParamItem') is not None:
            self.param_item = m.get('ParamItem')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceMode') is not None:
            self.resource_mode = m.get('ResourceMode')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StatIntervalMs') is not None:
            self.stat_interval_ms = m.get('StatIntervalMs')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

