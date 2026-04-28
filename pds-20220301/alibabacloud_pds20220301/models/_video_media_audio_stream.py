# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VideoMediaAudioStream(DaraModel):
    def __init__(
        self,
        bit_rate: str = None,
        code_name: str = None,
        duration: str = None,
    ):
        # The bitrate of the audio stream. Unit: bit/s.
        self.bit_rate = bit_rate
        # The audio encoding mode.
        self.code_name = code_name
        # The duration of the audio stream. Unit: seconds.
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bit_rate is not None:
            result['bit_rate'] = self.bit_rate

        if self.code_name is not None:
            result['code_name'] = self.code_name

        if self.duration is not None:
            result['duration'] = self.duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bit_rate') is not None:
            self.bit_rate = m.get('bit_rate')

        if m.get('code_name') is not None:
            self.code_name = m.get('code_name')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        return self

