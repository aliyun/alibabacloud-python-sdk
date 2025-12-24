# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class CheckLiveMessageUsersInGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        users: List[main_models.CheckLiveMessageUsersInGroupResponseBodyUsers] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of users queried.
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

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.CheckLiveMessageUsersInGroupResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class CheckLiveMessageUsersInGroupResponseBodyUsers(DaraModel):
    def __init__(
        self,
        online: bool = None,
        user_id: str = None,
    ):
        # Indicates whether the user is in the group.
        self.online = online
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.online is not None:
            result['Online'] = self.online

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

