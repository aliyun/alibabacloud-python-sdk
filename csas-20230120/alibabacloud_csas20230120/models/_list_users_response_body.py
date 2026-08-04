# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListUsersResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_num: str = None,
        users: List[main_models.ListUsersResponseBodyUsers] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of users.
        self.total_num = total_num
        # An array of user objects.
        self.users = users

    def validate(self):
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.ListUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class ListUsersResponseBodyUsers(DaraModel):
    def __init__(
        self,
        department: str = None,
        email: str = None,
        full_department: List[str] = None,
        idp_name: str = None,
        phone: str = None,
        sase_user_id: str = None,
        status: str = None,
        username: str = None,
    ):
        # The user\\"s department.
        self.department = department
        # The user\\"s email address.
        self.email = email
        # A list of full department paths.
        self.full_department = full_department
        # The name of the Identity Provider (IdP).
        self.idp_name = idp_name
        # The user\\"s phone number.
        self.phone = phone
        # The user ID.
        self.sase_user_id = sase_user_id
        # The user status.
        self.status = status
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department is not None:
            result['Department'] = self.department

        if self.email is not None:
            result['Email'] = self.email

        if self.full_department is not None:
            result['FullDepartment'] = self.full_department

        if self.idp_name is not None:
            result['IdpName'] = self.idp_name

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.status is not None:
            result['Status'] = self.status

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('FullDepartment') is not None:
            self.full_department = m.get('FullDepartment')

        if m.get('IdpName') is not None:
            self.idp_name = m.get('IdpName')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

