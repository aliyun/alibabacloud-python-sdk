# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ModifyTTSConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        ttsconfig: main_models.ModifyTTSConfigResponseBodyTTSConfig = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.ttsconfig = ttsconfig

    def validate(self):
        if self.ttsconfig:
            self.ttsconfig.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.ttsconfig is not None:
            result['TTSConfig'] = self.ttsconfig.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TTSConfig') is not None:
            temp_model = main_models.ModifyTTSConfigResponseBodyTTSConfig()
            self.ttsconfig = temp_model.from_map(m.get('TTSConfig'))

        return self

class ModifyTTSConfigResponseBodyTTSConfig(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        pitch_rate: str = None,
        script_id: str = None,
        speech_rate: str = None,
        ttsconfig_id: str = None,
        voice: str = None,
        volume: str = None,
    ):
        self.instance_id = instance_id
        # 语调
        # [-500,500]之间整数。默认值为0。
        # 
        # 大于0表示升高音高。
        # 
        # 小于0表示降低音高。
        self.pitch_rate = pitch_rate
        self.script_id = script_id
        self.speech_rate = speech_rate
        self.ttsconfig_id = ttsconfig_id
        self.voice = voice
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.ttsconfig_id is not None:
            result['TTSConfigId'] = self.ttsconfig_id

        if self.voice is not None:
            result['Voice'] = self.voice

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('TTSConfigId') is not None:
            self.ttsconfig_id = m.get('TTSConfigId')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

