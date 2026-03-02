# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListUsersForGroupResponseBody(DaraModel):
    def __init__(
        self,
        is_truncated: bool = None,
        marker: str = None,
        request_id: str = None,
        users: main_models.ListUsersForGroupResponseBodyUsers = None,
    ):
        self.is_truncated = is_truncated
        self.marker = marker
        self.request_id = request_id
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.users is not None:
            result['Users'] = self.users.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Users') is not None:
            temp_model = main_models.ListUsersForGroupResponseBodyUsers()
            self.users = temp_model.from_map(m.get('Users'))

        return self

class ListUsersForGroupResponseBodyUsers(DaraModel):
    def __init__(
        self,
        user: List[main_models.ListUsersForGroupResponseBodyUsersUser] = None,
    ):
        self.user = user

    def validate(self):
        if self.user:
            for v1 in self.user:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['User'] = []
        if self.user is not None:
            for k1 in self.user:
                result['User'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k1 in m.get('User'):
                temp_model = main_models.ListUsersForGroupResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k1))

        return self

class ListUsersForGroupResponseBodyUsersUser(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        join_date: str = None,
        user_id: str = None,
        user_principal_name: str = None,
    ):
        self.display_name = display_name
        self.join_date = join_date
        self.user_id = user_id
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.join_date is not None:
            result['JoinDate'] = self.join_date

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('JoinDate') is not None:
            self.join_date = m.get('JoinDate')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

