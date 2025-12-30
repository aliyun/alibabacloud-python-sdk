# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCustomizedVoiceRequest(DaraModel):
    def __init__(
        self,
        demo_audio_media_id: str = None,
        voice_id: str = None,
    ):
        # The media asset ID of the sample audio file.
        self.demo_audio_media_id = demo_audio_media_id
        # The voice ID.
        # 
        # This parameter is required.
        self.voice_id = voice_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.demo_audio_media_id is not None:
            result['DemoAudioMediaId'] = self.demo_audio_media_id

        if self.voice_id is not None:
            result['VoiceId'] = self.voice_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DemoAudioMediaId') is not None:
            self.demo_audio_media_id = m.get('DemoAudioMediaId')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        return self

