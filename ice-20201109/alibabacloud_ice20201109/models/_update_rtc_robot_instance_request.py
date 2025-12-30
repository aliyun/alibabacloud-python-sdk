# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class UpdateRtcRobotInstanceRequest(DaraModel):
    def __init__(
        self,
        config: main_models.UpdateRtcRobotInstanceRequestConfig = None,
        instance_id: str = None,
    ):
        self.config = config
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.UpdateRtcRobotInstanceRequestConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class UpdateRtcRobotInstanceRequestConfig(DaraModel):
    def __init__(
        self,
        enable_voice_interrupt: bool = None,
        greeting: str = None,
        voice_id: str = None,
    ):
        self.enable_voice_interrupt = enable_voice_interrupt
        self.greeting = greeting
        self.voice_id = voice_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_voice_interrupt is not None:
            result['EnableVoiceInterrupt'] = self.enable_voice_interrupt

        if self.greeting is not None:
            result['Greeting'] = self.greeting

        if self.voice_id is not None:
            result['VoiceId'] = self.voice_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableVoiceInterrupt') is not None:
            self.enable_voice_interrupt = m.get('EnableVoiceInterrupt')

        if m.get('Greeting') is not None:
            self.greeting = m.get('Greeting')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        return self

