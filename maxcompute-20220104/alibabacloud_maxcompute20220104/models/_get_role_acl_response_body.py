# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetRoleAclResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetRoleAclResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetRoleAclResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetRoleAclResponseBodyData(DaraModel):
    def __init__(
        self,
        function: List[main_models.GetRoleAclResponseBodyDataFunction] = None,
        instance: List[main_models.GetRoleAclResponseBodyDataInstance] = None,
        package: List[main_models.GetRoleAclResponseBodyDataPackage] = None,
        project: List[main_models.GetRoleAclResponseBodyDataProject] = None,
        resource: List[main_models.GetRoleAclResponseBodyDataResource] = None,
        table: List[main_models.GetRoleAclResponseBodyDataTable] = None,
    ):
        self.function = function
        self.instance = instance
        self.package = package
        self.project = project
        self.resource = resource
        self.table = table

    def validate(self):
        if self.function:
            for v1 in self.function:
                 if v1:
                    v1.validate()
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()
        if self.package:
            for v1 in self.package:
                 if v1:
                    v1.validate()
        if self.project:
            for v1 in self.project:
                 if v1:
                    v1.validate()
        if self.resource:
            for v1 in self.resource:
                 if v1:
                    v1.validate()
        if self.table:
            for v1 in self.table:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['function'] = []
        if self.function is not None:
            for k1 in self.function:
                result['function'].append(k1.to_map() if k1 else None)

        result['instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['instance'].append(k1.to_map() if k1 else None)

        result['package'] = []
        if self.package is not None:
            for k1 in self.package:
                result['package'].append(k1.to_map() if k1 else None)

        result['project'] = []
        if self.project is not None:
            for k1 in self.project:
                result['project'].append(k1.to_map() if k1 else None)

        result['resource'] = []
        if self.resource is not None:
            for k1 in self.resource:
                result['resource'].append(k1.to_map() if k1 else None)

        result['table'] = []
        if self.table is not None:
            for k1 in self.table:
                result['table'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function = []
        if m.get('function') is not None:
            for k1 in m.get('function'):
                temp_model = main_models.GetRoleAclResponseBodyDataFunction()
                self.function.append(temp_model.from_map(k1))

        self.instance = []
        if m.get('instance') is not None:
            for k1 in m.get('instance'):
                temp_model = main_models.GetRoleAclResponseBodyDataInstance()
                self.instance.append(temp_model.from_map(k1))

        self.package = []
        if m.get('package') is not None:
            for k1 in m.get('package'):
                temp_model = main_models.GetRoleAclResponseBodyDataPackage()
                self.package.append(temp_model.from_map(k1))

        self.project = []
        if m.get('project') is not None:
            for k1 in m.get('project'):
                temp_model = main_models.GetRoleAclResponseBodyDataProject()
                self.project.append(temp_model.from_map(k1))

        self.resource = []
        if m.get('resource') is not None:
            for k1 in m.get('resource'):
                temp_model = main_models.GetRoleAclResponseBodyDataResource()
                self.resource.append(temp_model.from_map(k1))

        self.table = []
        if m.get('table') is not None:
            for k1 in m.get('table'):
                temp_model = main_models.GetRoleAclResponseBodyDataTable()
                self.table.append(temp_model.from_map(k1))

        return self

class GetRoleAclResponseBodyDataTable(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        self.actions = actions
        self.name = name
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.name is not None:
            result['name'] = self.name

        if self.schema_name is not None:
            result['schemaName'] = self.schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')

        return self

class GetRoleAclResponseBodyDataResource(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        self.actions = actions
        self.name = name
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.name is not None:
            result['name'] = self.name

        if self.schema_name is not None:
            result['schemaName'] = self.schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')

        return self

class GetRoleAclResponseBodyDataProject(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        self.actions = actions
        self.name = name
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.name is not None:
            result['name'] = self.name

        if self.schema_name is not None:
            result['schemaName'] = self.schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')

        return self

class GetRoleAclResponseBodyDataPackage(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        self.actions = actions
        self.name = name
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.name is not None:
            result['name'] = self.name

        if self.schema_name is not None:
            result['schemaName'] = self.schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')

        return self

class GetRoleAclResponseBodyDataInstance(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        self.actions = actions
        self.name = name
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.name is not None:
            result['name'] = self.name

        if self.schema_name is not None:
            result['schemaName'] = self.schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')

        return self

class GetRoleAclResponseBodyDataFunction(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        self.actions = actions
        self.name = name
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.name is not None:
            result['name'] = self.name

        if self.schema_name is not None:
            result['schemaName'] = self.schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')

        return self

