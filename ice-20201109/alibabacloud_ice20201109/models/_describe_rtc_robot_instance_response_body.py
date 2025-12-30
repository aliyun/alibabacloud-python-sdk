# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class DescribeRtcRobotInstanceResponseBody(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        channel_id: str = None,
        config: main_models.DescribeRtcRobotInstanceResponseBodyConfig = None,
        request_id: str = None,
        status: str = None,
        user_data: str = None,
        user_id: str = None,
    ):
        self.auth_token = auth_token
        self.channel_id = channel_id
        self.config = config
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.user_data = user_data
        self.user_id = user_id

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('Config') is not None:
            temp_model = main_models.DescribeRtcRobotInstanceResponseBodyConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeRtcRobotInstanceResponseBodyConfig(DaraModel):
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

