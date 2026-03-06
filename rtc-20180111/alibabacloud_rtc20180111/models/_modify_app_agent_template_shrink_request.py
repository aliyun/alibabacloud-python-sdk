# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAppAgentTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_silence_config_shrink: str = None,
        ambient_sound_config_shrink: str = None,
        app_id: str = None,
        asr_config_shrink: str = None,
        back_channel_config_shrink: str = None,
        chat_mode: int = None,
        enable_video_understanding: bool = None,
        greeting: str = None,
        id: str = None,
        interrupt_config_shrink: str = None,
        interrupt_mode: int = None,
        llm_config_shrink: str = None,
        name: str = None,
        prefer_video: int = None,
        tts_config_shrink: str = None,
        type: int = None,
    ):
        self.agent_silence_config_shrink = agent_silence_config_shrink
        self.ambient_sound_config_shrink = ambient_sound_config_shrink
        # This parameter is required.
        self.app_id = app_id
        self.asr_config_shrink = asr_config_shrink
        self.back_channel_config_shrink = back_channel_config_shrink
        self.chat_mode = chat_mode
        self.enable_video_understanding = enable_video_understanding
        self.greeting = greeting
        # This parameter is required.
        self.id = id
        self.interrupt_config_shrink = interrupt_config_shrink
        self.interrupt_mode = interrupt_mode
        self.llm_config_shrink = llm_config_shrink
        # This parameter is required.
        self.name = name
        self.prefer_video = prefer_video
        self.tts_config_shrink = tts_config_shrink
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_silence_config_shrink is not None:
            result['AgentSilenceConfig'] = self.agent_silence_config_shrink

        if self.ambient_sound_config_shrink is not None:
            result['AmbientSoundConfig'] = self.ambient_sound_config_shrink

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.asr_config_shrink is not None:
            result['AsrConfig'] = self.asr_config_shrink

        if self.back_channel_config_shrink is not None:
            result['BackChannelConfig'] = self.back_channel_config_shrink

        if self.chat_mode is not None:
            result['ChatMode'] = self.chat_mode

        if self.enable_video_understanding is not None:
            result['EnableVideoUnderstanding'] = self.enable_video_understanding

        if self.greeting is not None:
            result['Greeting'] = self.greeting

        if self.id is not None:
            result['Id'] = self.id

        if self.interrupt_config_shrink is not None:
            result['InterruptConfig'] = self.interrupt_config_shrink

        if self.interrupt_mode is not None:
            result['InterruptMode'] = self.interrupt_mode

        if self.llm_config_shrink is not None:
            result['LlmConfig'] = self.llm_config_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.prefer_video is not None:
            result['PreferVideo'] = self.prefer_video

        if self.tts_config_shrink is not None:
            result['TtsConfig'] = self.tts_config_shrink

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentSilenceConfig') is not None:
            self.agent_silence_config_shrink = m.get('AgentSilenceConfig')

        if m.get('AmbientSoundConfig') is not None:
            self.ambient_sound_config_shrink = m.get('AmbientSoundConfig')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AsrConfig') is not None:
            self.asr_config_shrink = m.get('AsrConfig')

        if m.get('BackChannelConfig') is not None:
            self.back_channel_config_shrink = m.get('BackChannelConfig')

        if m.get('ChatMode') is not None:
            self.chat_mode = m.get('ChatMode')

        if m.get('EnableVideoUnderstanding') is not None:
            self.enable_video_understanding = m.get('EnableVideoUnderstanding')

        if m.get('Greeting') is not None:
            self.greeting = m.get('Greeting')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InterruptConfig') is not None:
            self.interrupt_config_shrink = m.get('InterruptConfig')

        if m.get('InterruptMode') is not None:
            self.interrupt_mode = m.get('InterruptMode')

        if m.get('LlmConfig') is not None:
            self.llm_config_shrink = m.get('LlmConfig')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PreferVideo') is not None:
            self.prefer_video = m.get('PreferVideo')

        if m.get('TtsConfig') is not None:
            self.tts_config_shrink = m.get('TtsConfig')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

