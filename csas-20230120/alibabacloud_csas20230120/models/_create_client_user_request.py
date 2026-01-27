# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClientUserRequest(DaraModel):
    def __init__(
        self,
        department_id: str = None,
        description: str = None,
        email: str = None,
        idp_config_id: str = None,
        mobile_number: str = None,
        password: str = None,
        username: str = None,
    ):
        self.department_id = department_id
        self.description = description
        # This parameter is required.
        self.email = email
        # This parameter is required.
        self.idp_config_id = idp_config_id
        self.mobile_number = mobile_number
        self.password = password
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.description is not None:
            result['Description'] = self.description

        if self.email is not None:
            result['Email'] = self.email

        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id

        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number

        if self.password is not None:
            result['Password'] = self.password

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')

        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

