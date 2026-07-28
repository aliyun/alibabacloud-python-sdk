# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetGroupResponseBody(DaraModel):
    def __init__(
        self,
        group: main_models.GetGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        # The group.
        self.group = group
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['group'] = self.group.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            temp_model = main_models.GetGroupResponseBodyGroup()
            self.group = temp_model.from_map(m.get('group'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGroupResponseBodyGroup(DaraModel):
    def __init__(
        self,
        auto_destroy: bool = None,
        auto_trigger: bool = None,
        create_time: str = None,
        description: str = None,
        forced_setting: bool = None,
        group_id: str = None,
        name: str = None,
        notify_config: List[main_models.GetGroupResponseBodyGroupNotifyConfig] = None,
        notify_operation_types: List[str] = None,
        project_id: str = None,
        ram_role: str = None,
        report_export_field: List[str] = None,
        report_export_path: str = None,
        task_cnt: int = None,
        terraform_provider_version: str = None,
        trigger_config: List[main_models.GetGroupResponseBodyGroupTriggerConfig] = None,
        trigger_resource_type: List[str] = None,
    ):
        # Indicates whether automatic deletion is enabled.
        self.auto_destroy = auto_destroy
        # Indicates whether automatic triggering is enabled.
        self.auto_trigger = auto_trigger
        # The creation time.
        self.create_time = create_time
        # The group description.
        self.description = description
        # Indicates whether the group configuration is forcibly used.
        self.forced_setting = forced_setting
        # The group ID.
        self.group_id = group_id
        # The group name.
        self.name = name
        # The notification configuration.
        self.notify_config = notify_config
        # The list of notification operation types.
        self.notify_operation_types = notify_operation_types
        # The project ID.
        self.project_id = project_id
        # The RAM role (1 to 128 characters). The system assumes this role to execute the template when a new job is triggered. This parameter is required when the job trigger mode is not manual.
        self.ram_role = ram_role
        # The list of report export field options.
        self.report_export_field = report_export_field
        # The export address for the execution report. OSS addresses are supported. Format: https://<OSS bucket address>/<path>.
        self.report_export_path = report_export_path
        # The number of tasks.
        self.task_cnt = task_cnt
        # The Terraform provider version. Select a Terraform provider version. Tasks in the group are executed based on the specified Terraform provider version. The version configured on a task takes higher priority. This version may conflict with the Terraform provider version specified in the module.
        self.terraform_provider_version = terraform_provider_version
        # The trigger policy. This parameter cannot be empty when autoTrigger is set to true.
        self.trigger_config = trigger_config
        # The resource type that triggers execution. Valid values:
        # 
        # - Task: regular task
        # - SceneTestingTask: scenario-based testing task.
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

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.forced_setting is not None:
            result['forcedSetting'] = self.forced_setting

        if self.group_id is not None:
            result['groupId'] = self.group_id

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

        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt

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

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('forcedSetting') is not None:
            self.forced_setting = m.get('forcedSetting')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.notify_config = []
        if m.get('notifyConfig') is not None:
            for k1 in m.get('notifyConfig'):
                temp_model = main_models.GetGroupResponseBodyGroupNotifyConfig()
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

        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')

        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')

        self.trigger_config = []
        if m.get('triggerConfig') is not None:
            for k1 in m.get('triggerConfig'):
                temp_model = main_models.GetGroupResponseBodyGroupTriggerConfig()
                self.trigger_config.append(temp_model.from_map(k1))

        if m.get('triggerResourceType') is not None:
            self.trigger_resource_type = m.get('triggerResourceType')

        return self

class GetGroupResponseBodyGroupTriggerConfig(DaraModel):
    def __init__(
        self,
        trigger_strategy: str = None,
        trigger_value: str = None,
    ):
        # The trigger strategy. Valid values:
        # 
        # - ProviderNewVersion: triggered when a new provider version is released
        # - Cron: triggered on a schedule.
        self.trigger_strategy = trigger_strategy
        # The policy value that must be maintained for scheduled triggering. This value is a cron expression.
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

class GetGroupResponseBodyGroupNotifyConfig(DaraModel):
    def __init__(
        self,
        notify_path: str = None,
        notify_type: str = None,
    ):
        # The path configuration for notifications.
        self.notify_path = notify_path
        # The notification type. Valid values:
        # DingDing.
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

