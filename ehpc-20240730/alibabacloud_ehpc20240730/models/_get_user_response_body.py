# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class GetUserResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user: main_models.GetUserResponseBodyUser = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The user details.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user is not None:
            result['User'] = self.user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('User') is not None:
            temp_model = main_models.GetUserResponseBodyUser()
            self.user = temp_model.from_map(m.get('User'))

        return self

class GetUserResponseBodyUser(DaraModel):
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
        # The user group. Valid values:
        # 
        # - users: ordinary permission group. This group is suitable for regular users who only need to commit and debug jobs.
        # 
        # - wheel: sudo permission group. This group is suitable for administrators who need cluster management. In addition to committing and debugging jobs, members of this group can execute sudo commands to install software, restart nodes, and perform other operations.
        self.group = group
        # The user group ID.
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

