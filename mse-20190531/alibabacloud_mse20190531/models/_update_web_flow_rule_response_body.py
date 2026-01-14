# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateWebFlowRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateWebFlowRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateWebFlowRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateWebFlowRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        burst: int = None,
        control_behavior: int = None,
        enable: bool = None,
        id: int = None,
        max_queueing_time_ms: int = None,
        metric_type: int = None,
        namespace: str = None,
        param_item: str = None,
        region_id: str = None,
        reource_mode: int = None,
        resource: str = None,
        stat_interval_ms: int = None,
        threshold: float = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.burst = burst
        self.control_behavior = control_behavior
        self.enable = enable
        self.id = id
        self.max_queueing_time_ms = max_queueing_time_ms
        self.metric_type = metric_type
        self.namespace = namespace
        self.param_item = param_item
        self.region_id = region_id
        self.reource_mode = reource_mode
        self.resource = resource
        self.stat_interval_ms = stat_interval_ms
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.id is not None:
            result['Id'] = self.id

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

        if self.reource_mode is not None:
            result['ReourceMode'] = self.reource_mode

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.stat_interval_ms is not None:
            result['StatIntervalMs'] = self.stat_interval_ms

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('Id') is not None:
            self.id = m.get('Id')

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

        if m.get('ReourceMode') is not None:
            self.reource_mode = m.get('ReourceMode')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('StatIntervalMs') is not None:
            self.stat_interval_ms = m.get('StatIntervalMs')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

