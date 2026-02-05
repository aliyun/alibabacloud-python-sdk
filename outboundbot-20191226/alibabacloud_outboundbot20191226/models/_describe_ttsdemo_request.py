# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTTSDemoRequest(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        ali_customized_voice: str = None,
        app_key: str = None,
        engine: str = None,
        instance_id: str = None,
        nls_service_type: str = None,
        pitch_rate: int = None,
        script_id: str = None,
        secret_key: str = None,
        speech_rate: int = None,
        text: str = None,
        voice: str = None,
        volume: int = None,
    ):
        self.access_key = access_key
        self.ali_customized_voice = ali_customized_voice
        self.app_key = app_key
        self.engine = engine
        # This parameter is required.
        self.instance_id = instance_id
        self.nls_service_type = nls_service_type
        self.pitch_rate = pitch_rate
        self.script_id = script_id
        self.secret_key = secret_key
        self.speech_rate = speech_rate
        # This parameter is required.
        self.text = text
        self.voice = voice
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.ali_customized_voice is not None:
            result['AliCustomizedVoice'] = self.ali_customized_voice

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nls_service_type is not None:
            result['NlsServiceType'] = self.nls_service_type

        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.text is not None:
            result['Text'] = self.text

        if self.voice is not None:
            result['Voice'] = self.voice

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('AliCustomizedVoice') is not None:
            self.ali_customized_voice = m.get('AliCustomizedVoice')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NlsServiceType') is not None:
            self.nls_service_type = m.get('NlsServiceType')

        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

