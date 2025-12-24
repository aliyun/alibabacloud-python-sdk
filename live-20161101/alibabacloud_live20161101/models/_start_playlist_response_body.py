# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class StartPlaylistResponseBody(DaraModel):
    def __init__(
        self,
        program_id: str = None,
        request_id: str = None,
        stream_info: main_models.StartPlaylistResponseBodyStreamInfo = None,
    ):
        # The ID of the episode list. You can use the ID as a request parameter in the API operation that is used to stop playing the episode list.
        self.program_id = program_id
        # The request ID.
        self.request_id = request_id
        # The information about the live stream.
        self.stream_info = stream_info

    def validate(self):
        if self.stream_info:
            self.stream_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.program_id is not None:
            result['ProgramId'] = self.program_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stream_info is not None:
            result['StreamInfo'] = self.stream_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProgramId') is not None:
            self.program_id = m.get('ProgramId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamInfo') is not None:
            temp_model = main_models.StartPlaylistResponseBodyStreamInfo()
            self.stream_info = temp_model.from_map(m.get('StreamInfo'))

        return self

class StartPlaylistResponseBodyStreamInfo(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        stream_name: str = None,
        streams: main_models.StartPlaylistResponseBodyStreamInfoStreams = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The main streaming domain.
        self.domain_name = domain_name
        # The name of the live stream.
        self.stream_name = stream_name
        # The streaming URLs.
        self.streams = streams

    def validate(self):
        if self.streams:
            self.streams.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.streams is not None:
            result['Streams'] = self.streams.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('Streams') is not None:
            temp_model = main_models.StartPlaylistResponseBodyStreamInfoStreams()
            self.streams = temp_model.from_map(m.get('Streams'))

        return self

class StartPlaylistResponseBodyStreamInfoStreams(DaraModel):
    def __init__(
        self,
        stream: List[main_models.StartPlaylistResponseBodyStreamInfoStreamsStream] = None,
    ):
        self.stream = stream

    def validate(self):
        if self.stream:
            for v1 in self.stream:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Stream'] = []
        if self.stream is not None:
            for k1 in self.stream:
                result['Stream'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stream = []
        if m.get('Stream') is not None:
            for k1 in m.get('Stream'):
                temp_model = main_models.StartPlaylistResponseBodyStreamInfoStreamsStream()
                self.stream.append(temp_model.from_map(k1))

        return self

class StartPlaylistResponseBodyStreamInfoStreamsStream(DaraModel):
    def __init__(
        self,
        pull_flv_url: str = None,
        pull_m3u8url: str = None,
        pull_rtmp_url: str = None,
        quality: str = None,
    ):
        # The streaming URL in the Flash Video (FLV) format.
        self.pull_flv_url = pull_flv_url
        # The streaming URL in the Real-Time Messaging Protocol (RTMP) format.
        self.pull_m3u8url = pull_m3u8url
        # The streaming URL in the M3U8 format.
        self.pull_rtmp_url = pull_rtmp_url
        # The video quality of the live stream. Valid values: **original**: original quality
        self.quality = quality

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pull_flv_url is not None:
            result['PullFlvUrl'] = self.pull_flv_url

        if self.pull_m3u8url is not None:
            result['PullM3U8Url'] = self.pull_m3u8url

        if self.pull_rtmp_url is not None:
            result['PullRtmpUrl'] = self.pull_rtmp_url

        if self.quality is not None:
            result['Quality'] = self.quality

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PullFlvUrl') is not None:
            self.pull_flv_url = m.get('PullFlvUrl')

        if m.get('PullM3U8Url') is not None:
            self.pull_m3u8url = m.get('PullM3U8Url')

        if m.get('PullRtmpUrl') is not None:
            self.pull_rtmp_url = m.get('PullRtmpUrl')

        if m.get('Quality') is not None:
            self.quality = m.get('Quality')

        return self

