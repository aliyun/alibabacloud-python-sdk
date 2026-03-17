# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeUserOnlineClientsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        users: main_models.DescribeUserOnlineClientsResponseBodyUsers = None,
    ):
        # The ID of the request.
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.users is not None:
            result['Users'] = self.users.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Users') is not None:
            temp_model = main_models.DescribeUserOnlineClientsResponseBodyUsers()
            self.users = temp_model.from_map(m.get('Users'))

        return self

class DescribeUserOnlineClientsResponseBodyUsers(DaraModel):
    def __init__(
        self,
        user: List[main_models.DescribeUserOnlineClientsResponseBodyUsersUser] = None,
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
                temp_model = main_models.DescribeUserOnlineClientsResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k1))

        return self

class DescribeUserOnlineClientsResponseBodyUsersUser(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        online_time: str = None,
    ):
        self.client_ip = client_ip
        self.online_time = online_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.online_time is not None:
            result['OnlineTime'] = self.online_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('OnlineTime') is not None:
            self.online_time = m.get('OnlineTime')

        return self

