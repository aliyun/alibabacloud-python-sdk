# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyScriptRequest(DaraModel):
    def __init__(
        self,
        agent_id: int = None,
        agent_key: str = None,
        agent_llm: bool = None,
        asr_config: str = None,
        chat_config: str = None,
        chatbot_id: str = None,
        emotion_enable: bool = None,
        industry: str = None,
        instance_id: str = None,
        label_config: str = None,
        long_wait_enable: bool = None,
        mini_playback_config_list_json_string: str = None,
        mini_playback_enable: bool = None,
        new_barge_in_enable: bool = None,
        nls_config: str = None,
        nlu_access_type: str = None,
        nlu_engine: str = None,
        scene: str = None,
        script_content: List[str] = None,
        script_description: str = None,
        script_id: str = None,
        script_name: str = None,
        script_waveform: List[str] = None,
        tts_config: str = None,
    ):
        # The ID of the robot workspace.
        self.agent_id = agent_id
        # The access key for the robot workspace.
        self.agent_key = agent_key
        # Indicates whether the robot workspace is a Large Language Model (LLM) workspace.
        self.agent_llm = agent_llm
        # The ASR configuration. Parameter definitions:
        # 
        # - **appKey**: The Alibaba Cloud account appKey.
        # 
        # - **maxEndSilence**: The duration for voice endpoint detection.
        # 
        # - **silenceTimeout**: The silence timeout. Unit: seconds. The system times out after the user is silent for N seconds.
        # 
        # - **engine**: The service to invoke. Valid values: ali, xunfei.
        # 
        # - **nlsServiceType**: The type of the invoked service.
        # 
        #   - Managed: Public cloud NLS service.
        # 
        #   - Authorized: Authorized NLS service.
        # 
        #   - Provided: NLS service provided by the customer through AS/SK.
        # 
        #   - Apes: Private cloud service.
        # 
        # - **engineXunfei**: If the caller is xunfei, fill in the corresponding configuration.
        # 
        # > If engine is set to ali and nlsServiceType is set to Authorized, a custom service is used, and the service provider is ali. If engine is set to ali and nlsServiceType is set to Managed, the default service is used. If engine is set to xunfei and nlsServiceType is set to Authorized, the service provider is xunfei. You must fill in the xunfei configuration, such as {"uuid":"ed2xxxxxxxxx","globalMaxEndSilence":700,"globalMaxEndSilenceEnable":true}.
        # 
        # - **globalMaxEndSilence**: Silence detection. Unit: milliseconds.
        # 
        # - **globalMaxEndSilenceEnable**: The switch for silence detection. Default value: enabled.
        # 
        # - **speechNoiseThreshold**: The noise filtering threshold.
        self.asr_config = asr_config
        # The call configuration.
        # 
        # - silenceConfig: Silence configuration.
        # 
        #   - silenceReplyTimeout: The timeout period for silence replies, in milliseconds.
        # 
        #   - silenceTimeoutMaxCount: Hang up after several rounds of silence timeout.
        # 
        #   - silenceTimeoutMaxCountEnable: Indicates whether to hang up on silence.
        # 
        # - hangupConfig: Hang-up configuration.
        # 
        #   - aiHangupEnable: AI hang-up. Valid values: true, false.
        # 
        #   - delayHangup: Delayed hang-up. Maximum value: 10.
        # 
        #   - hangupMaxRounds: Interaction rounds. Maximum value: 100.
        # 
        #   - hangupMaxRoundsBroadcast: The script for hang-up broadcast.
        # 
        #   - hangupMaxRoundsEnable: Determine the maximum number of interaction rounds. Valid values: true, false.
        # 
        # - securityInterceptConfig: Security block configuration.
        # 
        #   - broadcast: The script for block broadcast.
        # 
        # - specialInterceptConfig: Special case block.
        # 
        #   - specialInterceptEnable: The switch for special case block.
        # 
        #   - specialIntercepts: Special cases.
        # 
        #     - voiceAssistant: Voice assistant.
        # 
        #     - extensionNumberTransfer: Extension number transfer.
        # 
        # - transitionConfig: Transition phrase model configuration.
        # 
        #   - transitionSwitch: The switch for the transition phrase model.
        self.chat_config = chat_config
        # The ID of the chatbot.
        self.chatbot_id = chatbot_id
        # The switch for emotion detection configuration.
        self.emotion_enable = emotion_enable
        # The industry.
        # 
        # This parameter is required.
        self.industry = industry
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.label_config = label_config
        # The switch for intelligent sentence segmentation configuration (small model).
        self.long_wait_enable = long_wait_enable
        # The configuration for transition phrases. Customization is not supported temporarily. Do not pass this parameter by default. This parameter is deprecated.
        self.mini_playback_config_list_json_string = mini_playback_config_list_json_string
        # The switch for transition phrase configuration (small model).
        self.mini_playback_enable = mini_playback_enable
        # The switch for graceful barge-in configuration (small model).
        self.new_barge_in_enable = new_barge_in_enable
        # This parameter is deprecated.
        self.nls_config = nls_config
        # The NLU access method (applicable only to Large Language Model (LLM) scenarios).
        # 
        # Enumeration:
        # 
        # - Managed: Access using an Alibaba Cloud public account.
        # 
        # - This parameter is empty for non-LLM scenarios.
        self.nlu_access_type = nlu_access_type
        # The NLU engine (applicable only to Large Language Model (LLM) scenarios).
        # 
        # > After a scenario is created, you cannot modify the scenario mode.
        # 
        # Enumeration:
        # 
        # - Prompts: Text filling mode.
        # 
        # - SSE_FUNCTION: Function Compute mode.
        # 
        # - This parameter is empty for non-LLM scenarios.
        self.nlu_engine = nlu_engine
        # The scenario information.
        # 
        # This parameter is required.
        self.scene = scene
        # For notification instances, pass in the script list. This parameter is deprecated.
        self.script_content = script_content
        # The description of the script.
        self.script_description = script_description
        # The ID of the script.
        # 
        # This parameter is required.
        self.script_id = script_id
        # The name of the script.
        # 
        # This parameter is required.
        self.script_name = script_name
        # For notification instances, pass in the script voice list. This parameter is deprecated.
        self.script_waveform = script_waveform
        # The TTS configuration. Parameter definitions:
        # 
        # - **voice**: The voice actor.
        # 
        # - **volume**: The volume. Valid values: 0 to 100. Default value: 50.
        # 
        # - **speechRate**: The speech rate. Valid values: -500 to 500. Default value: 0.
        # 
        # - **pitchRate**: The pitch rate. Valid values: -500 to 500. Default value: 0.
        # 
        # - **globalInterruptible**: The voice interruption configuration.
        # 
        # - **engine**
        # 
        #   **nlsServiceType**: The type of the invoked service.
        # 
        #   - Managed: Public cloud NLS service.
        # 
        #   - Authorized: Authorized NLS service.
        # 
        #   - Provided: NLS service provided by the customer through AS/SK.
        # 
        #   - Apes: Private cloud service.
        # 
        # - **engineXunfei**: The configuration when the service provider is xunfei.
        # 
        # > 1\\. If engine is set to ali and nlsServiceType is set to Authorized, a custom service is used. 2. If the service provider is ali, and engine is set to ali and nlsServiceType is set to Managed, the default service is used. 3. If engine is set to xunfei (applicable to small model scenarios) and nlsServiceType is set to Authorized, the service provider is xunfei. You must fill in the engineXunfei configuration, such as {"pitchRate":50,"speechRate":50,"voice":"aisjiuxu","volume":50}. 4. If engine is set to volc and nlsServiceType is set to Authorized, it indicates that Doubao is applicable.
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

        if self.chat_config is not None:
            result['ChatConfig'] = self.chat_config

        if self.chatbot_id is not None:
            result['ChatbotId'] = self.chatbot_id

        if self.emotion_enable is not None:
            result['EmotionEnable'] = self.emotion_enable

        if self.industry is not None:
            result['Industry'] = self.industry

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.label_config is not None:
            result['LabelConfig'] = self.label_config

        if self.long_wait_enable is not None:
            result['LongWaitEnable'] = self.long_wait_enable

        if self.mini_playback_config_list_json_string is not None:
            result['MiniPlaybackConfigListJsonString'] = self.mini_playback_config_list_json_string

        if self.mini_playback_enable is not None:
            result['MiniPlaybackEnable'] = self.mini_playback_enable

        if self.new_barge_in_enable is not None:
            result['NewBargeInEnable'] = self.new_barge_in_enable

        if self.nls_config is not None:
            result['NlsConfig'] = self.nls_config

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

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

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

        if m.get('ChatConfig') is not None:
            self.chat_config = m.get('ChatConfig')

        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')

        if m.get('EmotionEnable') is not None:
            self.emotion_enable = m.get('EmotionEnable')

        if m.get('Industry') is not None:
            self.industry = m.get('Industry')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LabelConfig') is not None:
            self.label_config = m.get('LabelConfig')

        if m.get('LongWaitEnable') is not None:
            self.long_wait_enable = m.get('LongWaitEnable')

        if m.get('MiniPlaybackConfigListJsonString') is not None:
            self.mini_playback_config_list_json_string = m.get('MiniPlaybackConfigListJsonString')

        if m.get('MiniPlaybackEnable') is not None:
            self.mini_playback_enable = m.get('MiniPlaybackEnable')

        if m.get('NewBargeInEnable') is not None:
            self.new_barge_in_enable = m.get('NewBargeInEnable')

        if m.get('NlsConfig') is not None:
            self.nls_config = m.get('NlsConfig')

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

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('ScriptWaveform') is not None:
            self.script_waveform = m.get('ScriptWaveform')

        if m.get('TtsConfig') is not None:
            self.tts_config = m.get('TtsConfig')

        return self

