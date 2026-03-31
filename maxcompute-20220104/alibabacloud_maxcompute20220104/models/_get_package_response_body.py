# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetPackageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetPackageResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The ID of the request.
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
            temp_model = main_models.GetPackageResponseBodyData()
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

class GetPackageResponseBodyData(DaraModel):
    def __init__(
        self,
        allowed_project_list: List[main_models.GetPackageResponseBodyDataAllowedProjectList] = None,
        resource_list: main_models.GetPackageResponseBodyDataResourceList = None,
    ):
        # The projects in which the package is installed.
        self.allowed_project_list = allowed_project_list
        # The details of the resources that are included in the package.
        self.resource_list = resource_list

    def validate(self):
        if self.allowed_project_list:
            for v1 in self.allowed_project_list:
                 if v1:
                    v1.validate()
        if self.resource_list:
            self.resource_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['allowedProjectList'] = []
        if self.allowed_project_list is not None:
            for k1 in self.allowed_project_list:
                result['allowedProjectList'].append(k1.to_map() if k1 else None)

        if self.resource_list is not None:
            result['resourceList'] = self.resource_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.allowed_project_list = []
        if m.get('allowedProjectList') is not None:
            for k1 in m.get('allowedProjectList'):
                temp_model = main_models.GetPackageResponseBodyDataAllowedProjectList()
                self.allowed_project_list.append(temp_model.from_map(k1))

        if m.get('resourceList') is not None:
            temp_model = main_models.GetPackageResponseBodyDataResourceList()
            self.resource_list = temp_model.from_map(m.get('resourceList'))

        return self

class GetPackageResponseBodyDataResourceList(DaraModel):
    def __init__(
        self,
        function: List[main_models.GetPackageResponseBodyDataResourceListFunction] = None,
        resource: List[main_models.GetPackageResponseBodyDataResourceListResource] = None,
        table: List[main_models.GetPackageResponseBodyDataResourceListTable] = None,
    ):
        # The functions.
        self.function = function
        # The resources.
        self.resource = resource
        # The tables.
        self.table = table

    def validate(self):
        if self.function:
            for v1 in self.function:
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
                temp_model = main_models.GetPackageResponseBodyDataResourceListFunction()
                self.function.append(temp_model.from_map(k1))

        self.resource = []
        if m.get('resource') is not None:
            for k1 in m.get('resource'):
                temp_model = main_models.GetPackageResponseBodyDataResourceListResource()
                self.resource.append(temp_model.from_map(k1))

        self.table = []
        if m.get('table') is not None:
            for k1 in m.get('table'):
                temp_model = main_models.GetPackageResponseBodyDataResourceListTable()
                self.table.append(temp_model.from_map(k1))

        return self

class GetPackageResponseBodyDataResourceListTable(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the table.
        self.actions = actions
        # The name of the table.
        self.name = name
        # The name of schema.
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

class GetPackageResponseBodyDataResourceListResource(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the resource.
        self.actions = actions
        # The name of the resource.
        self.name = name
        # The name of schema.
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

class GetPackageResponseBodyDataResourceListFunction(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the function.
        self.actions = actions
        # The name of the function.
        self.name = name
        # The name of schema.
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

class GetPackageResponseBodyDataAllowedProjectList(DaraModel):
    def __init__(
        self,
        label: str = None,
        project: str = None,
    ):
        # The security level for sensitive data.
        self.label = label
        # The name of the MaxCompute project.
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['label'] = self.label

        if self.project is not None:
            result['project'] = self.project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('project') is not None:
            self.project = m.get('project')

        return self

