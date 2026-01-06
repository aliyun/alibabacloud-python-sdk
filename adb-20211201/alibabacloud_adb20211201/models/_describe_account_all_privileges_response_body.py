# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountAllPrivilegesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeAccountAllPrivilegesResponseBodyData = None,
        request_id: str = None,
    ):
        # Details of the permissions.
        self.data = data
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
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeAccountAllPrivilegesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAccountAllPrivilegesResponseBodyData(DaraModel):
    def __init__(
        self,
        marker: str = None,
        result: List[main_models.DescribeAccountAllPrivilegesResponseBodyDataResult] = None,
        truncated: bool = None,
    ):
        # Indicates the position where the results are truncated. When a value of `true` is returned for the `Truncated` parameter, this parameter is present and contains the value to use for the Marker parameter in a subsequent call.
        self.marker = marker
        # The permissions.
        self.result = result
        # Indicates whether the results are truncated. If the results are truncated, a value of `true` is returned. In this case, you must call this operation again to obtain all the results until a value of `false` is returned for this parameter.
        self.truncated = truncated

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.marker is not None:
            result['Marker'] = self.marker

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.truncated is not None:
            result['Truncated'] = self.truncated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeAccountAllPrivilegesResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Truncated') is not None:
            self.truncated = m.get('Truncated')

        return self

class DescribeAccountAllPrivilegesResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        privilege_object: main_models.DescribeAccountAllPrivilegesResponseBodyDataResultPrivilegeObject = None,
        privilege_type: str = None,
        privileges: List[str] = None,
    ):
        # The objects on which the permission takes effect, including databases, tables, and columns. If Global is returned for the PrivilegeType parameter, an empty string is returned for this parameter.
        self.privilege_object = privilege_object
        # The permission level of the database account. You can call the `DescribeEnabledPrivileges` operation to query the permission level of the database account.
        self.privilege_type = privilege_type
        # The name of the permission, which is the same as the permission name returned by the `DescribeEnabledPrivileges` operation.
        self.privileges = privileges

    def validate(self):
        if self.privilege_object:
            self.privilege_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.privilege_object is not None:
            result['PrivilegeObject'] = self.privilege_object.to_map()

        if self.privilege_type is not None:
            result['PrivilegeType'] = self.privilege_type

        if self.privileges is not None:
            result['Privileges'] = self.privileges

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivilegeObject') is not None:
            temp_model = main_models.DescribeAccountAllPrivilegesResponseBodyDataResultPrivilegeObject()
            self.privilege_object = temp_model.from_map(m.get('PrivilegeObject'))

        if m.get('PrivilegeType') is not None:
            self.privilege_type = m.get('PrivilegeType')

        if m.get('Privileges') is not None:
            self.privileges = m.get('Privileges')

        return self

class DescribeAccountAllPrivilegesResponseBodyDataResultPrivilegeObject(DaraModel):
    def __init__(
        self,
        column: str = None,
        database: str = None,
        description: str = None,
        table: str = None,
    ):
        # The name of the column.
        self.column = column
        # The name of the database.
        self.database = database
        # The description of the permission object.
        self.description = description
        # The name of the table.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['Column'] = self.column

        if self.database is not None:
            result['Database'] = self.database

        if self.description is not None:
            result['Description'] = self.description

        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

