# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ListDirectoryUsersResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        users: List[main_models.ListDirectoryUsersResponseBodyUsers] = None,
    ):
        # The token used to start the next query. If the value of this parameter is empty, all results are returned.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The usernames corresponding to the AD directory. If the AD directory contains only the Administrator and Guest accounts, the Users array will be empty.
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.ListDirectoryUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class ListDirectoryUsersResponseBodyUsers(DaraModel):
    def __init__(
        self,
        assigned_desktop_number: int = None,
        display_name: str = None,
        display_name_new: str = None,
        email: str = None,
        end_user: str = None,
        phone: str = None,
        user_principal_name: str = None,
    ):
        # The number of assigned cloud computers.
        self.assigned_desktop_number = assigned_desktop_number
        # The display name of the user.
        self.display_name = display_name
        self.display_name_new = display_name_new
        # The email address.
        self.email = email
        # The name of the user.
        self.end_user = end_user
        # The mobile number.
        self.phone = phone
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assigned_desktop_number is not None:
            result['AssignedDesktopNumber'] = self.assigned_desktop_number

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.display_name_new is not None:
            result['DisplayNameNew'] = self.display_name_new

        if self.email is not None:
            result['Email'] = self.email

        if self.end_user is not None:
            result['EndUser'] = self.end_user

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignedDesktopNumber') is not None:
            self.assigned_desktop_number = m.get('AssignedDesktopNumber')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('DisplayNameNew') is not None:
            self.display_name_new = m.get('DisplayNameNew')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndUser') is not None:
            self.end_user = m.get('EndUser')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

