# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class ListUsersResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        users: main_models.ListUsersResponseBodyUsers = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The information about the users.
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.users is not None:
            result['Users'] = self.users.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Users') is not None:
            temp_model = main_models.ListUsersResponseBodyUsers()
            self.users = temp_model.from_map(m.get('Users'))

        return self

class ListUsersResponseBodyUsers(DaraModel):
    def __init__(
        self,
        user_info: List[main_models.ListUsersResponseBodyUsersUserInfo] = None,
    ):
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            for v1 in self.user_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserInfo'] = []
        if self.user_info is not None:
            for k1 in self.user_info:
                result['UserInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_info = []
        if m.get('UserInfo') is not None:
            for k1 in m.get('UserInfo'):
                temp_model = main_models.ListUsersResponseBodyUsersUserInfo()
                self.user_info.append(temp_model.from_map(k1))

        return self

class ListUsersResponseBodyUsersUserInfo(DaraModel):
    def __init__(
        self,
        add_time: str = None,
        group: str = None,
        group_id: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The time when the user was first added.
        self.add_time = add_time
        # The name of the permission group. Valid values:
        # 
        # users: ordinary permissions, which are suitable for regular users that need only to submit and debug jobs.
        # 
        # wheel: sudo permissions, which are suitable for administrators who need to manage clusters. In addition to submitting and debugging jobs, you can also run sudo commands to install software and restart nodes.
        self.group = group
        # The permission group ID.
        self.group_id = group_id
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_time is not None:
            result['AddTime'] = self.add_time

        if self.group is not None:
            result['Group'] = self.group

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

