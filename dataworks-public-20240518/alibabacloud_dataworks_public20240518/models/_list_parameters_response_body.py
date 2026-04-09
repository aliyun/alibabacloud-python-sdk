# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListParametersResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListParametersResponseBodyPagingInfo = None,
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
            temp_model = main_models.ListParametersResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListParametersResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        parameters: List[main_models.ListParametersResponseBodyPagingInfoParameters] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.parameters = parameters
        self.total_count = total_count

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.ListParametersResponseBodyPagingInfoParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListParametersResponseBodyPagingInfoParameters(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        create_user: str = None,
        description: str = None,
        id: int = None,
        modify_time: int = None,
        modify_user: str = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        properties: List[main_models.ListParametersResponseBodyPagingInfoParametersProperties] = None,
        scope: str = None,
        type: str = None,
        version: int = None,
    ):
        self.create_time = create_time
        self.create_user = create_user
        self.description = description
        self.id = id
        self.modify_time = modify_time
        self.modify_user = modify_user
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.properties = properties
        self.scope = scope
        self.type = type
        self.version = version

    def validate(self):
        if self.properties:
            for v1 in self.properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        result['Properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['Properties'].append(k1.to_map() if k1 else None)

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        self.properties = []
        if m.get('Properties') is not None:
            for k1 in m.get('Properties'):
                temp_model = main_models.ListParametersResponseBodyPagingInfoParametersProperties()
                self.properties.append(temp_model.from_map(k1))

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListParametersResponseBodyPagingInfoParametersProperties(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        value: str = None,
    ):
        self.env_type = env_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

