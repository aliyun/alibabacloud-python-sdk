# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class AIAgentOutboundCallConfig(DaraModel):
    def __init__(
        self,
        ambient_sound_config: main_models.AIAgentOutboundCallConfigAmbientSoundConfig = None,
        asr_config: main_models.AIAgentOutboundCallConfigAsrConfig = None,
        auto_speech_config: main_models.AIAgentOutboundCallConfigAutoSpeechConfig = None,
        back_channeling_config: main_models.AIAgentOutboundCallConfigBackChannelingConfig = None,
        back_channeling_configs: List[main_models.AIAgentOutboundCallConfigBackChannelingConfigs] = None,
        enable_intelligent_segment: bool = None,
        experimental_config: str = None,
        greeting: str = None,
        greeting_delay: int = None,
        interrupt_config: main_models.AIAgentOutboundCallConfigInterruptConfig = None,
        llm_config: main_models.AIAgentOutboundCallConfigLlmConfig = None,
        max_idle_time: int = None,
        tts_config: main_models.AIAgentOutboundCallConfigTtsConfig = None,
        turn_detection_config: main_models.AIAgentOutboundCallConfigTurnDetectionConfig = None,
    ):
        # The configurations for ambient sound.
        self.ambient_sound_config = ambient_sound_config
        # The automatic speech recognition (ASR) configurations.
        self.asr_config = asr_config
        # The configurations for the automatic speech module of the AI agent, which includes prompts during LLM delays and inquiries during prolonged user silence.
        self.auto_speech_config = auto_speech_config
        # >Notice: 
        # 
        # This parameter is deprecated. Use `BackChannelingConfigs` instead.
        self.back_channeling_config = back_channeling_config
        # The configurations for the back-channeling feature module. If you enable this feature, the system randomly plays short and affirmative phrases at specific trigger points.
        self.back_channeling_configs = back_channeling_configs
        # Specifies whether to enable intelligent segmentation. If you enable this feature, short and consecutive speech segments from the user are merged into a complete sentence. Default value: `true`.
        self.enable_intelligent_segment = enable_intelligent_segment
        # The parameters for experimental features. If you have any requirements, contact technical support.
        self.experimental_config = experimental_config
        # The welcome message. This change takes effect in the next call session. If this parameter is not set, no welcome message is played.
        self.greeting = greeting
        # The delay before the welcome message is played. Unit: ms. Default value: 0. Valid values: 0 to 5000.
        self.greeting_delay = greeting_delay
        # The speech interruption policy configurations.
        self.interrupt_config = interrupt_config
        # The configurations of the large language model (LLM).
        self.llm_config = llm_config
        # The maximum wait time for interaction with the AI agent. If the wait time is exceeded, the AI agent goes offline. Unit: seconds. Default value: 600.
        self.max_idle_time = max_idle_time
        # The text-to-speech (TTS) configurations.
        self.tts_config = tts_config
        # The configurations for conversational turn detection.
        self.turn_detection_config = turn_detection_config

    def validate(self):
        if self.ambient_sound_config:
            self.ambient_sound_config.validate()
        if self.asr_config:
            self.asr_config.validate()
        if self.auto_speech_config:
            self.auto_speech_config.validate()
        if self.back_channeling_config:
            self.back_channeling_config.validate()
        if self.back_channeling_configs:
            for v1 in self.back_channeling_configs:
                 if v1:
                    v1.validate()
        if self.interrupt_config:
            self.interrupt_config.validate()
        if self.llm_config:
            self.llm_config.validate()
        if self.tts_config:
            self.tts_config.validate()
        if self.turn_detection_config:
            self.turn_detection_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ambient_sound_config is not None:
            result['AmbientSoundConfig'] = self.ambient_sound_config.to_map()

        if self.asr_config is not None:
            result['AsrConfig'] = self.asr_config.to_map()

        if self.auto_speech_config is not None:
            result['AutoSpeechConfig'] = self.auto_speech_config.to_map()

        if self.back_channeling_config is not None:
            result['BackChannelingConfig'] = self.back_channeling_config.to_map()

        result['BackChannelingConfigs'] = []
        if self.back_channeling_configs is not None:
            for k1 in self.back_channeling_configs:
                result['BackChannelingConfigs'].append(k1.to_map() if k1 else None)

        if self.enable_intelligent_segment is not None:
            result['EnableIntelligentSegment'] = self.enable_intelligent_segment

        if self.experimental_config is not None:
            result['ExperimentalConfig'] = self.experimental_config

        if self.greeting is not None:
            result['Greeting'] = self.greeting

        if self.greeting_delay is not None:
            result['GreetingDelay'] = self.greeting_delay

        if self.interrupt_config is not None:
            result['InterruptConfig'] = self.interrupt_config.to_map()

        if self.llm_config is not None:
            result['LlmConfig'] = self.llm_config.to_map()

        if self.max_idle_time is not None:
            result['MaxIdleTime'] = self.max_idle_time

        if self.tts_config is not None:
            result['TtsConfig'] = self.tts_config.to_map()

        if self.turn_detection_config is not None:
            result['TurnDetectionConfig'] = self.turn_detection_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AmbientSoundConfig') is not None:
            temp_model = main_models.AIAgentOutboundCallConfigAmbientSoundConfig()
            self.ambient_sound_config = temp_model.from_map(m.get('AmbientSoundConfig'))

        if m.get('AsrConfig') is not None:
            temp_model = main_models.AIAgentOutboundCallConfigAsrConfig()
            self.asr_config = temp_model.from_map(m.get('AsrConfig'))

        if m.get('AutoSpeechConfig') is not None:
            temp_model = main_models.AIAgentOutboundCallConfigAutoSpeechConfig()
            self.auto_speech_config = temp_model.from_map(m.get('AutoSpeechConfig'))

        if m.get('BackChannelingConfig') is not None:
            temp_model = main_models.AIAgentOutboundCallConfigBackChannelingConfig()
            self.back_channeling_config = temp_model.from_map(m.get('BackChannelingConfig'))

        self.back_channeling_configs = []
        if m.get('BackChannelingConfigs') is not None:
            for k1 in m.get('BackChannelingConfigs'):
                temp_model = main_models.AIAgentOutboundCallConfigBackChannelingConfigs()
                self.back_channeling_configs.append(temp_model.from_map(k1))

        if m.get('EnableIntelligentSegment') is not None:
            self.enable_intelligent_segment = m.get('EnableIntelligentSegment')

        if m.get('ExperimentalConfig') is not None:
            self.experimental_config = m.get('ExperimentalConfig')

        if m.get('Greeting') is not None:
            self.greeting = m.get('Greeting')

        if m.get('GreetingDelay') is not None:
            self.greeting_delay = m.get('GreetingDelay')

        if m.get('InterruptConfig') is not None:
            temp_model = main_models.AIAgentOutboundCallConfigInterruptConfig()
            self.interrupt_config = temp_model.from_map(m.get('InterruptConfig'))

        if m.get('LlmConfig') is not None:
            temp_model = main_models.AIAgentOutboundCallConfigLlmConfig()
            self.llm_config = temp_model.from_map(m.get('LlmConfig'))

        if m.get('MaxIdleTime') is not None:
            self.max_idle_time = m.get('MaxIdleTime')

        if m.get('TtsConfig') is not None:
            temp_model = main_models.AIAgentOutboundCallConfigTtsConfig()
            self.tts_config = temp_model.from_map(m.get('TtsConfig'))

        if m.get('TurnDetectionConfig') is not None:
            temp_model = main_models.AIAgentOutboundCallConfigTurnDetectionConfig()
            self.turn_detection_config = temp_model.from_map(m.get('TurnDetectionConfig'))

        return self

class AIAgentOutboundCallConfigTurnDetectionConfig(DaraModel):
    def __init__(
        self,
        eagerness: str = None,
        mode: str = None,
        semantic_wait_duration: int = None,
        turn_end_words: List[str] = None,
    ):
        self.eagerness = eagerness
        # The mode for conversational turn detection. Valid values:
        # 
        # - `Normal`: a basic mode that does not use AI for semantic analysis.
        # 
        # - `Semantic`: an AI-powered mode that determines whether the user has finished speaking based on the conversational context.
        # 
        # Default value: `Normal`.
        self.mode = mode
        # The pause duration in AI mode that is used to determine whether a conversational turn has ended. Unit: ms. Default value: -1.
        # 
        # - `-1`: The AI automatically determines an appropriate wait time.
        # 
        # - `0-10000`: A custom wait time. We recommend that you set this parameter to a value from 0 to 1500.
        # 
        # Note: This parameter is invalid in Normal mode.
        self.semantic_wait_duration = semantic_wait_duration
        # The list of keywords that are used to determine the end of a user\\"s conversational turn.
        self.turn_end_words = turn_end_words

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eagerness is not None:
            result['Eagerness'] = self.eagerness

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.semantic_wait_duration is not None:
            result['SemanticWaitDuration'] = self.semantic_wait_duration

        if self.turn_end_words is not None:
            result['TurnEndWords'] = self.turn_end_words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eagerness') is not None:
            self.eagerness = m.get('Eagerness')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('SemanticWaitDuration') is not None:
            self.semantic_wait_duration = m.get('SemanticWaitDuration')

        if m.get('TurnEndWords') is not None:
            self.turn_end_words = m.get('TurnEndWords')

        return self

class AIAgentOutboundCallConfigTtsConfig(DaraModel):
    def __init__(
        self,
        emotion: str = None,
        language_id: str = None,
        model_id: str = None,
        pronunciation_rules: List[main_models.AIAgentOutboundCallConfigTtsConfigPronunciationRules] = None,
        speech_rate: float = None,
        voice_id: str = None,
        voice_id_list: List[str] = None,
    ):
        # Only MiniMax is supported. The following seven emotions are supported:
        # 
        # - `happy`
        # 
        # - `sad`
        # 
        # - `angry`
        # 
        # - `fearful`
        # 
        # - `disgusted`
        # 
        # - `surprised`
        # 
        # - `calm`
        self.emotion = emotion
        # Only MiniMax is supported. The default value is empty. This parameter enhances the recognition of specific minority languages and dialects. After you set this parameter, the speech performance in the specified minority language or dialect scenarios is improved. If the minority language type is unknown, you can set this parameter to `auto` to enable the model to automatically determine the minority language type. Valid values:
        # 
        # <details>
        # 
        # <summary>
        # 
        # Supported languages
        # 
        # </summary>
        # 
        # - `Chinese`: Chinese
        # 
        # - `Chinese,Yue`: Cantonese
        # 
        # - `English`: English
        # 
        # - `Arabic`: Arabic
        # 
        # - `Russian`: Russian
        # 
        # - `Spanish`: Spanish
        # 
        # - `French`: French
        # 
        # - `Portuguese`: Portuguese
        # 
        # - `German`: German
        # 
        # - `Turkish`: Turkish
        # 
        # - `Dutch`: Dutch
        # 
        # - `Ukrainian`: Ukrainian
        # 
        # - `Vietnamese`: Vietnamese
        # 
        # - `Indonesian`: Indonesian
        # 
        # - `Japanese`: Japanese
        # 
        # - `Italian`: Italian
        # 
        # - `Korean`: Korean
        # 
        # - `Thai`: Thai
        # 
        # - `Polish`: Polish
        # 
        # - `Romanian`: Romanian
        # 
        # - `Greek`: Greek
        # 
        # - `Czech`: Czech
        # 
        # - `Finnish`: Finnish
        # 
        # - `Hindi`: Hindi
        # 
        # - `auto`: Automatic detection
        # 
        # </details>
        self.language_id = language_id
        # Only MiniMax is supported. Valid values: `speech-01-turbo` and `speech-02-turbo`.
        self.model_id = model_id
        # The TTS pronunciation rules. You can specify a maximum of 20 rules in the array. The rules are executed in sequence.
        self.pronunciation_rules = pronunciation_rules
        # This parameter is supported on all platforms. For CosyVoice, the default value is 1.0 and the valid values are 0.5 to 2.0. For MiniMax, the default value is 1.0 and the valid values are 0.5 to 2.0.
        self.speech_rate = speech_rate
        # The voice ID. The change takes effect on the next sentence. If you do not specify this parameter, the voice ID configured in the AI agent template is used. This parameter is valid only for preset TTS voices. The value can be up to 64 characters in length. For more information about the valid values, see [Intelligent speech effect samples](https://help.aliyun.com/document_detail/449563.html).
        self.voice_id = voice_id
        # The list of available voices.
        self.voice_id_list = voice_id_list

    def validate(self):
        if self.pronunciation_rules:
            for v1 in self.pronunciation_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.emotion is not None:
            result['Emotion'] = self.emotion

        if self.language_id is not None:
            result['LanguageId'] = self.language_id

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        result['PronunciationRules'] = []
        if self.pronunciation_rules is not None:
            for k1 in self.pronunciation_rules:
                result['PronunciationRules'].append(k1.to_map() if k1 else None)

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.voice_id is not None:
            result['VoiceId'] = self.voice_id

        if self.voice_id_list is not None:
            result['VoiceIdList'] = self.voice_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')

        if m.get('LanguageId') is not None:
            self.language_id = m.get('LanguageId')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        self.pronunciation_rules = []
        if m.get('PronunciationRules') is not None:
            for k1 in m.get('PronunciationRules'):
                temp_model = main_models.AIAgentOutboundCallConfigTtsConfigPronunciationRules()
                self.pronunciation_rules.append(temp_model.from_map(k1))

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        if m.get('VoiceIdList') is not None:
            self.voice_id_list = m.get('VoiceIdList')

        return self

class AIAgentOutboundCallConfigTtsConfigPronunciationRules(DaraModel):
    def __init__(
        self,
        pronunciation: str = None,
        type: str = None,
        word: str = None,
    ):
        # The target pronunciation. The pronunciation must be a Chinese character string of up to 10 characters in length and cannot contain spaces.
        self.pronunciation = pronunciation
        # The type of the pronunciation rule. Valid value:
        # 
        # - `replacement`: replaces the word with the specified pronunciation.
        self.type = type
        # The word to be replaced. The word must be a Chinese character string of up to 10 characters in length and cannot contain spaces.
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pronunciation is not None:
            result['Pronunciation'] = self.pronunciation

        if self.type is not None:
            result['Type'] = self.type

        if self.word is not None:
            result['Word'] = self.word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pronunciation') is not None:
            self.pronunciation = m.get('Pronunciation')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Word') is not None:
            self.word = m.get('Word')

        return self

class AIAgentOutboundCallConfigLlmConfig(DaraModel):
    def __init__(
        self,
        bailian_app_params: str = None,
        function_map: List[main_models.AIAgentOutboundCallConfigLlmConfigFunctionMap] = None,
        history_sync_with_tts: bool = None,
        llm_complete_reply: bool = None,
        llm_history: List[main_models.AIAgentOutboundCallConfigLlmConfigLlmHistory] = None,
        llm_history_limit: int = None,
        llm_system_prompt: str = None,
        open_aiextra_query: str = None,
        output_max_delay: str = None,
        output_min_length: int = None,
    ):
        # The parameters for Alibaba Cloud Model Studio. For more information about the parameter format, see [Alibaba Cloud Model Studio parameters](https://help.aliyun.com/document_detail/2858132.html).
        self.bailian_app_params = bailian_app_params
        # The list of function mappings, which is used to map AI agent capabilities to LLM functions. This feature is supported only when function calls are used in custom LLMs that are compatible with the OpenAI protocol.
        self.function_map = function_map
        # Specifies whether to keep the LLM message history consistent with the TTS playback content. Default value: false. If you enable this feature, the saved LLM messages are consistent with the TTS playback content.
        self.history_sync_with_tts = history_sync_with_tts
        # If you enable this feature, the system sends the complete LLM-generated result to the client after the generation is complete.
        self.llm_complete_reply = llm_complete_reply
        # The conversation history of the LLM or MLLM.
        self.llm_history = llm_history
        # The maximum number of conversational turns to retain in the history of the LLM or multimodal large language model (MLLM). Default value: 10.
        self.llm_history_limit = llm_history_limit
        # The system prompt for the LLM after the call is initiated.
        self.llm_system_prompt = llm_system_prompt
        # The additional query parameters for an LLM that is compatible with the OpenAI protocol. The parameters must be in the key=value format. If you specify multiple parameters, separate them with ampersands (`&`). All values must be of the string type.
        self.open_aiextra_query = open_aiextra_query
        # The maximum delay for text output. If this threshold is exceeded, the cached text is forcibly output. Valid values: 1000 to 10000. Unit: ms. A value of 0 or empty indicates that this parameter is not in effect. Default value: empty.
        self.output_max_delay = output_max_delay
        # The minimum length of text output. The unit is characters. Text shorter than this length is cached and waits for concatenation. Valid values: 0 to 100. A value of 0 or empty indicates that this parameter is not in effect. Default value: empty.
        self.output_min_length = output_min_length

    def validate(self):
        if self.function_map:
            for v1 in self.function_map:
                 if v1:
                    v1.validate()
        if self.llm_history:
            for v1 in self.llm_history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bailian_app_params is not None:
            result['BailianAppParams'] = self.bailian_app_params

        result['FunctionMap'] = []
        if self.function_map is not None:
            for k1 in self.function_map:
                result['FunctionMap'].append(k1.to_map() if k1 else None)

        if self.history_sync_with_tts is not None:
            result['HistorySyncWithTTS'] = self.history_sync_with_tts

        if self.llm_complete_reply is not None:
            result['LlmCompleteReply'] = self.llm_complete_reply

        result['LlmHistory'] = []
        if self.llm_history is not None:
            for k1 in self.llm_history:
                result['LlmHistory'].append(k1.to_map() if k1 else None)

        if self.llm_history_limit is not None:
            result['LlmHistoryLimit'] = self.llm_history_limit

        if self.llm_system_prompt is not None:
            result['LlmSystemPrompt'] = self.llm_system_prompt

        if self.open_aiextra_query is not None:
            result['OpenAIExtraQuery'] = self.open_aiextra_query

        if self.output_max_delay is not None:
            result['OutputMaxDelay'] = self.output_max_delay

        if self.output_min_length is not None:
            result['OutputMinLength'] = self.output_min_length

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BailianAppParams') is not None:
            self.bailian_app_params = m.get('BailianAppParams')

        self.function_map = []
        if m.get('FunctionMap') is not None:
            for k1 in m.get('FunctionMap'):
                temp_model = main_models.AIAgentOutboundCallConfigLlmConfigFunctionMap()
                self.function_map.append(temp_model.from_map(k1))

        if m.get('HistorySyncWithTTS') is not None:
            self.history_sync_with_tts = m.get('HistorySyncWithTTS')

        if m.get('LlmCompleteReply') is not None:
            self.llm_complete_reply = m.get('LlmCompleteReply')

        self.llm_history = []
        if m.get('LlmHistory') is not None:
            for k1 in m.get('LlmHistory'):
                temp_model = main_models.AIAgentOutboundCallConfigLlmConfigLlmHistory()
                self.llm_history.append(temp_model.from_map(k1))

        if m.get('LlmHistoryLimit') is not None:
            self.llm_history_limit = m.get('LlmHistoryLimit')

        if m.get('LlmSystemPrompt') is not None:
            self.llm_system_prompt = m.get('LlmSystemPrompt')

        if m.get('OpenAIExtraQuery') is not None:
            self.open_aiextra_query = m.get('OpenAIExtraQuery')

        if m.get('OutputMaxDelay') is not None:
            self.output_max_delay = m.get('OutputMaxDelay')

        if m.get('OutputMinLength') is not None:
            self.output_min_length = m.get('OutputMinLength')

        return self

class AIAgentOutboundCallConfigLlmConfigLlmHistory(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        # The text of the conversation content that records the specific expressions or responses of the role in the conversation.
        self.content = content
        # The role of the participant in the conversation. Valid values:
        # 
        # - `user`: the user
        # 
        # - `assistant`: the AI assistant
        # 
        # - `system`: the system
        # 
        # - `function`: a function
        # 
        # - `plugin`: a plug-in
        # 
        # - `tool`: a tool
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

class AIAgentOutboundCallConfigLlmConfigFunctionMap(DaraModel):
    def __init__(
        self,
        function: str = None,
        match_function: str = None,
    ):
        # The name of the built-in function provided by the AI agent in Alibaba Cloud. The value hangup is supported.
        self.function = function
        # The name of the LLM function that corresponds to this function. This parameter is customized and used to call the corresponding function in the LLM. For more information about the protocol for custom LLMs, see [Standard LLM API](https://help.aliyun.com/document_detail/2839094.html).
        self.match_function = match_function

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['Function'] = self.function

        if self.match_function is not None:
            result['MatchFunction'] = self.match_function

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            self.function = m.get('Function')

        if m.get('MatchFunction') is not None:
            self.match_function = m.get('MatchFunction')

        return self

class AIAgentOutboundCallConfigInterruptConfig(DaraModel):
    def __init__(
        self,
        eagerness: str = None,
        enable_voice_interrupt: bool = None,
        interrupt_words: List[str] = None,
        keep_interrupt_words_for_llm: bool = None,
        no_interrupt_mode: str = None,
    ):
        self.eagerness = eagerness
        # Specifies whether to support speech interruption. Default value: true.
        self.enable_voice_interrupt = enable_voice_interrupt
        # The specific words or phrases that trigger a conversation interruption.
        self.interrupt_words = interrupt_words
        self.keep_interrupt_words_for_llm = keep_interrupt_words_for_llm
        # The ASR processing policy in `NoInterruptMode`.
        # 
        # - `cache`: caches the ASR text. The cached ASR text is processed in the next conversational turn.
        # 
        # - `discard`: discards the ASR text.
        # 
        # Default value: cache.
        self.no_interrupt_mode = no_interrupt_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eagerness is not None:
            result['Eagerness'] = self.eagerness

        if self.enable_voice_interrupt is not None:
            result['EnableVoiceInterrupt'] = self.enable_voice_interrupt

        if self.interrupt_words is not None:
            result['InterruptWords'] = self.interrupt_words

        if self.keep_interrupt_words_for_llm is not None:
            result['KeepInterruptWordsForLLM'] = self.keep_interrupt_words_for_llm

        if self.no_interrupt_mode is not None:
            result['NoInterruptMode'] = self.no_interrupt_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eagerness') is not None:
            self.eagerness = m.get('Eagerness')

        if m.get('EnableVoiceInterrupt') is not None:
            self.enable_voice_interrupt = m.get('EnableVoiceInterrupt')

        if m.get('InterruptWords') is not None:
            self.interrupt_words = m.get('InterruptWords')

        if m.get('KeepInterruptWordsForLLM') is not None:
            self.keep_interrupt_words_for_llm = m.get('KeepInterruptWordsForLLM')

        if m.get('NoInterruptMode') is not None:
            self.no_interrupt_mode = m.get('NoInterruptMode')

        return self

class AIAgentOutboundCallConfigBackChannelingConfigs(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        probability: float = None,
        trigger_stage: str = None,
        words: List[main_models.AIAgentOutboundCallConfigBackChannelingConfigsWords] = None,
    ):
        # Specifies whether to enable the back-channeling feature. This parameter is required. Valid values: true and false.
        self.enabled = enabled
        # The trigger probability. This parameter is required. Valid values: 0.0 to 1.0.
        self.probability = probability
        # The trigger point for back-channeling. Valid value:
        # 
        # - `pause_detected`: triggered when a short pause in speech is detected
        self.trigger_stage = trigger_stage
        # The collection of back-channeling phrases. You can specify a maximum of 10 phrases. Each phrase can be up to 20 characters in length. The sum of the probabilities of all phrases must be 1.0.
        self.words = words

    def validate(self):
        if self.words:
            for v1 in self.words:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.probability is not None:
            result['Probability'] = self.probability

        if self.trigger_stage is not None:
            result['TriggerStage'] = self.trigger_stage

        result['Words'] = []
        if self.words is not None:
            for k1 in self.words:
                result['Words'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Probability') is not None:
            self.probability = m.get('Probability')

        if m.get('TriggerStage') is not None:
            self.trigger_stage = m.get('TriggerStage')

        self.words = []
        if m.get('Words') is not None:
            for k1 in m.get('Words'):
                temp_model = main_models.AIAgentOutboundCallConfigBackChannelingConfigsWords()
                self.words.append(temp_model.from_map(k1))

        return self

class AIAgentOutboundCallConfigBackChannelingConfigsWords(DaraModel):
    def __init__(
        self,
        probability: float = None,
        text: str = None,
    ):
        # The selection probability of this phrase. This parameter is required. Valid values: 0.0 to 1.0.
        self.probability = probability
        # The text of the phrase. This parameter is required. The text can be up to 20 characters in length and supports multiple languages.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.probability is not None:
            result['Probability'] = self.probability

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Probability') is not None:
            self.probability = m.get('Probability')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class AIAgentOutboundCallConfigBackChannelingConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        probability: float = None,
        trigger_stage: str = None,
        words: main_models.AIAgentOutboundCallConfigBackChannelingConfigWords = None,
    ):
        self.enabled = enabled
        self.probability = probability
        self.trigger_stage = trigger_stage
        self.words = words

    def validate(self):
        if self.words:
            self.words.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.probability is not None:
            result['Probability'] = self.probability

        if self.trigger_stage is not None:
            result['TriggerStage'] = self.trigger_stage

        if self.words is not None:
            result['Words'] = self.words.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Probability') is not None:
            self.probability = m.get('Probability')

        if m.get('TriggerStage') is not None:
            self.trigger_stage = m.get('TriggerStage')

        if m.get('Words') is not None:
            temp_model = main_models.AIAgentOutboundCallConfigBackChannelingConfigWords()
            self.words = temp_model.from_map(m.get('Words'))

        return self

class AIAgentOutboundCallConfigBackChannelingConfigWords(DaraModel):
    def __init__(
        self,
        probability: float = None,
        text: str = None,
    ):
        self.probability = probability
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.probability is not None:
            result['Probability'] = self.probability

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Probability') is not None:
            self.probability = m.get('Probability')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class AIAgentOutboundCallConfigAutoSpeechConfig(DaraModel):
    def __init__(
        self,
        llm_pending: main_models.AIAgentOutboundCallConfigAutoSpeechConfigLlmPending = None,
        user_idle: main_models.AIAgentOutboundCallConfigAutoSpeechConfigUserIdle = None,
    ):
        # The configurations for broadcasts during LLM response delays.
        self.llm_pending = llm_pending
        # The configurations for inquiry broadcasts during prolonged user silence.
        self.user_idle = user_idle

    def validate(self):
        if self.llm_pending:
            self.llm_pending.validate()
        if self.user_idle:
            self.user_idle.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.llm_pending is not None:
            result['LlmPending'] = self.llm_pending.to_map()

        if self.user_idle is not None:
            result['UserIdle'] = self.user_idle.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LlmPending') is not None:
            temp_model = main_models.AIAgentOutboundCallConfigAutoSpeechConfigLlmPending()
            self.llm_pending = temp_model.from_map(m.get('LlmPending'))

        if m.get('UserIdle') is not None:
            temp_model = main_models.AIAgentOutboundCallConfigAutoSpeechConfigUserIdle()
            self.user_idle = temp_model.from_map(m.get('UserIdle'))

        return self

class AIAgentOutboundCallConfigAutoSpeechConfigUserIdle(DaraModel):
    def __init__(
        self,
        hangup_end_word: str = None,
        max_repeats: int = None,
        messages: List[main_models.AIAgentOutboundCallConfigAutoSpeechConfigUserIdleMessages] = None,
        wait_time: int = None,
    ):
        self.hangup_end_word = hangup_end_word
        # The maximum number of inquiries. This parameter is required. Valid values: 0 to 10. After the maximum number of inquiries is reached, no more inquiries are triggered, and the call is disconnected.
        self.max_repeats = max_repeats
        # The collection of inquiry prompts. You can specify a maximum of 10 prompts. Each prompt can be up to 100 characters in length. The sum of the probabilities of all prompts must be 100%.
        self.messages = messages
        # The silence duration threshold. This parameter is required. An inquiry is triggered if this threshold is exceeded. Unit: ms. Valid values: 5000 to 600000.
        self.wait_time = wait_time

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hangup_end_word is not None:
            result['HangupEndWord'] = self.hangup_end_word

        if self.max_repeats is not None:
            result['MaxRepeats'] = self.max_repeats

        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        if self.wait_time is not None:
            result['WaitTime'] = self.wait_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HangupEndWord') is not None:
            self.hangup_end_word = m.get('HangupEndWord')

        if m.get('MaxRepeats') is not None:
            self.max_repeats = m.get('MaxRepeats')

        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.AIAgentOutboundCallConfigAutoSpeechConfigUserIdleMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('WaitTime') is not None:
            self.wait_time = m.get('WaitTime')

        return self

class AIAgentOutboundCallConfigAutoSpeechConfigUserIdleMessages(DaraModel):
    def __init__(
        self,
        probability: float = None,
        text: str = None,
    ):
        # The selection probability of the prompt. Valid values: 0 to 1, which corresponds to 0% to 100%.
        self.probability = probability
        # The text of the inquiry prompt. The text can be up to 100 characters in length.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.probability is not None:
            result['Probability'] = self.probability

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Probability') is not None:
            self.probability = m.get('Probability')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class AIAgentOutboundCallConfigAutoSpeechConfigLlmPending(DaraModel):
    def __init__(
        self,
        messages: List[main_models.AIAgentOutboundCallConfigAutoSpeechConfigLlmPendingMessages] = None,
        mode: str = None,
        wait_time: int = None,
    ):
        # The collection of inquiry prompts. You can specify a maximum of 10 prompts. Each prompt can be up to 100 characters in length. The sum of the probabilities of all prompts must be 100%.
        self.messages = messages
        self.mode = mode
        # The wait time threshold for LLM responses. This parameter is required. A broadcast prompt is triggered if this threshold is exceeded. Unit: ms. Valid values: 500 to 10000. You need to configure this parameter based on the actual usage of the LLM.
        self.wait_time = wait_time

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.wait_time is not None:
            result['WaitTime'] = self.wait_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.AIAgentOutboundCallConfigAutoSpeechConfigLlmPendingMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('WaitTime') is not None:
            self.wait_time = m.get('WaitTime')

        return self

class AIAgentOutboundCallConfigAutoSpeechConfigLlmPendingMessages(DaraModel):
    def __init__(
        self,
        probability: float = None,
        text: str = None,
    ):
        # The selection probability of the prompt. Valid values: 0 to 1, which corresponds to 0% to 100%.
        self.probability = probability
        # The text of the inquiry prompt. The text can be up to 100 characters in length.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.probability is not None:
            result['Probability'] = self.probability

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Probability') is not None:
            self.probability = m.get('Probability')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class AIAgentOutboundCallConfigAsrConfig(DaraModel):
    def __init__(
        self,
        asr_hot_words: List[str] = None,
        asr_language_id: str = None,
        asr_max_silence: int = None,
        custom_params: str = None,
        vad_duration: int = None,
        vad_level: int = None,
    ):
        # The list of hotwords for ASR. You can specify a maximum of 128 hotwords in the list.
        self.asr_hot_words = asr_hot_words
        # The language ID for ASR. Valid values:
        # 
        # - `zh_mandarin`: Chinese
        # 
        # - `en`: English
        # 
        # - `zh_en`: Chinese and English
        # 
        # - `es`: Spanish
        # 
        # - `jp`: Japanese
        self.asr_language_id = asr_language_id
        # The sentence segmentation threshold. If the duration of a silence exceeds this threshold, the system determines that the sentence is complete. Valid values: 200 to 1200. Unit: ms. Default value: 400.
        self.asr_max_silence = asr_max_silence
        # The passthrough parameters for proprietary ASR.
        self.custom_params = custom_params
        # The minimum duration threshold for VAD. This parameter controls the interruption sensitivity. A value of 0 indicates that this feature is disabled. Valid values: 200 to 2000. Unit: ms. A value from 200 to 500 corresponds to 1 to 4 words. The default value is empty, which indicates that this parameter is not in effect.
        self.vad_duration = vad_duration
        # The interruption threshold for voice activity detection (VAD). Valid values: 0 to 11. Default value: 11.
        # 
        # - A value of 0 disables the VAD feature.
        # 
        # - A value from 1 to 10 indicates that the higher the value, the less sensitive the interruption.
        # 
        # - A value of 11 provides a significantly different experience from the previous values. It lowers audio distortion during conversations and enhances resistance to interference.
        self.vad_level = vad_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_hot_words is not None:
            result['AsrHotWords'] = self.asr_hot_words

        if self.asr_language_id is not None:
            result['AsrLanguageId'] = self.asr_language_id

        if self.asr_max_silence is not None:
            result['AsrMaxSilence'] = self.asr_max_silence

        if self.custom_params is not None:
            result['CustomParams'] = self.custom_params

        if self.vad_duration is not None:
            result['VadDuration'] = self.vad_duration

        if self.vad_level is not None:
            result['VadLevel'] = self.vad_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrHotWords') is not None:
            self.asr_hot_words = m.get('AsrHotWords')

        if m.get('AsrLanguageId') is not None:
            self.asr_language_id = m.get('AsrLanguageId')

        if m.get('AsrMaxSilence') is not None:
            self.asr_max_silence = m.get('AsrMaxSilence')

        if m.get('CustomParams') is not None:
            self.custom_params = m.get('CustomParams')

        if m.get('VadDuration') is not None:
            self.vad_duration = m.get('VadDuration')

        if m.get('VadLevel') is not None:
            self.vad_level = m.get('VadLevel')

        return self

class AIAgentOutboundCallConfigAmbientSoundConfig(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        volume: int = None,
    ):
        # The ID of the ambient sound. You can obtain the ID from the advanced configurations of the AI agent on the console.
        self.resource_id = resource_id
        # The volume of the ambient sound. Valid values: 0 to 100. A value of 0 disables the sound.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

