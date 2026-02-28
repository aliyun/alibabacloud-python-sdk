# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeChannelResponseBody(DaraModel):
    def __init__(
        self,
        channel: main_models.DescribeChannelResponseBodyChannel = None,
        channel_exist: bool = None,
        request_id: str = None,
    ):
        # channel
        self.channel = channel
        self.channel_exist = channel_exist
        self.request_id = request_id

    def validate(self):
        if self.channel:
            self.channel.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel.to_map()

        if self.channel_exist is not None:
            result['ChannelExist'] = self.channel_exist

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            temp_model = main_models.DescribeChannelResponseBodyChannel()
            self.channel = temp_model.from_map(m.get('Channel'))

        if m.get('ChannelExist') is not None:
            self.channel_exist = m.get('ChannelExist')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeChannelResponseBodyChannel(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        start_time: int = None,
    ):
        self.channel_id = channel_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

