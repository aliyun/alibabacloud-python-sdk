# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeDeviceChannelsResponseBody(DaraModel):
    def __init__(
        self,
        channels: List[main_models.DescribeDeviceChannelsResponseBodyChannels] = None,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.channels = channels
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.channels:
            for v1 in self.channels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Channels'] = []
        if self.channels is not None:
            for k1 in self.channels:
                result['Channels'].append(k1.to_map() if k1 else None)

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channels = []
        if m.get('Channels') is not None:
            for k1 in m.get('Channels'):
                temp_model = main_models.DescribeDeviceChannelsResponseBodyChannels()
                self.channels.append(temp_model.from_map(k1))

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDeviceChannelsResponseBodyChannels(DaraModel):
    def __init__(
        self,
        channel_id: int = None,
        device_id: str = None,
        device_status: str = None,
        gb_id: str = None,
        name: str = None,
        params: str = None,
        stream_id: str = None,
        stream_status: str = None,
    ):
        self.channel_id = channel_id
        self.device_id = device_id
        self.device_status = device_status
        self.gb_id = gb_id
        self.name = name
        self.params = params
        self.stream_id = stream_id
        self.stream_status = stream_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status

        if self.gb_id is not None:
            result['GbId'] = self.gb_id

        if self.name is not None:
            result['Name'] = self.name

        if self.params is not None:
            result['Params'] = self.params

        if self.stream_id is not None:
            result['StreamId'] = self.stream_id

        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')

        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')

        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')

        return self

