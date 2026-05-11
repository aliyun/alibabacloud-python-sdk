# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTTSConfigRequest(DaraModel):
    def __init__(
        self,
        ali_customized_voice: str = None,
        app_key: str = None,
        engine: str = None,
        engine_xunfei: str = None,
        instance_id: str = None,
        nls_service_type: str = None,
        pitch_rate: str = None,
        speech_rate: str = None,
        tts_overrides: str = None,
        voice: str = None,
        volume: str = None,
    ):
        self.ali_customized_voice = ali_customized_voice
        self.app_key = app_key
        self.engine = engine
        self.engine_xunfei = engine_xunfei
        # This parameter is required.
        self.instance_id = instance_id
        self.nls_service_type = nls_service_type
        self.pitch_rate = pitch_rate
        self.speech_rate = speech_rate
        self.tts_overrides = tts_overrides
        self.voice = voice
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_customized_voice is not None:
            result['AliCustomizedVoice'] = self.ali_customized_voice

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_xunfei is not None:
            result['EngineXunfei'] = self.engine_xunfei

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nls_service_type is not None:
            result['NlsServiceType'] = self.nls_service_type

        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.tts_overrides is not None:
            result['TtsOverrides'] = self.tts_overrides

        if self.voice is not None:
            result['Voice'] = self.voice

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliCustomizedVoice') is not None:
            self.ali_customized_voice = m.get('AliCustomizedVoice')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineXunfei') is not None:
            self.engine_xunfei = m.get('EngineXunfei')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NlsServiceType') is not None:
            self.nls_service_type = m.get('NlsServiceType')

        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('TtsOverrides') is not None:
            self.tts_overrides = m.get('TtsOverrides')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

