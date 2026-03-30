# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class PreviewVoiceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        model: str = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        params: main_models.PreviewVoiceRequestParams = None,
        text: str = None,
        voice: str = None,
    ):
        self.instance_id = instance_id
        self.model = model
        self.nls_access_type = nls_access_type
        self.nls_engine = nls_engine
        self.params = params
        self.text = text
        self.voice = voice

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.model is not None:
            result['Model'] = self.model

        if self.nls_access_type is not None:
            result['NlsAccessType'] = self.nls_access_type

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        if self.params is not None:
            result['Params'] = self.params.to_map()

        if self.text is not None:
            result['Text'] = self.text

        if self.voice is not None:
            result['Voice'] = self.voice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NlsAccessType') is not None:
            self.nls_access_type = m.get('NlsAccessType')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        if m.get('Params') is not None:
            temp_model = main_models.PreviewVoiceRequestParams()
            self.params = temp_model.from_map(m.get('Params'))

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        return self

class PreviewVoiceRequestParams(DaraModel):
    def __init__(
        self,
        pitch_rate: float = None,
        speech_rate: float = None,
        volume: int = None,
    ):
        self.pitch_rate = pitch_rate
        self.speech_rate = speech_rate
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

