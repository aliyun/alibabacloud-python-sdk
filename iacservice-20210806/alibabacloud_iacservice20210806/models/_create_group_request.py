# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class CreateGroupRequest(DaraModel):
    def __init__(
        self,
        auto_destroy: bool = None,
        auto_trigger: bool = None,
        client_token: str = None,
        description: str = None,
        forced_setting: bool = None,
        name: str = None,
        notify_config: List[main_models.CreateGroupRequestNotifyConfig] = None,
        notify_operation_types: List[str] = None,
        project_id: str = None,
        ram_role: str = None,
        report_export_field: List[str] = None,
        report_export_path: str = None,
        terraform_provider_version: str = None,
        trigger_config: List[main_models.CreateGroupRequestTriggerConfig] = None,
        trigger_resource_type: List[str] = None,
    ):
        self.auto_destroy = auto_destroy
        self.auto_trigger = auto_trigger
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.forced_setting = forced_setting
        # This parameter is required.
        self.name = name
        self.notify_config = notify_config
        self.notify_operation_types = notify_operation_types
        # This parameter is required.
        self.project_id = project_id
        self.ram_role = ram_role
        self.report_export_field = report_export_field
        self.report_export_path = report_export_path
        self.terraform_provider_version = terraform_provider_version
        self.trigger_config = trigger_config
        self.trigger_resource_type = trigger_resource_type

    def validate(self):
        if self.notify_config:
            for v1 in self.notify_config:
                 if v1:
                    v1.validate()
        if self.trigger_config:
            for v1 in self.trigger_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy

        if self.auto_trigger is not None:
            result['autoTrigger'] = self.auto_trigger

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.description is not None:
            result['description'] = self.description

        if self.forced_setting is not None:
            result['forcedSetting'] = self.forced_setting

        if self.name is not None:
            result['name'] = self.name

        result['notifyConfig'] = []
        if self.notify_config is not None:
            for k1 in self.notify_config:
                result['notifyConfig'].append(k1.to_map() if k1 else None)

        if self.notify_operation_types is not None:
            result['notifyOperationTypes'] = self.notify_operation_types

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.ram_role is not None:
            result['ramRole'] = self.ram_role

        if self.report_export_field is not None:
            result['reportExportField'] = self.report_export_field

        if self.report_export_path is not None:
            result['reportExportPath'] = self.report_export_path

        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version

        result['triggerConfig'] = []
        if self.trigger_config is not None:
            for k1 in self.trigger_config:
                result['triggerConfig'].append(k1.to_map() if k1 else None)

        if self.trigger_resource_type is not None:
            result['triggerResourceType'] = self.trigger_resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')

        if m.get('autoTrigger') is not None:
            self.auto_trigger = m.get('autoTrigger')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('forcedSetting') is not None:
            self.forced_setting = m.get('forcedSetting')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.notify_config = []
        if m.get('notifyConfig') is not None:
            for k1 in m.get('notifyConfig'):
                temp_model = main_models.CreateGroupRequestNotifyConfig()
                self.notify_config.append(temp_model.from_map(k1))

        if m.get('notifyOperationTypes') is not None:
            self.notify_operation_types = m.get('notifyOperationTypes')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')

        if m.get('reportExportField') is not None:
            self.report_export_field = m.get('reportExportField')

        if m.get('reportExportPath') is not None:
            self.report_export_path = m.get('reportExportPath')

        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')

        self.trigger_config = []
        if m.get('triggerConfig') is not None:
            for k1 in m.get('triggerConfig'):
                temp_model = main_models.CreateGroupRequestTriggerConfig()
                self.trigger_config.append(temp_model.from_map(k1))

        if m.get('triggerResourceType') is not None:
            self.trigger_resource_type = m.get('triggerResourceType')

        return self

class CreateGroupRequestTriggerConfig(DaraModel):
    def __init__(
        self,
        trigger_strategy: str = None,
        trigger_value: str = None,
    ):
        self.trigger_strategy = trigger_strategy
        self.trigger_value = trigger_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy

        if self.trigger_value is not None:
            result['triggerValue'] = self.trigger_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')

        if m.get('triggerValue') is not None:
            self.trigger_value = m.get('triggerValue')

        return self



class CreateGroupRequestNotifyConfig(DaraModel):
    def __init__(
        self,
        notify_path: str = None,
        notify_type: str = None,
    ):
        self.notify_path = notify_path
        self.notify_type = notify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notify_path is not None:
            result['notifyPath'] = self.notify_path

        if self.notify_type is not None:
            result['notifyType'] = self.notify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notifyPath') is not None:
            self.notify_path = m.get('notifyPath')

        if m.get('notifyType') is not None:
            self.notify_type = m.get('notifyType')

        return self

