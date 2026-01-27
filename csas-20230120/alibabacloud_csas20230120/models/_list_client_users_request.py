# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClientUsersRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        department_id: str = None,
        email: str = None,
        idp_config_id: str = None,
        mobile_number: str = None,
        page_size: int = None,
        status: str = None,
        username: str = None,
    ):
        self.current_page = current_page
        self.department_id = department_id
        self.email = email
        # This parameter is required.
        self.idp_config_id = idp_config_id
        self.mobile_number = mobile_number
        self.page_size = page_size
        self.status = status
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.email is not None:
            result['Email'] = self.email

        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id

        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')

        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

