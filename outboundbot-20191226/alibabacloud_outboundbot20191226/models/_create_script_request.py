# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateScriptRequest(DaraModel):
    def __init__(
        self,
        agent_id: int = None,
        agent_key: str = None,
        agent_llm: bool = None,
        asr_config: str = None,
        chatbot_id: str = None,
        emotion_enable: bool = None,
        industry: str = None,
        instance_id: str = None,
        long_wait_enable: bool = None,
        mini_playback_enable: bool = None,
        new_barge_in_enable: bool = None,
        nlu_access_type: str = None,
        nlu_engine: str = None,
        scene: str = None,
        script_content: List[str] = None,
        script_description: str = None,
        script_name: str = None,
        script_nlu_profile_json_string: str = None,
        script_waveform: List[str] = None,
        tts_config: str = None,
    ):
        self.agent_id = agent_id
        self.agent_key = agent_key
        self.agent_llm = agent_llm
        self.asr_config = asr_config
        self.chatbot_id = chatbot_id
        self.emotion_enable = emotion_enable
        # This parameter is required.
        self.industry = industry
        # This parameter is required.
        self.instance_id = instance_id
        self.long_wait_enable = long_wait_enable
        self.mini_playback_enable = mini_playback_enable
        self.new_barge_in_enable = new_barge_in_enable
        self.nlu_access_type = nlu_access_type
        self.nlu_engine = nlu_engine
        # This parameter is required.
        self.scene = scene
        self.script_content = script_content
        self.script_description = script_description
        # This parameter is required.
        self.script_name = script_name
        self.script_nlu_profile_json_string = script_nlu_profile_json_string
        self.script_waveform = script_waveform
        self.tts_config = tts_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.agent_llm is not None:
            result['AgentLlm'] = self.agent_llm

        if self.asr_config is not None:
            result['AsrConfig'] = self.asr_config

        if self.chatbot_id is not None:
            result['ChatbotId'] = self.chatbot_id

        if self.emotion_enable is not None:
            result['EmotionEnable'] = self.emotion_enable

        if self.industry is not None:
            result['Industry'] = self.industry

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.long_wait_enable is not None:
            result['LongWaitEnable'] = self.long_wait_enable

        if self.mini_playback_enable is not None:
            result['MiniPlaybackEnable'] = self.mini_playback_enable

        if self.new_barge_in_enable is not None:
            result['NewBargeInEnable'] = self.new_barge_in_enable

        if self.nlu_access_type is not None:
            result['NluAccessType'] = self.nlu_access_type

        if self.nlu_engine is not None:
            result['NluEngine'] = self.nlu_engine

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.script_content is not None:
            result['ScriptContent'] = self.script_content

        if self.script_description is not None:
            result['ScriptDescription'] = self.script_description

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.script_nlu_profile_json_string is not None:
            result['ScriptNluProfileJsonString'] = self.script_nlu_profile_json_string

        if self.script_waveform is not None:
            result['ScriptWaveform'] = self.script_waveform

        if self.tts_config is not None:
            result['TtsConfig'] = self.tts_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('AgentLlm') is not None:
            self.agent_llm = m.get('AgentLlm')

        if m.get('AsrConfig') is not None:
            self.asr_config = m.get('AsrConfig')

        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')

        if m.get('EmotionEnable') is not None:
            self.emotion_enable = m.get('EmotionEnable')

        if m.get('Industry') is not None:
            self.industry = m.get('Industry')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LongWaitEnable') is not None:
            self.long_wait_enable = m.get('LongWaitEnable')

        if m.get('MiniPlaybackEnable') is not None:
            self.mini_playback_enable = m.get('MiniPlaybackEnable')

        if m.get('NewBargeInEnable') is not None:
            self.new_barge_in_enable = m.get('NewBargeInEnable')

        if m.get('NluAccessType') is not None:
            self.nlu_access_type = m.get('NluAccessType')

        if m.get('NluEngine') is not None:
            self.nlu_engine = m.get('NluEngine')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')

        if m.get('ScriptDescription') is not None:
            self.script_description = m.get('ScriptDescription')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('ScriptNluProfileJsonString') is not None:
            self.script_nlu_profile_json_string = m.get('ScriptNluProfileJsonString')

        if m.get('ScriptWaveform') is not None:
            self.script_waveform = m.get('ScriptWaveform')

        if m.get('TtsConfig') is not None:
            self.tts_config = m.get('TtsConfig')

        return self

