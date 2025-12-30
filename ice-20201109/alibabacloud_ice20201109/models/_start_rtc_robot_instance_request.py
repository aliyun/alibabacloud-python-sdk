# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class StartRtcRobotInstanceRequest(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        channel_id: str = None,
        config: main_models.StartRtcRobotInstanceRequestConfig = None,
        robot_id: str = None,
        user_data: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.channel_id = channel_id
        self.config = config
        # This parameter is required.
        self.robot_id = robot_id
        self.user_data = user_data
        # This parameter is required.
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

        if self.robot_id is not None:
            result['RobotId'] = self.robot_id

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
            temp_model = main_models.StartRtcRobotInstanceRequestConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class StartRtcRobotInstanceRequestConfig(DaraModel):
    def __init__(
        self,
        asr_max_silence: int = None,
        enable_voice_interrupt: bool = None,
        greeting: str = None,
        use_voiceprint: bool = None,
        user_offline_timeout: int = None,
        user_online_timeout: int = None,
        voice_id: str = None,
        voiceprint_id: str = None,
        volume: int = None,
    ):
        self.asr_max_silence = asr_max_silence
        self.enable_voice_interrupt = enable_voice_interrupt
        self.greeting = greeting
        self.use_voiceprint = use_voiceprint
        self.user_offline_timeout = user_offline_timeout
        self.user_online_timeout = user_online_timeout
        self.voice_id = voice_id
        self.voiceprint_id = voiceprint_id
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_max_silence is not None:
            result['AsrMaxSilence'] = self.asr_max_silence

        if self.enable_voice_interrupt is not None:
            result['EnableVoiceInterrupt'] = self.enable_voice_interrupt

        if self.greeting is not None:
            result['Greeting'] = self.greeting

        if self.use_voiceprint is not None:
            result['UseVoiceprint'] = self.use_voiceprint

        if self.user_offline_timeout is not None:
            result['UserOfflineTimeout'] = self.user_offline_timeout

        if self.user_online_timeout is not None:
            result['UserOnlineTimeout'] = self.user_online_timeout

        if self.voice_id is not None:
            result['VoiceId'] = self.voice_id

        if self.voiceprint_id is not None:
            result['VoiceprintId'] = self.voiceprint_id

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrMaxSilence') is not None:
            self.asr_max_silence = m.get('AsrMaxSilence')

        if m.get('EnableVoiceInterrupt') is not None:
            self.enable_voice_interrupt = m.get('EnableVoiceInterrupt')

        if m.get('Greeting') is not None:
            self.greeting = m.get('Greeting')

        if m.get('UseVoiceprint') is not None:
            self.use_voiceprint = m.get('UseVoiceprint')

        if m.get('UserOfflineTimeout') is not None:
            self.user_offline_timeout = m.get('UserOfflineTimeout')

        if m.get('UserOnlineTimeout') is not None:
            self.user_online_timeout = m.get('UserOnlineTimeout')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        if m.get('VoiceprintId') is not None:
            self.voiceprint_id = m.get('VoiceprintId')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

