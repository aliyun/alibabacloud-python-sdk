# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListProcessDefinitionsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListProcessDefinitionsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        self.paging_info = paging_info
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListProcessDefinitionsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProcessDefinitionsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        process_definitions: List[main_models.ListProcessDefinitionsResponseBodyPagingInfoProcessDefinitions] = None,
        total_count: int = None,
    ):
        self.process_definitions = process_definitions
        self.total_count = total_count

    def validate(self):
        if self.process_definitions:
            for v1 in self.process_definitions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProcessDefinitions'] = []
        if self.process_definitions is not None:
            for k1 in self.process_definitions:
                result['ProcessDefinitions'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.process_definitions = []
        if m.get('ProcessDefinitions') is not None:
            for k1 in m.get('ProcessDefinitions'):
                temp_model = main_models.ListProcessDefinitionsResponseBodyPagingInfoProcessDefinitions()
                self.process_definitions.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProcessDefinitionsResponseBodyPagingInfoProcessDefinitions(DaraModel):
    def __init__(
        self,
        description: str = None,
        enabled: bool = None,
        id: str = None,
        is_system: bool = None,
        name: str = None,
        priority: str = None,
        scopes: List[str] = None,
        sub_type: str = None,
        type: str = None,
    ):
        self.description = description
        self.enabled = enabled
        self.id = id
        self.is_system = is_system
        self.name = name
        self.priority = priority
        self.scopes = scopes
        self.sub_type = sub_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

        if self.is_system is not None:
            result['IsSystem'] = self.is_system

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.scopes is not None:
            result['Scopes'] = self.scopes

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsSystem') is not None:
            self.is_system = m.get('IsSystem')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Scopes') is not None:
            self.scopes = m.get('Scopes')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

