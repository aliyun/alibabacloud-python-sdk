# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListClientUsersResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListClientUsersResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
            temp_model = main_models.ListClientUsersResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClientUsersResponseBodyData(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.ListClientUsersResponseBodyDataDataList] = None,
        total_num: int = None,
    ):
        self.data_list = data_list
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.ListClientUsersResponseBodyDataDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListClientUsersResponseBodyDataDataList(DaraModel):
    def __init__(
        self,
        department: main_models.ListClientUsersResponseBodyDataDataListDepartment = None,
        department_id: str = None,
        description: str = None,
        email: str = None,
        id: str = None,
        idp_config_id: str = None,
        mobile_number: str = None,
        status: str = None,
        user_id: str = None,
        username: str = None,
    ):
        self.department = department
        self.department_id = department_id
        self.description = description
        self.email = email
        self.id = id
        self.idp_config_id = idp_config_id
        self.mobile_number = mobile_number
        self.status = status
        self.user_id = user_id
        self.username = username

    def validate(self):
        if self.department:
            self.department.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department is not None:
            result['Department'] = self.department.to_map()

        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.description is not None:
            result['Description'] = self.description

        if self.email is not None:
            result['Email'] = self.email

        if self.id is not None:
            result['Id'] = self.id

        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id

        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            temp_model = main_models.ListClientUsersResponseBodyDataDataListDepartment()
            self.department = temp_model.from_map(m.get('Department'))

        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')

        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class ListClientUsersResponseBodyDataDataListDepartment(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

