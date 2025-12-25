# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AlertEventIntegrationPolicyForView(DaraModel):
    def __init__(
        self,
        alert_event_integration_policy_id: str = None,
        alert_event_integration_policy_name: str = None,
        create_time: str = None,
        description: str = None,
        enable: bool = None,
        filter_setting: main_models.FilterSetting = None,
        integration_setting: str = None,
        token: str = None,
        transformer_setting: List[main_models.TransformAction] = None,
        type: str = None,
        update_time: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        self.alert_event_integration_policy_id = alert_event_integration_policy_id
        # This parameter is required.
        self.alert_event_integration_policy_name = alert_event_integration_policy_name
        self.create_time = create_time
        self.description = description
        self.enable = enable
        self.filter_setting = filter_setting
        self.integration_setting = integration_setting
        self.token = token
        self.transformer_setting = transformer_setting
        self.type = type
        self.update_time = update_time
        self.user_id = user_id
        self.workspace = workspace

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
        if self.alert_event_integration_policy_id is not None:
            result['alertEventIntegrationPolicyId'] = self.alert_event_integration_policy_id

        if self.alert_event_integration_policy_name is not None:
            result['alertEventIntegrationPolicyName'] = self.alert_event_integration_policy_name

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.enable is not None:
            result['enable'] = self.enable

        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()

        if self.integration_setting is not None:
            result['integrationSetting'] = self.integration_setting

        if self.token is not None:
            result['token'] = self.token

        result['transformerSetting'] = []
        if self.transformer_setting is not None:
            for k1 in self.transformer_setting:
                result['transformerSetting'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEventIntegrationPolicyId') is not None:
            self.alert_event_integration_policy_id = m.get('alertEventIntegrationPolicyId')

        if m.get('alertEventIntegrationPolicyName') is not None:
            self.alert_event_integration_policy_name = m.get('alertEventIntegrationPolicyName')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('integrationSetting') is not None:
            self.integration_setting = m.get('integrationSetting')

        if m.get('token') is not None:
            self.token = m.get('token')

        self.transformer_setting = []
        if m.get('transformerSetting') is not None:
            for k1 in m.get('transformerSetting'):
                temp_model = main_models.TransformAction()
                self.transformer_setting.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

