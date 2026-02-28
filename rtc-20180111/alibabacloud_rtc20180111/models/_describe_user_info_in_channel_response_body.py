# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeUserInfoInChannelResponseBody(DaraModel):
    def __init__(
        self,
        is_channel_exist: bool = None,
        is_in_channel: bool = None,
        property: List[main_models.DescribeUserInfoInChannelResponseBodyProperty] = None,
        request_id: str = None,
        timestamp: int = None,
    ):
        self.is_channel_exist = is_channel_exist
        self.is_in_channel = is_in_channel
        self.property = property
        self.request_id = request_id
        self.timestamp = timestamp

    def validate(self):
        if self.property:
            for v1 in self.property:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_channel_exist is not None:
            result['IsChannelExist'] = self.is_channel_exist

        if self.is_in_channel is not None:
            result['IsInChannel'] = self.is_in_channel

        result['Property'] = []
        if self.property is not None:
            for k1 in self.property:
                result['Property'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsChannelExist') is not None:
            self.is_channel_exist = m.get('IsChannelExist')

        if m.get('IsInChannel') is not None:
            self.is_in_channel = m.get('IsInChannel')

        self.property = []
        if m.get('Property') is not None:
            for k1 in m.get('Property'):
                temp_model = main_models.DescribeUserInfoInChannelResponseBodyProperty()
                self.property.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class DescribeUserInfoInChannelResponseBodyProperty(DaraModel):
    def __init__(
        self,
        join: int = None,
        role: int = None,
        session: str = None,
    ):
        self.join = join
        self.role = role
        self.session = session

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.join is not None:
            result['Join'] = self.join

        if self.role is not None:
            result['Role'] = self.role

        if self.session is not None:
            result['Session'] = self.session

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Join') is not None:
            self.join = m.get('Join')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Session') is not None:
            self.session = m.get('Session')

        return self

