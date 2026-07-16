# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitCosyVoiceCustomizedVoiceJobRequest(DaraModel):
    def __init__(
        self,
        audios: str = None,
        demo_audio_media_url: str = None,
        gender: str = None,
        model: str = None,
        voice_name: str = None,
    ):
        # The media asset ID of the training audio material. Currently, only one audio material can be used for training.
        self.audios = audios
        # The sample audio output address.  
        # - If you specify this parameter, a sample audio file is generated at the specified OSS address after training succeeds.  
        # >Notice: The address must be a valid public OSS address under your account.
        self.demo_audio_media_url = demo_audio_media_url
        # The gender. Valid values:
        # - female
        # - male
        self.gender = gender
        # The voice cloning model. Valid values:
        # - **cosyvoice-v3-plus**
        # - **cosyvoice-v3-flash**
        # - **cosyvoice-v3.5-plus**
        # - **cosyvoice-v3.5-flash**
        self.model = model
        # The voice name. The name can be up to 32 characters in length.
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

        if self.demo_audio_media_url is not None:
            result['DemoAudioMediaURL'] = self.demo_audio_media_url

        if self.gender is not None:
            result['Gender'] = self.gender

        if self.model is not None:
            result['Model'] = self.model

        if self.voice_name is not None:
            result['VoiceName'] = self.voice_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audios') is not None:
            self.audios = m.get('Audios')

        if m.get('DemoAudioMediaURL') is not None:
            self.demo_audio_media_url = m.get('DemoAudioMediaURL')

        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('VoiceName') is not None:
            self.voice_name = m.get('VoiceName')

        return self

