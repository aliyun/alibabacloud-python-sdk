# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitCustomizedVoiceJobRequest(DaraModel):
    def __init__(
        self,
        demo_audio_media_url: str = None,
        voice_id: str = None,
    ):
        # The OSS URL where the demo audio will be saved.
        # 
        # - If specified, the service generates a demo audio file at the provided OSS URL after training completes.
        # 
        # - >Notice: 
        # 
        #   The URL must be a valid public address for an OSS object in your account.
        self.demo_audio_media_url = demo_audio_media_url
        # The unique identifier for the voice.
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
        if self.demo_audio_media_url is not None:
            result['DemoAudioMediaURL'] = self.demo_audio_media_url

        if self.voice_id is not None:
            result['VoiceId'] = self.voice_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DemoAudioMediaURL') is not None:
            self.demo_audio_media_url = m.get('DemoAudioMediaURL')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        return self

