# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomizedVoiceJobRequest(DaraModel):
    def __init__(
        self,
        gender: str = None,
        scenario: str = None,
        voice_desc: str = None,
        voice_id: str = None,
        voice_name: str = None,
    ):
        # The gender. Valid values:
        # 
        # *   female
        # *   male
        # 
        # This parameter is required.
        self.gender = gender
        # The scenario. Valid values:
        # 
        # *   story
        # *   interaction
        # *   navigation
        # 
        # This parameter is required.
        self.scenario = scenario
        # The voice description.
        # 
        # *   The description can be up to 256 characters in length.
        self.voice_desc = voice_desc
        # The voice ID. It can be the English name or Chinese Pinyin of the voice.
        # 
        # *   The value must be a unique ID that is not used by other custom voices.
        # *   The ID can be up to 32 characters in length.
        # *   Only letters and digits are supported.
        # 
        # This parameter is required.
        self.voice_id = voice_id
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

