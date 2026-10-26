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
        # Specifies whether the robot workspace is a large model workspace.
        self.agent_llm = agent_llm
        # The ASR configuration. Parameter definitions:
        # 
        # - **appKey**: The appKey of the Alibaba Cloud account.
        # - **maxEndSilence**: The duration of voice endpoint detection.
        # - **silenceTimeout**: The silence timeout in seconds. The timeout occurs after the user is silent for N seconds.
        # 
        # - **engine**: The service to call. Valid values: ali and xunfei.
        # - **nlsServiceType**: The type of the service to call. Valid values: 
        #    - Managed: The NLS service on the public cloud. 
        #    - Authorized: The authorized NLS service.
        #    - Provided: The NLS service provided by the customer through AccessKey ID and AccessKey secret.
        #    - Apes: The private cloud service.
        # - **engineXunfei**: The configuration required when the caller is xunfei.
        # > When engine is set to ali and nlsServiceType is set to Authorized, a custom service is used, and the service provider is ali. When engine is set to ali and nlsServiceType is set to Managed, the default service is used. When engine is set to xunfei and nlsServiceType is set to Authorized, the service provider is xunfei, and you must enter the xunfei configuration: {"uuid":"ed2xxxxxxxxx","globalMaxEndSilence":700,"globalMaxEndSilenceEnable":true}.
        # 
        # - **globalMaxEndSilence**: The silence detection duration in milliseconds.
        # 
        # - **globalMaxEndSilenceEnable**: The silence detection switch. Enabled by default.
        # 
        # - **speechNoiseThreshold**: The noise filtering threshold.
        self.asr_config = asr_config
        # The call configuration.
        # - silenceConfig: The silence configuration.
        #     - silenceReplyTimeout: The silence reply timeout in milliseconds.
        #     - silenceTimeoutMaxCount: The maximum number of silence timeout rounds before hanging up.
        #     - silenceTimeoutMaxCountEnable: Specifies whether to hang up after silence timeouts.
        # - hangupConfig: The hang-up configuration.
        #     - aiHangupEnable: Specifies whether to enable AI hang-up. Valid values: true and false.
        #     - delayHangup: The delayed hang-up time. Maximum value: 10.
        #     - hangupMaxRounds: The maximum number of interaction rounds. Maximum value: 100.
        #     - hangupMaxRoundsBroadcast: The broadcast script for hanging up.
        #     - hangupMaxRoundsEnable: Specifies whether to enable the maximum interaction rounds check. Valid values: true and false.
        # - securityInterceptConfig: The security interception configuration.
        #     - broadcast: The interception broadcast script.
        # - specialInterceptConfig: The special case interception configuration.
        #     - specialInterceptEnable: Specifies whether to enable special case interception.
        #     - specialIntercepts: The special cases.
        #         - voiceAssistant: Voice assistant.
        #         - extensionNumberTransfer: Extension number transfer.
        # - transitionConfig: The backchannel model configuration.
        #     - transitionSwitch: Specifies whether to enable the backchannel model.
        self.chat_config = chat_config
        # The robot ID.
        self.chatbot_id = chatbot_id
        # Specifies whether to enable the emotion recognition configuration.
        self.emotion_enable = emotion_enable
        # The industry.
        # 
        # This parameter is required.
        self.industry = industry
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The label definition.
        # > Used in large model flow canvas scenarios.
        self.label_config = label_config
        # Specifies whether to enable the intelligent sentence segmentation configuration for small models.
        self.long_wait_enable = long_wait_enable
        # The backchannel configuration. Customization is not supported at the moment. You do not need to pass this parameter by default. **[Deprecated]**
        self.mini_playback_config_list_json_string = mini_playback_config_list_json_string
        # Specifies whether to enable the backchannel configuration for small models.
        self.mini_playback_enable = mini_playback_enable
        # Specifies whether to enable the graceful interruption configuration for small models.
        self.new_barge_in_enable = new_barge_in_enable
        # **[Deprecated]**
        self.nls_config = nls_config
        # The NLU access method. This parameter is applicable only to large model scenarios.
        # 
        # Valid values:
        # - Managed: Uses the Alibaba Cloud public account for access.
        # - Empty: For non-large model scenarios.
        self.nlu_access_type = nlu_access_type
        # The NLU engine. This parameter is applicable only to large model scenarios.
        # 
        # > After a scenario is created, the scenario mode cannot be modified.
        # 
        # Valid values:
        # - Prompts: The text input mode.
        # - SSE_FUNCTION: The Function Compute mode.
        # - Empty: For non-large model scenarios.
        self.nlu_engine = nlu_engine
        # The scenario information.
        # 
        # This parameter is required.
        self.scene = scene
        # The script list for notification instances. **[Deprecated]**
        self.script_content = script_content
        # The script description.
        self.script_description = script_description
        # The script ID.
        # 
        # This parameter is required.
        self.script_id = script_id
        # The script name.
        # 
        # This parameter is required.
        self.script_name = script_name
        # The script voice list for notification instances. **[Deprecated]**
        self.script_waveform = script_waveform
        # The TTS configuration. Parameter definitions:
        # 
        # - **voice**: The speaker.
        # - **volume**: The volume. Valid values: 0 to 100. Default value: 50.
        # - **speechRate**: The speech rate. Valid values: -500 to 500. Default value: 0.
        # - **pitchRate**: The pitch. Valid values: -500 to 500. Default value: 0.
        # - **openingPromptInterruptible**: The interruption configuration for the opening prompt.
        # - **closingStatementInterruptible**: The interruption configuration for the closing statement.
        # 
        # - **globalInterruptible**: The voice interruption configuration.
        # - **engine**: The service to call. Valid values: ali, volc, and xunfei. xunfei is not supported in large model scenarios.
        # - **nlsServiceType**: The type of the service to call. Valid values: 
        #    - Managed: The NLS service on the public cloud. 
        #    - Authorized: The authorized NLS service.
        #    - Provided: The NLS service provided by the customer through AccessKey ID and AccessKey secret.
        #    - Apes: The private cloud service.
        # - **engineXunfei**: The configuration when the service provider is xunfei.
        # 
        # > 1. When engine is set to ali and nlsServiceType is set to Authorized, a custom service is used. 2. When the service provider is ali, engine is set to ali, and nlsServiceType is set to Managed, the default service is used. 3. When engine is set to xunfei (applicable to small model scenarios) and nlsServiceType is set to Authorized, the service provider is xunfei, and you must enter the engineXunfei configuration: {"pitchRate":50,"speechRate":50,"voice":"aisjiuxu","volume":50}. 4. When engine is set to volc and nlsServiceType is set to Authorized, the applicable service is doubao.
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

