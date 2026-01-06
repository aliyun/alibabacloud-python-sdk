# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountPrivilegesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeAccountPrivilegesResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of the permissions.
        self.data = data
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeAccountPrivilegesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAccountPrivilegesResponseBodyData(DaraModel):
    def __init__(
        self,
        privilege_object: main_models.DescribeAccountPrivilegesResponseBodyDataPrivilegeObject = None,
        privilege_type: str = None,
        privileges: List[str] = None,
    ):
        # The objects on which the permission takes effect, including databases, tables, columns, and additional descriptions.
        self.privilege_object = privilege_object
        # The permission level of the permission. Valid values: `Global`, `Database`, `Table`, and `Column`. You can call the `DescribeEnabledPrivileges` parameter to query the permission level of a specific permission.
        self.privilege_type = privilege_type
        # The name of the permission. You can call the `DescribeEnabledPrivileges` operation to query the name of the permission.
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
            temp_model = main_models.DescribeAccountPrivilegesResponseBodyDataPrivilegeObject()
            self.privilege_object = temp_model.from_map(m.get('PrivilegeObject'))

        if m.get('PrivilegeType') is not None:
            self.privilege_type = m.get('PrivilegeType')

        if m.get('Privileges') is not None:
            self.privileges = m.get('Privileges')

        return self

class DescribeAccountPrivilegesResponseBodyDataPrivilegeObject(DaraModel):
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

