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
        # The URL of the sample audio file.
        # 
        # *   If this parameter is specified, a sample audio file is generated at the specified Object Storage Service (OSS) URL after the training is complete.
        # 
        # *   If this parameter is not specified, no sample audio file is generated.
        # 
        #     **
        # 
        #     **Note**: The URL must be a valid public OSS URL within your Alibaba Cloud account.
        self.demo_audio_media_url = demo_audio_media_url
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

