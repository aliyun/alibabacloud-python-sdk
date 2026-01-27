# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListApprovalSchemasForApprovalProcessesResponseBody(DaraModel):
    def __init__(
        self,
        processes: List[main_models.ListApprovalSchemasForApprovalProcessesResponseBodyProcesses] = None,
        request_id: str = None,
    ):
        self.processes = processes
        self.request_id = request_id

    def validate(self):
        if self.processes:
            for v1 in self.processes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Processes'] = []
        if self.processes is not None:
            for k1 in self.processes:
                result['Processes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.processes = []
        if m.get('Processes') is not None:
            for k1 in m.get('Processes'):
                temp_model = main_models.ListApprovalSchemasForApprovalProcessesResponseBodyProcesses()
                self.processes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListApprovalSchemasForApprovalProcessesResponseBodyProcesses(DaraModel):
    def __init__(
        self,
        process_id: str = None,
        schemas: List[main_models.ListApprovalSchemasForApprovalProcessesResponseBodyProcessesSchemas] = None,
    ):
        self.process_id = process_id
        self.schemas = schemas

    def validate(self):
        if self.schemas:
            for v1 in self.schemas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        result['Schemas'] = []
        if self.schemas is not None:
            for k1 in self.schemas:
                result['Schemas'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        self.schemas = []
        if m.get('Schemas') is not None:
            for k1 in m.get('Schemas'):
                temp_model = main_models.ListApprovalSchemasForApprovalProcessesResponseBodyProcessesSchemas()
                self.schemas.append(temp_model.from_map(k1))

        return self

class ListApprovalSchemasForApprovalProcessesResponseBodyProcessesSchemas(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        is_default: bool = None,
        policy_type: str = None,
        schema_content: str = None,
        schema_id: str = None,
        schema_name: str = None,
        schema_version: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.is_default = is_default
        self.policy_type = policy_type
        self.schema_content = schema_content
        self.schema_id = schema_id
        self.schema_name = schema_name
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.schema_content is not None:
            result['SchemaContent'] = self.schema_content

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('SchemaContent') is not None:
            self.schema_content = m.get('SchemaContent')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')

        return self

