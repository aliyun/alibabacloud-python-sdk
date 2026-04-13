# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class UpdateDetectConfigRequest(DaraModel):
    def __init__(
        self,
        alarm_configs: List[main_models.UpdateDetectConfigRequestAlarmConfigs] = None,
        client_token: str = None,
        cron_expression: str = None,
        description: str = None,
        detect_config_name: str = None,
        enabled: bool = None,
        trigger_type: str = None,
    ):
        self.alarm_configs = alarm_configs
        self.client_token = client_token
        self.cron_expression = cron_expression
        self.description = description
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

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression

        if self.description is not None:
            result['description'] = self.description

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
                temp_model = main_models.UpdateDetectConfigRequestAlarmConfigs()
                self.alarm_configs.append(temp_model.from_map(k1))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('detectConfigName') is not None:
            self.detect_config_name = m.get('detectConfigName')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

class UpdateDetectConfigRequestAlarmConfigs(DaraModel):
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

