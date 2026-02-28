# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeChannelAllUsersResponseBody(DaraModel):
    def __init__(
        self,
        channel_exist: bool = None,
        request_id: str = None,
        users: List[main_models.DescribeChannelAllUsersResponseBodyUsers] = None,
    ):
        self.channel_exist = channel_exist
        self.request_id = request_id
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
        if self.channel_exist is not None:
            result['ChannelExist'] = self.channel_exist

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelExist') is not None:
            self.channel_exist = m.get('ChannelExist')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.DescribeChannelAllUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class DescribeChannelAllUsersResponseBodyUsers(DaraModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

