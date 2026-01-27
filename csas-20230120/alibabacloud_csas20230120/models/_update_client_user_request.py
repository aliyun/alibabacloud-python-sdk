# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateClientUserRequest(DaraModel):
    def __init__(
        self,
        department_id: str = None,
        description: str = None,
        email: str = None,
        id: str = None,
        mobile_number: str = None,
    ):
        self.department_id = department_id
        self.description = description
        self.email = email
        # This parameter is required.
        self.id = id
        self.mobile_number = mobile_number

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

        if self.id is not None:
            result['Id'] = self.id

        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')

        return self

