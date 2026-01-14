# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VoiceModelResponse(DaraModel):
    def __init__(
        self,
        resource_type_desc: str = None,
        tts_version: int = None,
        use_scene: str = None,
        voice_desc: str = None,
        voice_gender: str = None,
        voice_id: int = None,
        voice_language: str = None,
        voice_model: str = None,
        voice_name: str = None,
        voice_type: str = None,
        voice_url: str = None,
    ):
        self.resource_type_desc = resource_type_desc
        self.tts_version = tts_version
        self.use_scene = use_scene
        self.voice_desc = voice_desc
        self.voice_gender = voice_gender
        self.voice_id = voice_id
        self.voice_language = voice_language
        self.voice_model = voice_model
        self.voice_name = voice_name
        self.voice_type = voice_type
        self.voice_url = voice_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type_desc is not None:
            result['resourceTypeDesc'] = self.resource_type_desc

        if self.tts_version is not None:
            result['ttsVersion'] = self.tts_version

        if self.use_scene is not None:
            result['useScene'] = self.use_scene

        if self.voice_desc is not None:
            result['voiceDesc'] = self.voice_desc

        if self.voice_gender is not None:
            result['voiceGender'] = self.voice_gender

        if self.voice_id is not None:
            result['voiceId'] = self.voice_id

        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language

        if self.voice_model is not None:
            result['voiceModel'] = self.voice_model

        if self.voice_name is not None:
            result['voiceName'] = self.voice_name

        if self.voice_type is not None:
            result['voiceType'] = self.voice_type

        if self.voice_url is not None:
            result['voiceUrl'] = self.voice_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceTypeDesc') is not None:
            self.resource_type_desc = m.get('resourceTypeDesc')

        if m.get('ttsVersion') is not None:
            self.tts_version = m.get('ttsVersion')

        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')

        if m.get('voiceDesc') is not None:
            self.voice_desc = m.get('voiceDesc')

        if m.get('voiceGender') is not None:
            self.voice_gender = m.get('voiceGender')

        if m.get('voiceId') is not None:
            self.voice_id = m.get('voiceId')

        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')

        if m.get('voiceModel') is not None:
            self.voice_model = m.get('voiceModel')

        if m.get('voiceName') is not None:
            self.voice_name = m.get('voiceName')

        if m.get('voiceType') is not None:
            self.voice_type = m.get('voiceType')

        if m.get('voiceUrl') is not None:
            self.voice_url = m.get('voiceUrl')

        return self

