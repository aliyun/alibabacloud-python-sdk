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
        self.ambient_sound_config = ambient_sound_config
        self.asr_config = asr_config
        self.auto_speech_config = auto_speech_config
        self.back_channeling_config = back_channeling_config
        self.enable_intelligent_segment = enable_intelligent_segment
        self.experimental_config = experimental_config
        self.greeting = greeting
        self.greeting_delay = greeting_delay
        self.interrupt_config = interrupt_config
        self.llm_config = llm_config
        self.max_idle_time = max_idle_time
        self.tts_config = tts_config
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
        self.mode = mode
        self.semantic_wait_duration = semantic_wait_duration
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
        self.emotion = emotion
        self.language_id = language_id
        self.model_id = model_id
        self.pronunciation_rules = pronunciation_rules
        self.speech_rate = speech_rate
        self.voice_id = voice_id
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
        self.pronunciation = pronunciation
        self.type = type
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
        self.bailian_app_params = bailian_app_params
        self.function_map = function_map
        self.history_sync_with_tts = history_sync_with_tts
        self.llm_complete_reply = llm_complete_reply
        self.llm_history = llm_history
        self.llm_history_limit = llm_history_limit
        self.llm_system_prompt = llm_system_prompt
        self.open_aiextra_query = open_aiextra_query
        self.output_max_delay = output_max_delay
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
        self.content = content
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
        self.function = function
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
        no_interrupt_mode: str = None,
    ):
        self.eagerness = eagerness
        self.enable_voice_interrupt = enable_voice_interrupt
        self.interrupt_words = interrupt_words
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

        if m.get('NoInterruptMode') is not None:
            self.no_interrupt_mode = m.get('NoInterruptMode')

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
        self.llm_pending = llm_pending
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
        max_repeats: int = None,
        messages: List[main_models.AIAgentOutboundCallConfigAutoSpeechConfigUserIdleMessages] = None,
        wait_time: int = None,
    ):
        self.max_repeats = max_repeats
        self.messages = messages
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

class AIAgentOutboundCallConfigAutoSpeechConfigLlmPending(DaraModel):
    def __init__(
        self,
        messages: List[main_models.AIAgentOutboundCallConfigAutoSpeechConfigLlmPendingMessages] = None,
        wait_time: int = None,
    ):
        self.messages = messages
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

        if m.get('WaitTime') is not None:
            self.wait_time = m.get('WaitTime')

        return self

class AIAgentOutboundCallConfigAutoSpeechConfigLlmPendingMessages(DaraModel):
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
        self.asr_hot_words = asr_hot_words
        self.asr_language_id = asr_language_id
        self.asr_max_silence = asr_max_silence
        self.custom_params = custom_params
        self.vad_duration = vad_duration
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
        self.resource_id = resource_id
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

