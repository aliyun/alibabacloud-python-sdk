# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListResourceExportTasksResponseBody(DaraModel):
    def __init__(
        self,
        export_tasks: List[main_models.ListResourceExportTasksResponseBodyExportTasks] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.export_tasks = export_tasks
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
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
                temp_model = main_models.ListResourceExportTasksResponseBodyExportTasks()
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

class ListResourceExportTasksResponseBodyExportTasks(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        elapsed_time: int = None,
        export_status: str = None,
        export_task_id: str = None,
        export_to_module: main_models.ListResourceExportTasksResponseBodyExportTasksExportToModule = None,
        export_version: str = None,
        include_rules: List[main_models.ListResourceExportTasksResponseBodyExportTasksIncludeRules] = None,
        modules: List[main_models.ListResourceExportTasksResponseBodyExportTasksModules] = None,
        name: str = None,
        status: str = None,
        variables: List[main_models.ListResourceExportTasksResponseBodyExportTasksVariables] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.elapsed_time = elapsed_time
        self.export_status = export_status
        self.export_task_id = export_task_id
        self.export_to_module = export_to_module
        self.export_version = export_version
        self.include_rules = include_rules
        self.modules = modules
        self.name = name
        self.status = status
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

        if self.export_status is not None:
            result['exportStatus'] = self.export_status

        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id

        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()

        if self.export_version is not None:
            result['exportVersion'] = self.export_version

        result['includeRules'] = []
        if self.include_rules is not None:
            for k1 in self.include_rules:
                result['includeRules'].append(k1.to_map() if k1 else None)

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

        if m.get('exportStatus') is not None:
            self.export_status = m.get('exportStatus')

        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')

        if m.get('exportToModule') is not None:
            temp_model = main_models.ListResourceExportTasksResponseBodyExportTasksExportToModule()
            self.export_to_module = temp_model.from_map(m.get('exportToModule'))

        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')

        self.include_rules = []
        if m.get('includeRules') is not None:
            for k1 in m.get('includeRules'):
                temp_model = main_models.ListResourceExportTasksResponseBodyExportTasksIncludeRules()
                self.include_rules.append(temp_model.from_map(k1))

        self.modules = []
        if m.get('modules') is not None:
            for k1 in m.get('modules'):
                temp_model = main_models.ListResourceExportTasksResponseBodyExportTasksModules()
                self.modules.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.variables = []
        if m.get('variables') is not None:
            for k1 in m.get('variables'):
                temp_model = main_models.ListResourceExportTasksResponseBodyExportTasksVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class ListResourceExportTasksResponseBodyExportTasksVariables(DaraModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        self.properties = properties
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

class ListResourceExportTasksResponseBodyExportTasksModules(DaraModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        version: str = None,
    ):
        self.source = source
        self.source_path = source_path
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

class ListResourceExportTasksResponseBodyExportTasksIncludeRules(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
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

class ListResourceExportTasksResponseBodyExportTasksExportToModule(DaraModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        self.source = source
        self.source_path = source_path
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

