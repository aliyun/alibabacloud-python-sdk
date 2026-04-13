# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListDetectConfigsResponseBody(DaraModel):
    def __init__(
        self,
        detect_configs: List[main_models.ListDetectConfigsResponseBodyDetectConfigs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.detect_configs = detect_configs
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.detect_configs:
            for v1 in self.detect_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['detectConfigs'] = []
        if self.detect_configs is not None:
            for k1 in self.detect_configs:
                result['detectConfigs'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detect_configs = []
        if m.get('detectConfigs') is not None:
            for k1 in m.get('detectConfigs'):
                temp_model = main_models.ListDetectConfigsResponseBodyDetectConfigs()
                self.detect_configs.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListDetectConfigsResponseBodyDetectConfigs(DaraModel):
    def __init__(
        self,
        alarm_configs: List[main_models.ListDetectConfigsResponseBodyDetectConfigsAlarmConfigs] = None,
        create_time: str = None,
        cron_expression: str = None,
        description: str = None,
        detect_config_id: str = None,
        detect_config_name: str = None,
        enabled: bool = None,
        trigger_type: str = None,
    ):
        self.alarm_configs = alarm_configs
        self.create_time = create_time
        self.cron_expression = cron_expression
        self.description = description
        self.detect_config_id = detect_config_id
        self.detect_config_name = detect_config_name
        self.enabled = enabled
        self.trigger_type = trigger_type

    def validate(self):
        if self.alarm_configs:
            for v1 in self.alarm_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['alarmConfigs'] = []
        if self.alarm_configs is not None:
            for k1 in self.alarm_configs:
                result['alarmConfigs'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression

        if self.description is not None:
            result['description'] = self.description

        if self.detect_config_id is not None:
            result['detectConfigId'] = self.detect_config_id

        if self.detect_config_name is not None:
            result['detectConfigName'] = self.detect_config_name

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_configs = []
        if m.get('alarmConfigs') is not None:
            for k1 in m.get('alarmConfigs'):
                temp_model = main_models.ListDetectConfigsResponseBodyDetectConfigsAlarmConfigs()
                self.alarm_configs.append(temp_model.from_map(k1))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('detectConfigId') is not None:
            self.detect_config_id = m.get('detectConfigId')

        if m.get('detectConfigName') is not None:
            self.detect_config_name = m.get('detectConfigName')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

class ListDetectConfigsResponseBodyDetectConfigsAlarmConfigs(DaraModel):
    def __init__(
        self,
        address: str = None,
        type: str = None,
    ):
        self.address = address
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

