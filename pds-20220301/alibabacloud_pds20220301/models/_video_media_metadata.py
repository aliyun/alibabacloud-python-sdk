# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class VideoMediaMetadata(DaraModel):
    def __init__(
        self,
        height: int = None,
        video_media_audio_stream: List[main_models.VideoMediaAudioStream] = None,
        video_media_video_stream: List[main_models.VideoMediaVideoStream] = None,
        width: int = None,
    ):
        # The height of the video image. Unit: pixel.
        self.height = height
        # The information about the audio stream.
        self.video_media_audio_stream = video_media_audio_stream
        # The information about the video stream.
        self.video_media_video_stream = video_media_video_stream
        # The width of the video image. Unit: pixel.
        self.width = width

    def validate(self):
        if self.video_media_audio_stream:
            for v1 in self.video_media_audio_stream:
                 if v1:
                    v1.validate()
        if self.video_media_video_stream:
            for v1 in self.video_media_video_stream:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['height'] = self.height

        result['video_media_audio_stream'] = []
        if self.video_media_audio_stream is not None:
            for k1 in self.video_media_audio_stream:
                result['video_media_audio_stream'].append(k1.to_map() if k1 else None)

        result['video_media_video_stream'] = []
        if self.video_media_video_stream is not None:
            for k1 in self.video_media_video_stream:
                result['video_media_video_stream'].append(k1.to_map() if k1 else None)

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')

        self.video_media_audio_stream = []
        if m.get('video_media_audio_stream') is not None:
            for k1 in m.get('video_media_audio_stream'):
                temp_model = main_models.VideoMediaAudioStream()
                self.video_media_audio_stream.append(temp_model.from_map(k1))

        self.video_media_video_stream = []
        if m.get('video_media_video_stream') is not None:
            for k1 in m.get('video_media_video_stream'):
                temp_model = main_models.VideoMediaVideoStream()
                self.video_media_video_stream.append(temp_model.from_map(k1))

        if m.get('width') is not None:
            self.width = m.get('width')

        return self

