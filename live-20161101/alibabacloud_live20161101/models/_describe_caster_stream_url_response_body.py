# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeCasterStreamUrlResponseBody(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        caster_streams: main_models.DescribeCasterStreamUrlResponseBodyCasterStreams = None,
        request_id: str = None,
        total: int = None,
    ):
        # The ID of the production studio.
        self.caster_id = caster_id
        # The information about the streams of the production studio.
        self.caster_streams = caster_streams
        # The ID of the request.
        self.request_id = request_id
        # The number of streams that were returned.
        self.total = total

    def validate(self):
        if self.caster_streams:
            self.caster_streams.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.caster_streams is not None:
            result['CasterStreams'] = self.caster_streams.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('CasterStreams') is not None:
            temp_model = main_models.DescribeCasterStreamUrlResponseBodyCasterStreams()
            self.caster_streams = temp_model.from_map(m.get('CasterStreams'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeCasterStreamUrlResponseBodyCasterStreams(DaraModel):
    def __init__(
        self,
        caster_stream: List[main_models.DescribeCasterStreamUrlResponseBodyCasterStreamsCasterStream] = None,
    ):
        self.caster_stream = caster_stream

    def validate(self):
        if self.caster_stream:
            for v1 in self.caster_stream:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CasterStream'] = []
        if self.caster_stream is not None:
            for k1 in self.caster_stream:
                result['CasterStream'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.caster_stream = []
        if m.get('CasterStream') is not None:
            for k1 in m.get('CasterStream'):
                temp_model = main_models.DescribeCasterStreamUrlResponseBodyCasterStreamsCasterStream()
                self.caster_stream.append(temp_model.from_map(k1))

        return self

class DescribeCasterStreamUrlResponseBodyCasterStreamsCasterStream(DaraModel):
    def __init__(
        self,
        output_type: int = None,
        rtmp_url: str = None,
        scene_id: str = None,
        stream_infos: main_models.DescribeCasterStreamUrlResponseBodyCasterStreamsCasterStreamStreamInfos = None,
        stream_url: str = None,
    ):
        # Indicates whether the output stream is in preview mode or program mode.
        # 
        # *   **0**: indicates that the output videos of the scene are in preview mode.
        # *   **1**: indicates that the output videos of the scene are in program mode.
        self.output_type = output_type
        # The Real Time Messaging Protocol (RTMP) URL.
        self.rtmp_url = rtmp_url
        # The ID of the scene.
        self.scene_id = scene_id
        # The information about the stream.
        self.stream_infos = stream_infos
        # The streaming URL.
        self.stream_url = stream_url

    def validate(self):
        if self.stream_infos:
            self.stream_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_type is not None:
            result['OutputType'] = self.output_type

        if self.rtmp_url is not None:
            result['RtmpUrl'] = self.rtmp_url

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.stream_infos is not None:
            result['StreamInfos'] = self.stream_infos.to_map()

        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        if m.get('RtmpUrl') is not None:
            self.rtmp_url = m.get('RtmpUrl')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('StreamInfos') is not None:
            temp_model = main_models.DescribeCasterStreamUrlResponseBodyCasterStreamsCasterStreamStreamInfos()
            self.stream_infos = temp_model.from_map(m.get('StreamInfos'))

        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')

        return self

class DescribeCasterStreamUrlResponseBodyCasterStreamsCasterStreamStreamInfos(DaraModel):
    def __init__(
        self,
        stream_info: List[main_models.DescribeCasterStreamUrlResponseBodyCasterStreamsCasterStreamStreamInfosStreamInfo] = None,
    ):
        self.stream_info = stream_info

    def validate(self):
        if self.stream_info:
            for v1 in self.stream_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StreamInfo'] = []
        if self.stream_info is not None:
            for k1 in self.stream_info:
                result['StreamInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stream_info = []
        if m.get('StreamInfo') is not None:
            for k1 in m.get('StreamInfo'):
                temp_model = main_models.DescribeCasterStreamUrlResponseBodyCasterStreamsCasterStreamStreamInfosStreamInfo()
                self.stream_info.append(temp_model.from_map(k1))

        return self

class DescribeCasterStreamUrlResponseBodyCasterStreamsCasterStreamStreamInfosStreamInfo(DaraModel):
    def __init__(
        self,
        output_stream_url: str = None,
        transcode_config: str = None,
        video_format: str = None,
    ):
        # The streaming URL.
        self.output_stream_url = output_stream_url
        # The resolution to which the scene transcodes the stream for playback. Valid values:
        # 
        # *   **lsd**: standard definition.
        # *   **lld**: low definition.
        # *   **lud**: ultra high definition.
        # *   **lhd**: high definition.
        self.transcode_config = transcode_config
        # The format to which the scene transcodes the stream for playback. Valid values:
        # 
        # *   **flv**.
        # *   **rtmp**.
        # *   **m3u8**.
        self.video_format = video_format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_stream_url is not None:
            result['OutputStreamUrl'] = self.output_stream_url

        if self.transcode_config is not None:
            result['TranscodeConfig'] = self.transcode_config

        if self.video_format is not None:
            result['VideoFormat'] = self.video_format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputStreamUrl') is not None:
            self.output_stream_url = m.get('OutputStreamUrl')

        if m.get('TranscodeConfig') is not None:
            self.transcode_config = m.get('TranscodeConfig')

        if m.get('VideoFormat') is not None:
            self.video_format = m.get('VideoFormat')

        return self

