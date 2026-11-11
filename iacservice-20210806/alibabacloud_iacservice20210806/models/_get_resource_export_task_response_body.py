# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetResourceExportTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task: main_models.GetResourceExportTaskResponseBodyTask = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The task information.
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.task is not None:
            result['task'] = self.task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('task') is not None:
            temp_model = main_models.GetResourceExportTaskResponseBodyTask()
            self.task = temp_model.from_map(m.get('task'))

        return self

class GetResourceExportTaskResponseBodyTask(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        elapsed_time: int = None,
        export_task_id: str = None,
        export_to_module: main_models.GetResourceExportTaskResponseBodyTaskExportToModule = None,
        export_version: str = None,
        failed_reason: str = None,
        include_rules: List[main_models.GetResourceExportTaskResponseBodyTaskIncludeRules] = None,
        modify_time: str = None,
        modules: List[main_models.GetResourceExportTaskResponseBodyTaskModules] = None,
        name: str = None,
        ram_role: str = None,
        status: str = None,
        task_output_path: str = None,
        terraform_context: Dict[str, Any] = None,
        terraform_provider_version: str = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
        variables: List[main_models.GetResourceExportTaskResponseBodyTaskVariables] = None,
    ):
        # The time when the task was created. The time is displayed in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format.
        self.create_time = create_time
        # The description of the task.
        self.description = description
        # The execution duration.
        self.elapsed_time = elapsed_time
        # The ID of the resource export task.
        self.export_task_id = export_task_id
        # Saves the exported template as a module. If this parameter is not specified, the template is automatically saved in the registry.
        self.export_to_module = export_to_module
        # The resource export version.
        self.export_version = export_version
        # The cause of the failure.
        self.failed_reason = failed_reason
        # The inclusion rules for resource export.
        self.include_rules = include_rules
        # The time when the task was modified. The time is displayed in UTC and follows the ISO 8601 standard.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.modify_time = modify_time
        # The module configurations after the resources are exported.
        self.modules = modules
        # The name of the task.
        self.name = name
        # The Resource Access Management (RAM) role.
        self.ram_role = ram_role
        # The status of the task. Valid values:
        # 
        # - Available: The task is available and no jobs are running.
        # - Running: The task is running and a job is in progress.
        self.status = status
        # The output path of the task.
        self.task_output_path = task_output_path
        # The Terraform content.
        self.terraform_context = terraform_context
        # The Terraform provider version.
        self.terraform_provider_version = terraform_provider_version
        # The Terraform version.
        self.terraform_version = terraform_version
        # The trigger strategy. Valid values:
        # 
        # - Auto: The task is automatically triggered when the rules or trigger strategy are modified.
        # - Manual: The task is manually triggered.
        # 
        # Default value: Manual.
        self.trigger_strategy = trigger_strategy
        # The list of variables. The parameters of the exported resources are set as variables.
        self.variables = variables

    def validate(self):
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for v1 in self.include_rules:
                 if v1:
                    v1.validate()
        if self.modules:
            for v1 in self.modules:
                 if v1:
                    v1.validate()
        if self.variables:
            for v1 in self.variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time

        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id

        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()

        if self.export_version is not None:
            result['exportVersion'] = self.export_version

        if self.failed_reason is not None:
            result['failedReason'] = self.failed_reason

        result['includeRules'] = []
        if self.include_rules is not None:
            for k1 in self.include_rules:
                result['includeRules'].append(k1.to_map() if k1 else None)

        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time

        result['modules'] = []
        if self.modules is not None:
            for k1 in self.modules:
                result['modules'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.ram_role is not None:
            result['ramRole'] = self.ram_role

        if self.status is not None:
            result['status'] = self.status

        if self.task_output_path is not None:
            result['taskOutputPath'] = self.task_output_path

        if self.terraform_context is not None:
            result['terraformContext'] = self.terraform_context

        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version

        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version

        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy

        result['variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')

        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')

        if m.get('exportToModule') is not None:
            temp_model = main_models.GetResourceExportTaskResponseBodyTaskExportToModule()
            self.export_to_module = temp_model.from_map(m.get('exportToModule'))

        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')

        if m.get('failedReason') is not None:
            self.failed_reason = m.get('failedReason')

        self.include_rules = []
        if m.get('includeRules') is not None:
            for k1 in m.get('includeRules'):
                temp_model = main_models.GetResourceExportTaskResponseBodyTaskIncludeRules()
                self.include_rules.append(temp_model.from_map(k1))

        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')

        self.modules = []
        if m.get('modules') is not None:
            for k1 in m.get('modules'):
                temp_model = main_models.GetResourceExportTaskResponseBodyTaskModules()
                self.modules.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskOutputPath') is not None:
            self.task_output_path = m.get('taskOutputPath')

        if m.get('terraformContext') is not None:
            self.terraform_context = m.get('terraformContext')

        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')

        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')

        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')

        self.variables = []
        if m.get('variables') is not None:
            for k1 in m.get('variables'):
                temp_model = main_models.GetResourceExportTaskResponseBodyTaskVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class GetResourceExportTaskResponseBodyTaskVariables(DaraModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        # The list of properties for the Terraform resource that corresponds to the resource type.
        self.properties = properties
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.properties is not None:
            result['properties'] = self.properties

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class GetResourceExportTaskResponseBodyTaskModules(DaraModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        version: str = None,
    ):
        # The type of the module where the exported template is located. Two formats are supported: CloudRegistry and OSS. If the ExportToModule parameter is specified, both formats are returned. Otherwise, only CloudRegistry is returned.
        self.source = source
        # The download URL of the module where the exported template is located.
        # 
        # - If Source is set to CloudRegistry, the format is cloudregistry::iacservice//.
        # 
        # - If Source is set to OSS, the format is oss::https://.oss-cn-hangzhou.aliyuncs.com/xxx.zip.
        self.source_path = source_path
        # The version of the module where the exported template is located.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['source'] = self.source

        if self.source_path is not None:
            result['sourcePath'] = self.source_path

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class GetResourceExportTaskResponseBodyTaskIncludeRules(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The name of the inclusion rule for resource export. Valid values:
        # 
        # - ResourceType: required. The resource type. Example: ALIYUN::VPC::VPC.
        # - RegionId: required. The region to which the resource belongs. Only one region is supported. Example: cn-chengdu.
        # - <ResourceType>:Id: the resource ID. Example: ALIYUN::VPC::VPC:Id.
        # - ResourceGroupId: the resource group ID. Example: rg-1234.
        # - ZoneId: the zone to which the resource belongs. Only one zone is supported. Example: cn-hangzhou-h.
        # 
        # By default, multiple filter conditions are connected by the AND operator. A resource matches the filter conditions only if it meets all the conditions.
        self.key = key
        # The inclusion rules for resource export.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

class GetResourceExportTaskResponseBodyTaskExportToModule(DaraModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        # The type of the module where the exported template is saved. Valid values:
        # 
        # - OSS: Object Storage Service (OSS).
        # - Registry: Terraform Registry.
        self.source = source
        # The path where the template content is saved.
        # 
        # - If Source is set to Registry, the format is cloudregistry::iacservice//.
        # 
        # - If Source is set to OSS, the format is oss::https://.oss-cn-hangzhou.aliyuncs.com/xxx.zip.
        self.source_path = source_path
        # The path of the state file that corresponds to the module.
        self.state_path = state_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['source'] = self.source

        if self.source_path is not None:
            result['sourcePath'] = self.source_path

        if self.state_path is not None:
            result['statePath'] = self.state_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')

        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')

        return self

