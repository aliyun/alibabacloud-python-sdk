# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class ListVoiceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        voice_list: List[main_models.ListVoiceResponseBodyVoiceList] = None,
    ):
        self.request_id = request_id
        self.voice_list = voice_list

    def validate(self):
        if self.voice_list:
            for v1 in self.voice_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VoiceList'] = []
        if self.voice_list is not None:
            for k1 in self.voice_list:
                result['VoiceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.voice_list = []
        if m.get('VoiceList') is not None:
            for k1 in m.get('VoiceList'):
                temp_model = main_models.ListVoiceResponseBodyVoiceList()
                self.voice_list.append(temp_model.from_map(k1))

        return self

class ListVoiceResponseBodyVoiceList(DaraModel):
    def __init__(
        self,
        gender: str = None,
        illustration: str = None,
        illustration_audio: str = None,
        language: str = None,
        model_id: str = None,
        name: str = None,
        voice: str = None,
    ):
        self.gender = gender
        self.illustration = illustration
        self.illustration_audio = illustration_audio
        self.language = language
        self.model_id = model_id
        self.name = name
        self.voice = voice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gender is not None:
            result['Gender'] = self.gender

        if self.illustration is not None:
            result['Illustration'] = self.illustration

        if self.illustration_audio is not None:
            result['IllustrationAudio'] = self.illustration_audio

        if self.language is not None:
            result['Language'] = self.language

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.name is not None:
            result['Name'] = self.name

        if self.voice is not None:
            result['Voice'] = self.voice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('Illustration') is not None:
            self.illustration = m.get('Illustration')

        if m.get('IllustrationAudio') is not None:
            self.illustration_audio = m.get('IllustrationAudio')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        return self

