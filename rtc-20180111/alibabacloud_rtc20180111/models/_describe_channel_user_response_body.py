# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeChannelUserResponseBody(DaraModel):
    def __init__(
        self,
        channel_exist: bool = None,
        in_channel: bool = None,
        request_id: str = None,
        sessions: List[main_models.DescribeChannelUserResponseBodySessions] = None,
    ):
        self.channel_exist = channel_exist
        self.in_channel = in_channel
        self.request_id = request_id
        self.sessions = sessions

    def validate(self):
        if self.sessions:
            for v1 in self.sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_exist is not None:
            result['ChannelExist'] = self.channel_exist

        if self.in_channel is not None:
            result['InChannel'] = self.in_channel

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['Sessions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelExist') is not None:
            self.channel_exist = m.get('ChannelExist')

        if m.get('InChannel') is not None:
            self.in_channel = m.get('InChannel')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.DescribeChannelUserResponseBodySessions()
                self.sessions.append(temp_model.from_map(k1))

        return self

class DescribeChannelUserResponseBodySessions(DaraModel):
    def __init__(
        self,
        joined: int = None,
        session_id: str = None,
        user_id: str = None,
    ):
        self.joined = joined
        self.session_id = session_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.joined is not None:
            result['Joined'] = self.joined

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Joined') is not None:
            self.joined = m.get('Joined')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

