# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListApprovalProcessesForApprovalSchemasResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        schemas: List[main_models.ListApprovalProcessesForApprovalSchemasResponseBodySchemas] = None,
    ):
        self.request_id = request_id
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Schemas'] = []
        if self.schemas is not None:
            for k1 in self.schemas:
                result['Schemas'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.schemas = []
        if m.get('Schemas') is not None:
            for k1 in m.get('Schemas'):
                temp_model = main_models.ListApprovalProcessesForApprovalSchemasResponseBodySchemas()
                self.schemas.append(temp_model.from_map(k1))

        return self

class ListApprovalProcessesForApprovalSchemasResponseBodySchemas(DaraModel):
    def __init__(
        self,
        processes: List[main_models.ListApprovalProcessesForApprovalSchemasResponseBodySchemasProcesses] = None,
        schema_id: str = None,
    ):
        self.processes = processes
        self.schema_id = schema_id

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

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.processes = []
        if m.get('Processes') is not None:
            for k1 in m.get('Processes'):
                temp_model = main_models.ListApprovalProcessesForApprovalSchemasResponseBodySchemasProcesses()
                self.processes.append(temp_model.from_map(k1))

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class ListApprovalProcessesForApprovalSchemasResponseBodySchemasProcesses(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        process_id: str = None,
        process_name: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.process_id = process_id
        self.process_name = process_name

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

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        return self

