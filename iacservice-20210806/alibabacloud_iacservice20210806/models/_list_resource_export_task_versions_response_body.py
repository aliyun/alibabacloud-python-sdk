# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListResourceExportTaskVersionsResponseBody(DaraModel):
    def __init__(
        self,
        export_tasks: List[main_models.ListResourceExportTaskVersionsResponseBodyExportTasks] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of export task versions.
        self.export_tasks = export_tasks
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of results per page. Default value: 20. Minimum value: 1. Maximum value: 100.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.export_tasks:
            for v1 in self.export_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['exportTasks'] = []
        if self.export_tasks is not None:
            for k1 in self.export_tasks:
                result['exportTasks'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.export_tasks = []
        if m.get('exportTasks') is not None:
            for k1 in m.get('exportTasks'):
                temp_model = main_models.ListResourceExportTaskVersionsResponseBodyExportTasks()
                self.export_tasks.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListResourceExportTaskVersionsResponseBodyExportTasks(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        elapsed_time: int = None,
        export_task_id: str = None,
        export_to_module: main_models.ListResourceExportTaskVersionsResponseBodyExportTasksExportToModule = None,
        export_version: str = None,
        failed_reason: str = None,
        include_rules: List[main_models.ListResourceExportTaskVersionsResponseBodyExportTasksIncludeRules] = None,
        managed_task_id: str = None,
        modules: List[main_models.ListResourceExportTaskVersionsResponseBodyExportTasksModules] = None,
        name: str = None,
        status: str = None,
        variables: List[main_models.ListResourceExportTaskVersionsResponseBodyExportTasksVariables] = None,
    ):
        # The creation time in UTC, in the ISO 8601 format of YYYY-MM-DDTHH:mm:ssZ.
        self.create_time = create_time
        # The description.
        self.description = description
        # The execution duration.
        self.elapsed_time = elapsed_time
        # The ID of the resource export task.
        self.export_task_id = export_task_id
        # The module to which the exported template is saved. If this parameter is not set, the template is automatically saved in the Registry.
        self.export_to_module = export_to_module
        # The resource export version.
        self.export_version = export_version
        # The reason for the export failure.
        self.failed_reason = failed_reason
        # The list of include rules used when exporting resources.
        self.include_rules = include_rules
        self.managed_task_id = managed_task_id
        # The module configuration of the exported resources.
        self.modules = modules
        # The name of the export task.
        self.name = name
        # The version export status. Valid values:
        # - Queue: queued
        # - Pending: preparing to run
        # - Success: succeeded
        # - Errored: failed
        # - Canceled: canceled
        self.status = status
        # The list of variables. Parameters of exported resources are set as variables.
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

        if self.managed_task_id is not None:
            result['managedTaskId'] = self.managed_task_id

        result['modules'] = []
        if self.modules is not None:
            for k1 in self.modules:
                result['modules'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

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
            temp_model = main_models.ListResourceExportTaskVersionsResponseBodyExportTasksExportToModule()
            self.export_to_module = temp_model.from_map(m.get('exportToModule'))

        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')

        if m.get('failedReason') is not None:
            self.failed_reason = m.get('failedReason')

        self.include_rules = []
        if m.get('includeRules') is not None:
            for k1 in m.get('includeRules'):
                temp_model = main_models.ListResourceExportTaskVersionsResponseBodyExportTasksIncludeRules()
                self.include_rules.append(temp_model.from_map(k1))

        if m.get('managedTaskId') is not None:
            self.managed_task_id = m.get('managedTaskId')

        self.modules = []
        if m.get('modules') is not None:
            for k1 in m.get('modules'):
                temp_model = main_models.ListResourceExportTaskVersionsResponseBodyExportTasksModules()
                self.modules.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.variables = []
        if m.get('variables') is not None:
            for k1 in m.get('variables'):
                temp_model = main_models.ListResourceExportTaskVersionsResponseBodyExportTasksVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class ListResourceExportTaskVersionsResponseBodyExportTasksVariables(DaraModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        # The list of Terraform resource properties corresponding to the resource type.
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

class ListResourceExportTaskVersionsResponseBodyExportTasksModules(DaraModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        version: str = None,
    ):
        # The module type where the exported template is located. Two formats are supported: CloudRegistry and OSS. If the ExportToModule parameter is specified, both formats are returned. Otherwise, only CloudRegistry is returned.
        self.source = source
        # The download address of the exported template within the module.
        # 
        # - If Source is CloudRegistry, the format is: "cloudregistry::iacservice//"
        # 
        # - If Source is OSS, the format is: "oss::https://.oss-cn-hangzhou.aliyuncs.com/xxx.zip"
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

class ListResourceExportTaskVersionsResponseBodyExportTasksIncludeRules(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The name of the include rule for resource export. Valid values:
        # 
        # - ResourceType: required. The resource type. Example: ALIYUN::VPC::VPC.
        # - RegionId: required. The region to which the resource belongs. Only one region is supported. Example: cn-chengdu.
        # - \\<ResourceType>:Id: the resource ID. Example: ALIYUN::VPC::VPC:Id.
        # - ResourceGroupId: the resource group ID. Example: rg-1234.
        # - ZoneId: the zone to which the resource belongs. Only one zone is supported. Example: cn-hangzhou-h.
        # 
        # Multiple filter conditions have an AND relationship by default. A resource must meet all filter conditions to be considered a match.
        self.key = key
        # The values of the include rule for resource export.
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

class ListResourceExportTaskVersionsResponseBodyExportTasksExportToModule(DaraModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        # The module type to which the exported template is saved. Valid values:
        # 
        # - OSS: OSS
        # - Registry: Terraform Registry
        self.source = source
        # The path where the template content is saved.
        # 
        # - If Source is set to Registry, the format is: "cloudregistry::iacservice//"
        # 
        # - If Source is set to OSS, the format is: "oss::https://.oss-cn-hangzhou.aliyuncs.com/xxx.zip"
        self.source_path = source_path
        # The path of the State file corresponding to the module.
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

