# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListWebFlowRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListWebFlowRulesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.ListWebFlowRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListWebFlowRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[main_models.ListWebFlowRulesResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.result = result
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListWebFlowRulesResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListWebFlowRulesResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        burst: int = None,
        control_behavior: int = None,
        enable: bool = None,
        fallback_object: str = None,
        max_queueing_time_ms: int = None,
        metric_type: int = None,
        namespace: str = None,
        param_item: str = None,
        region_id: str = None,
        resource: str = None,
        resource_mode: int = None,
        resource_type: int = None,
        rule_id: str = None,
        stat_interval_ms: int = None,
        threshold: float = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.burst = burst
        self.control_behavior = control_behavior
        self.enable = enable
        self.fallback_object = fallback_object
        self.max_queueing_time_ms = max_queueing_time_ms
        self.metric_type = metric_type
        self.namespace = namespace
        self.param_item = param_item
        self.region_id = region_id
        self.resource = resource
        self.resource_mode = resource_mode
        self.resource_type = resource_type
        self.rule_id = rule_id
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

        if self.fallback_object is not None:
            result['FallbackObject'] = self.fallback_object

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

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

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

        if m.get('FallbackObject') is not None:
            self.fallback_object = m.get('FallbackObject')

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

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('StatIntervalMs') is not None:
            self.stat_interval_ms = m.get('StatIntervalMs')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

