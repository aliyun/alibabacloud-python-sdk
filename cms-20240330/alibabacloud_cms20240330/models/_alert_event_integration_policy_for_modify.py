# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AlertEventIntegrationPolicyForModify(DaraModel):
    def __init__(
        self,
        alert_event_integration_policy_name: str = None,
        description: str = None,
        filter_setting: main_models.FilterSetting = None,
        integration_setting: str = None,
        transformer_setting: List[main_models.TransformAction] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.alert_event_integration_policy_name = alert_event_integration_policy_name
        self.description = description
        self.filter_setting = filter_setting
        self.integration_setting = integration_setting
        self.transformer_setting = transformer_setting
        self.type = type

    def validate(self):
        if self.filter_setting:
            self.filter_setting.validate()
        if self.transformer_setting:
            for v1 in self.transformer_setting:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_event_integration_policy_name is not None:
            result['alertEventIntegrationPolicyName'] = self.alert_event_integration_policy_name

        if self.description is not None:
            result['description'] = self.description

        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()

        if self.integration_setting is not None:
            result['integrationSetting'] = self.integration_setting

        result['transformerSetting'] = []
        if self.transformer_setting is not None:
            for k1 in self.transformer_setting:
                result['transformerSetting'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEventIntegrationPolicyName') is not None:
            self.alert_event_integration_policy_name = m.get('alertEventIntegrationPolicyName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('integrationSetting') is not None:
            self.integration_setting = m.get('integrationSetting')

        self.transformer_setting = []
        if m.get('transformerSetting') is not None:
            for k1 in m.get('transformerSetting'):
                temp_model = main_models.TransformAction()
                self.transformer_setting.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

