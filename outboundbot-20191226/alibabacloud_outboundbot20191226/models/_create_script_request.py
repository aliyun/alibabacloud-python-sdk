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
        # Robot workspace ID
        self.agent_id = agent_id
        # Robot workspace access Key
        self.agent_key = agent_key
        # Is the robot workspace a Large Language Model (LLM) workspace?
        self.agent_llm = agent_llm
        # ASR configuration. Parameter definitions:
        # 
        # - **appKey**: Alibaba Cloud account appKey.
        # 
        # - **maxEndSilence**: Voice endpoint detection duration.
        # 
        # - **silenceTimeout**: Silence timeout. Unit: seconds. The user times out after N seconds of silence.
        # 
        # - **engine**: Invoke service; [ali, xunfei]
        # 
        # - **nlsServiceType**: Invoke service type [Managed, Authorized]
        # 
        # - **engineXunfei**: If the caller is xunfei, enter the corresponding configuration.
        # 
        # > If you select ali as the engine and Authorized as the nlsServiceType, a custom service is used, and the service provider is ali. If you select ali as the engine and Managed as the nlsServiceType, the default service is used. If you select xunfei as the engine and Authorized as the nlsServiceType, xunfei is the service provider. You must enter the xunfei configuration: {"uuid":"ed2xxxxxxxxx","globalMaxEndSilence":700,"globalMaxEndSilenceEnable":true}
        # 
        # - **globalMaxEndSilence**: Silence detection. Unit: milliseconds.
        # 
        # - **globalMaxEndSilenceEnable**: Silence detection switch. Enabled by default.
        # 
        # - **speechNoiseThreshold**: Noise filtering threshold
        self.asr_config = asr_config
        # If the NluServiceType of the instance is Authorized or Provided, specify the ID of the chatbot instance to which the script needs to be attached using this field.
        self.chatbot_id = chatbot_id
        # Emotion detection configuration switch (applicable to small models)
        self.emotion_enable = emotion_enable
        # Industry
        # 
        # This parameter is required.
        self.industry = industry
        # Instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Intelligent sentence segmentation configuration switch (applicable to small models)
        self.long_wait_enable = long_wait_enable
        # Connective phrase configuration switch (applicable to small models)
        self.mini_playback_enable = mini_playback_enable
        # Graceful interruption configuration switch (applicable to small models)
        self.new_barge_in_enable = new_barge_in_enable
        # NLU access method (applicable only to Large Language Model (LLM) scenarios). Enumeration: Managed - Access using an Alibaba public account. This field is empty for non-LLM scenarios.
        self.nlu_access_type = nlu_access_type
        # NLU engine (applicable only to Large Language Model (LLM) scenarios). This field is empty for non-LLM scenarios.
        # 
        # - Prompts - Large Language Model (LLM) scenario,
        # 
        # - SSE_FUNCTION - Function Compute pattern.
        # 
        # - BeeBot - Workflow pattern.
        self.nlu_engine = nlu_engine
        # Scenario
        # 
        # This parameter is required.
        self.scene = scene
        # For notification instances, pass in the script list. Deprecated.
        self.script_content = script_content
        # Script description
        self.script_description = script_description
        # Script name
        # 
        # This parameter is required.
        self.script_name = script_name
        # > If nluEngine is SSE_FUNCTION, you must pass in the corresponding configuration.
        # 
        # Function Compute service pattern configuration
        # 
        # - fcRegion: Function service region
        # 
        # - fcFunction: Function service name
        # 
        # - fcHttpTriggerUrl Function service trigger
        self.script_nlu_profile_json_string = script_nlu_profile_json_string
        # For notification instances, pass in the script voice list. Deprecated.
        self.script_waveform = script_waveform
        # TTS configuration. Parameter definitions:
        # 
        # - **voice**: Speaker.
        # 
        # - **volume**: Volume. Value range: 0 to 100. Default value: 50.
        # 
        # - **speechRate**: Speech rate. Value range: -500 to 500. Default value: 0.
        # 
        # - **pitchRate**: Pitch rate. Value range: -500 to 500. Default value: 0.
        # 
        # - **globalInterruptible**: Voice interruption configuration.
        #   -**engine**: Invoke service; [ali, volc, xunfei]. Large Language Model (LLM) scenarios do not support xunfei.
        # 
        # - **nlsServiceType**: Service type. [Managed, Authorized]
        # 
        # - **engineXunfei**: Configuration when the service provider is xunfei.
        # 
        # > 1\\. If you select ali as the engine and Authorized as the nlsServiceType, a custom service is used. 2. If the service provider is ali, and you select ali as the engine and Managed as the nlsServiceType, the default service is used. 3. If you select xunfei as the engine (applicable to small model scenarios) and Authorized as the nlsServiceType, xunfei is the service provider. You must enter the engineXunfei configuration: {"pitchRate":50,"speechRate":50,"voice":"aisjiuxu","volume":50}. 4. If you select volc as the engine and Authorized as the nlsServiceType, it applies to doubao.
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

