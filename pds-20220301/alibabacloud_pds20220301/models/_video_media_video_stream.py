# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VideoMediaVideoStream(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        code_name: str = None,
        duration: str = None,
        frame_count: str = None,
    ):
        # The bitrate of the video stream. Unit: bit/s.
        self.bitrate = bitrate
        # The video encoding mode.
        self.code_name = code_name
        # The duration of the video stream. Unit: seconds.
        self.duration = duration
        # The number of video frames.
        self.frame_count = frame_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['bitrate'] = self.bitrate

        if self.code_name is not None:
            result['code_name'] = self.code_name

        if self.duration is not None:
            result['duration'] = self.duration

        if self.frame_count is not None:
            result['frame_count'] = self.frame_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bitrate') is not None:
            self.bitrate = m.get('bitrate')

        if m.get('code_name') is not None:
            self.code_name = m.get('code_name')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('frame_count') is not None:
            self.frame_count = m.get('frame_count')

        return self

