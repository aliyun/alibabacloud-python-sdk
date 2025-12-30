# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitStandardCustomizedVoiceJobRequest(DaraModel):
    def __init__(
        self,
        audios: str = None,
        authentication: str = None,
        demo_audio_media_url: str = None,
        gender: str = None,
        voice_name: str = None,
    ):
        # *   The material assets IDs of the materials for training.
        # *   Separate multiple media IDs with commas (,).
        # 
        # > : The total duration of all materials must be within 15 to 30 minutes. The duration of each material must be greater than 1 minute.
        self.audios = audios
        # *   The media asset ID of the authentication audio.
        # 
        # *   Upload an audio file for identity authentication. If the voiceprint extracted from the uploaded file differs from that of the training file, the job fails.
        # 
        #     **
        # 
        #     **Note**: Clearly read and record the following text: I confirm to customize human voice cloning and provide audio files that contain my voice for training. I promise that I am responsible for the customized content and that the content complies with laws and regulations.
        self.authentication = authentication
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
        # The gender. Valid values:
        # 
        # *   female
        # *   male
        self.gender = gender
        # The voice name.
        # 
        # *   The name can be up to 32 characters in length.
        self.voice_name = voice_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audios is not None:
            result['Audios'] = self.audios

        if self.authentication is not None:
            result['Authentication'] = self.authentication

        if self.demo_audio_media_url is not None:
            result['DemoAudioMediaURL'] = self.demo_audio_media_url

        if self.gender is not None:
            result['Gender'] = self.gender

        if self.voice_name is not None:
            result['VoiceName'] = self.voice_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audios') is not None:
            self.audios = m.get('Audios')

        if m.get('Authentication') is not None:
            self.authentication = m.get('Authentication')

        if m.get('DemoAudioMediaURL') is not None:
            self.demo_audio_media_url = m.get('DemoAudioMediaURL')

        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('VoiceName') is not None:
            self.voice_name = m.get('VoiceName')

        return self

