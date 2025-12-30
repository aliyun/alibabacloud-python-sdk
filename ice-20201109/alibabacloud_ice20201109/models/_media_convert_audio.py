# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MediaConvertAudio(DaraModel):
    def __init__(
        self,
        bitrate: int = None,
        channels: int = None,
        codec: str = None,
        profile: str = None,
        remove: bool = None,
        samplerate: str = None,
    ):
        self.bitrate = bitrate
        self.channels = channels
        self.codec = codec
        self.profile = profile
        self.remove = remove
        self.samplerate = samplerate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.channels is not None:
            result['Channels'] = self.channels

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.remove is not None:
            result['Remove'] = self.remove

        if self.samplerate is not None:
            result['Samplerate'] = self.samplerate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Remove') is not None:
            self.remove = m.get('Remove')

        if m.get('Samplerate') is not None:
            self.samplerate = m.get('Samplerate')

        return self

