# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetCustomizedVoiceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetCustomizedVoiceResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetCustomizedVoiceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCustomizedVoiceResponseBodyData(DaraModel):
    def __init__(
        self,
        customized_voice: main_models.GetCustomizedVoiceResponseBodyDataCustomizedVoice = None,
    ):
        # The personalized human voice.
        self.customized_voice = customized_voice

    def validate(self):
        if self.customized_voice:
            self.customized_voice.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customized_voice is not None:
            result['CustomizedVoice'] = self.customized_voice.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomizedVoice') is not None:
            temp_model = main_models.GetCustomizedVoiceResponseBodyDataCustomizedVoice()
            self.customized_voice = temp_model.from_map(m.get('CustomizedVoice'))

        return self

class GetCustomizedVoiceResponseBodyDataCustomizedVoice(DaraModel):
    def __init__(
        self,
        demo_audio_media_id: str = None,
        gender: str = None,
        scenario: str = None,
        voice_desc: str = None,
        voice_id: str = None,
        voice_name: str = None,
    ):
        # The media asset ID of the sample audio file.
        self.demo_audio_media_id = demo_audio_media_id
        # The gender. Valid values:
        # 
        # *   female
        # *   male
        self.gender = gender
        # The demonstration scenario.
        # 
        # Valid values:
        # 
        # *   **story**
        # *   **interaction**
        # *   **navigation**
        self.scenario = scenario
        # The voice description.
        self.voice_desc = voice_desc
        # The voice ID.
        self.voice_id = voice_id
        # The voice name.
        self.voice_name = voice_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.demo_audio_media_id is not None:
            result['DemoAudioMediaId'] = self.demo_audio_media_id

        if self.gender is not None:
            result['Gender'] = self.gender

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        if self.voice_desc is not None:
            result['VoiceDesc'] = self.voice_desc

        if self.voice_id is not None:
            result['VoiceId'] = self.voice_id

        if self.voice_name is not None:
            result['VoiceName'] = self.voice_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DemoAudioMediaId') is not None:
            self.demo_audio_media_id = m.get('DemoAudioMediaId')

        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        if m.get('VoiceDesc') is not None:
            self.voice_desc = m.get('VoiceDesc')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        if m.get('VoiceName') is not None:
            self.voice_name = m.get('VoiceName')

        return self

