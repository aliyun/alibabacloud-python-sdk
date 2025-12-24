# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeCasterChannelsResponseBody(DaraModel):
    def __init__(
        self,
        channels: main_models.DescribeCasterChannelsResponseBodyChannels = None,
        request_id: str = None,
        total: int = None,
    ):
        # The channels.
        self.channels = channels
        # The request ID.
        self.request_id = request_id
        # The total number of channels.
        self.total = total

    def validate(self):
        if self.channels:
            self.channels.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            temp_model = main_models.DescribeCasterChannelsResponseBodyChannels()
            self.channels = temp_model.from_map(m.get('Channels'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeCasterChannelsResponseBodyChannels(DaraModel):
    def __init__(
        self,
        channel: List[main_models.DescribeCasterChannelsResponseBodyChannelsChannel] = None,
    ):
        self.channel = channel

    def validate(self):
        if self.channel:
            for v1 in self.channel:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Channel'] = []
        if self.channel is not None:
            for k1 in self.channel:
                result['Channel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channel = []
        if m.get('Channel') is not None:
            for k1 in m.get('Channel'):
                temp_model = main_models.DescribeCasterChannelsResponseBodyChannelsChannel()
                self.channel.append(temp_model.from_map(k1))

        return self

class DescribeCasterChannelsResponseBodyChannelsChannel(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        face_beauty: str = None,
        resource_id: str = None,
        rtmp_url: str = None,
        stream_url: str = None,
    ):
        # The ID of the channel.
        # 
        # The layout references the channel ID when the channel is enabled. You can specify up to one video resource for the channel. The value of this parameter must be in the RV[Number] format, such as RV01 and RV12.
        self.channel_id = channel_id
        # The face retouching effect. Valid values: 0 (all effects), 1 (skin smoothing), 2 (skin whitening), 3 (dark circles removal), and 4 (nasolabial folds removal).
        self.face_beauty = face_beauty
        # The ID of the video resource.
        self.resource_id = resource_id
        # The URL in the Real-Time Messaging Protocol (RTMP) format.
        self.rtmp_url = rtmp_url
        # The URL of the output content in the channel.
        self.stream_url = stream_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.face_beauty is not None:
            result['FaceBeauty'] = self.face_beauty

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.rtmp_url is not None:
            result['RtmpUrl'] = self.rtmp_url

        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('FaceBeauty') is not None:
            self.face_beauty = m.get('FaceBeauty')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('RtmpUrl') is not None:
            self.rtmp_url = m.get('RtmpUrl')

        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')

        return self

