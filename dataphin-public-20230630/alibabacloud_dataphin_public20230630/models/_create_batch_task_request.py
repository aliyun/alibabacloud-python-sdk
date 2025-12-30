# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateBatchTaskRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateBatchTaskRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command = create_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateBatchTaskRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateBatchTaskRequestCreateCommand(DaraModel):
    def __init__(
        self,
        data_source_catalog: str = None,
        data_source_id: str = None,
        data_source_schema: str = None,
        description: str = None,
        directory: str = None,
        engine: str = None,
        name: str = None,
        project_id: int = None,
        python_module_list: List[str] = None,
        schedule_type: int = None,
        task_type: int = None,
    ):
        self.data_source_catalog = data_source_catalog
        self.data_source_id = data_source_id
        self.data_source_schema = data_source_schema
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.directory = directory
        self.engine = engine
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project_id = project_id
        self.python_module_list = python_module_list
        # This parameter is required.
        self.schedule_type = schedule_type
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_catalog is not None:
            result['DataSourceCatalog'] = self.data_source_catalog

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_schema is not None:
            result['DataSourceSchema'] = self.data_source_schema

        if self.description is not None:
            result['Description'] = self.description

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.python_module_list is not None:
            result['PythonModuleList'] = self.python_module_list

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceCatalog') is not None:
            self.data_source_catalog = m.get('DataSourceCatalog')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceSchema') is not None:
            self.data_source_schema = m.get('DataSourceSchema')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('PythonModuleList') is not None:
            self.python_module_list = m.get('PythonModuleList')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

