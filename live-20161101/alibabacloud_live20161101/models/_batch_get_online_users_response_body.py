# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class BatchGetOnlineUsersResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.BatchGetOnlineUsersResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.BatchGetOnlineUsersResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class BatchGetOnlineUsersResponseBodyResult(DaraModel):
    def __init__(
        self,
        online_users: List[main_models.BatchGetOnlineUsersResponseBodyResultOnlineUsers] = None,
    ):
        # The information about users.
        self.online_users = online_users

    def validate(self):
        if self.online_users:
            for v1 in self.online_users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OnlineUsers'] = []
        if self.online_users is not None:
            for k1 in self.online_users:
                result['OnlineUsers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.online_users = []
        if m.get('OnlineUsers') is not None:
            for k1 in m.get('OnlineUsers'):
                temp_model = main_models.BatchGetOnlineUsersResponseBodyResultOnlineUsers()
                self.online_users.append(temp_model.from_map(k1))

        return self

class BatchGetOnlineUsersResponseBodyResultOnlineUsers(DaraModel):
    def __init__(
        self,
        join_time: int = None,
        online: bool = None,
        user_id: str = None,
    ):
        # The time when the user joined the group. The value is a UTC timestamp. Unit: milliseconds.
        self.join_time = join_time
        # Indicates whether the user is online. Valid values:
        # 
        # *   **true**
        # *   **false**
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
        if self.join_time is not None:
            result['JoinTime'] = self.join_time

        if self.online is not None:
            result['Online'] = self.online

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

