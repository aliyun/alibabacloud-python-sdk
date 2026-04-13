# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class StartAgentRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        rtc_config: main_models.StartAgentRequestRtcConfig = None,
        task_id: str = None,
        template_id: str = None,
        voice_chat_config: main_models.StartAgentRequestVoiceChatConfig = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.rtc_config = rtc_config
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.template_id = template_id
        self.voice_chat_config = voice_chat_config

    def validate(self):
        if self.rtc_config:
            self.rtc_config.validate()
        if self.voice_chat_config:
            self.voice_chat_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.rtc_config is not None:
            result['RtcConfig'] = self.rtc_config.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.voice_chat_config is not None:
            result['VoiceChatConfig'] = self.voice_chat_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('RtcConfig') is not None:
            temp_model = main_models.StartAgentRequestRtcConfig()
            self.rtc_config = temp_model.from_map(m.get('RtcConfig'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('VoiceChatConfig') is not None:
            temp_model = main_models.StartAgentRequestVoiceChatConfig()
            self.voice_chat_config = temp_model.from_map(m.get('VoiceChatConfig'))

        return self

class StartAgentRequestVoiceChatConfig(DaraModel):
    def __init__(
        self,
        asrconfig: main_models.StartAgentRequestVoiceChatConfigASRConfig = None,
        agent_silence_config: main_models.StartAgentRequestVoiceChatConfigAgentSilenceConfig = None,
        ambient_sound_config: main_models.StartAgentRequestVoiceChatConfigAmbientSoundConfig = None,
        back_channel_config: main_models.StartAgentRequestVoiceChatConfigBackChannelConfig = None,
        chat_mode: int = None,
        enable_video_understanding: bool = None,
        greeting: str = None,
        interrupt_config: main_models.StartAgentRequestVoiceChatConfigInterruptConfig = None,
        interrupt_mode: int = None,
        llmconfig: main_models.StartAgentRequestVoiceChatConfigLLMConfig = None,
        ttsconfig: main_models.StartAgentRequestVoiceChatConfigTTSConfig = None,
        prefer_video: int = None,
    ):
        self.asrconfig = asrconfig
        self.agent_silence_config = agent_silence_config
        self.ambient_sound_config = ambient_sound_config
        self.back_channel_config = back_channel_config
        self.chat_mode = chat_mode
        self.enable_video_understanding = enable_video_understanding
        self.greeting = greeting
        self.interrupt_config = interrupt_config
        self.interrupt_mode = interrupt_mode
        self.llmconfig = llmconfig
        self.ttsconfig = ttsconfig
        self.prefer_video = prefer_video

    def validate(self):
        if self.asrconfig:
            self.asrconfig.validate()
        if self.agent_silence_config:
            self.agent_silence_config.validate()
        if self.ambient_sound_config:
            self.ambient_sound_config.validate()
        if self.back_channel_config:
            self.back_channel_config.validate()
        if self.interrupt_config:
            self.interrupt_config.validate()
        if self.llmconfig:
            self.llmconfig.validate()
        if self.ttsconfig:
            self.ttsconfig.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asrconfig is not None:
            result['ASRConfig'] = self.asrconfig.to_map()

        if self.agent_silence_config is not None:
            result['AgentSilenceConfig'] = self.agent_silence_config.to_map()

        if self.ambient_sound_config is not None:
            result['AmbientSoundConfig'] = self.ambient_sound_config.to_map()

        if self.back_channel_config is not None:
            result['BackChannelConfig'] = self.back_channel_config.to_map()

        if self.chat_mode is not None:
            result['ChatMode'] = self.chat_mode

        if self.enable_video_understanding is not None:
            result['EnableVideoUnderstanding'] = self.enable_video_understanding

        if self.greeting is not None:
            result['Greeting'] = self.greeting

        if self.interrupt_config is not None:
            result['InterruptConfig'] = self.interrupt_config.to_map()

        if self.interrupt_mode is not None:
            result['InterruptMode'] = self.interrupt_mode

        if self.llmconfig is not None:
            result['LLMConfig'] = self.llmconfig.to_map()

        if self.ttsconfig is not None:
            result['TTSConfig'] = self.ttsconfig.to_map()

        if self.prefer_video is not None:
            result['preferVideo'] = self.prefer_video

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ASRConfig') is not None:
            temp_model = main_models.StartAgentRequestVoiceChatConfigASRConfig()
            self.asrconfig = temp_model.from_map(m.get('ASRConfig'))

        if m.get('AgentSilenceConfig') is not None:
            temp_model = main_models.StartAgentRequestVoiceChatConfigAgentSilenceConfig()
            self.agent_silence_config = temp_model.from_map(m.get('AgentSilenceConfig'))

        if m.get('AmbientSoundConfig') is not None:
            temp_model = main_models.StartAgentRequestVoiceChatConfigAmbientSoundConfig()
            self.ambient_sound_config = temp_model.from_map(m.get('AmbientSoundConfig'))

        if m.get('BackChannelConfig') is not None:
            temp_model = main_models.StartAgentRequestVoiceChatConfigBackChannelConfig()
            self.back_channel_config = temp_model.from_map(m.get('BackChannelConfig'))

        if m.get('ChatMode') is not None:
            self.chat_mode = m.get('ChatMode')

        if m.get('EnableVideoUnderstanding') is not None:
            self.enable_video_understanding = m.get('EnableVideoUnderstanding')

        if m.get('Greeting') is not None:
            self.greeting = m.get('Greeting')

        if m.get('InterruptConfig') is not None:
            temp_model = main_models.StartAgentRequestVoiceChatConfigInterruptConfig()
            self.interrupt_config = temp_model.from_map(m.get('InterruptConfig'))

        if m.get('InterruptMode') is not None:
            self.interrupt_mode = m.get('InterruptMode')

        if m.get('LLMConfig') is not None:
            temp_model = main_models.StartAgentRequestVoiceChatConfigLLMConfig()
            self.llmconfig = temp_model.from_map(m.get('LLMConfig'))

        if m.get('TTSConfig') is not None:
            temp_model = main_models.StartAgentRequestVoiceChatConfigTTSConfig()
            self.ttsconfig = temp_model.from_map(m.get('TTSConfig'))

        if m.get('preferVideo') is not None:
            self.prefer_video = m.get('preferVideo')

        return self

class StartAgentRequestVoiceChatConfigTTSConfig(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        filter_brackets: List[int] = None,
        model: str = None,
        pitch: float = None,
        rate: float = None,
        vendor: str = None,
        voice: str = None,
        volume: int = None,
    ):
        self.api_key = api_key
        self.filter_brackets = filter_brackets
        self.model = model
        self.pitch = pitch
        self.rate = rate
        self.vendor = vendor
        self.voice = voice
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.filter_brackets is not None:
            result['FilterBrackets'] = self.filter_brackets

        if self.model is not None:
            result['Model'] = self.model

        if self.pitch is not None:
            result['Pitch'] = self.pitch

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        if self.voice is not None:
            result['Voice'] = self.voice

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('FilterBrackets') is not None:
            self.filter_brackets = m.get('FilterBrackets')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class StartAgentRequestVoiceChatConfigLLMConfig(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        app_id: str = None,
        biz_params: Any = None,
        history_depth: int = None,
        max_token: int = None,
        model: str = None,
        params: Dict[str, Any] = None,
        prompt: str = None,
        temperature: float = None,
        tool_execution_config: Any = None,
        tools: List[Any] = None,
        top_p: float = None,
        url: str = None,
        vendor: str = None,
    ):
        self.api_key = api_key
        self.app_id = app_id
        self.biz_params = biz_params
        self.history_depth = history_depth
        self.max_token = max_token
        self.model = model
        self.params = params
        self.prompt = prompt
        self.temperature = temperature
        self.tool_execution_config = tool_execution_config
        self.tools = tools
        self.top_p = top_p
        self.url = url
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.biz_params is not None:
            result['BizParams'] = self.biz_params

        if self.history_depth is not None:
            result['HistoryDepth'] = self.history_depth

        if self.max_token is not None:
            result['MaxToken'] = self.max_token

        if self.model is not None:
            result['Model'] = self.model

        if self.params is not None:
            result['Params'] = self.params

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.temperature is not None:
            result['Temperature'] = self.temperature

        if self.tool_execution_config is not None:
            result['ToolExecutionConfig'] = self.tool_execution_config

        if self.tools is not None:
            result['Tools'] = self.tools

        if self.top_p is not None:
            result['TopP'] = self.top_p

        if self.url is not None:
            result['Url'] = self.url

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BizParams') is not None:
            self.biz_params = m.get('BizParams')

        if m.get('HistoryDepth') is not None:
            self.history_depth = m.get('HistoryDepth')

        if m.get('MaxToken') is not None:
            self.max_token = m.get('MaxToken')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')

        if m.get('ToolExecutionConfig') is not None:
            self.tool_execution_config = m.get('ToolExecutionConfig')

        if m.get('Tools') is not None:
            self.tools = m.get('Tools')

        if m.get('TopP') is not None:
            self.top_p = m.get('TopP')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class StartAgentRequestVoiceChatConfigInterruptConfig(DaraModel):
    def __init__(
        self,
        semantics_interrupt: bool = None,
    ):
        self.semantics_interrupt = semantics_interrupt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.semantics_interrupt is not None:
            result['SemanticsInterrupt'] = self.semantics_interrupt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SemanticsInterrupt') is not None:
            self.semantics_interrupt = m.get('SemanticsInterrupt')

        return self

class StartAgentRequestVoiceChatConfigBackChannelConfig(DaraModel):
    def __init__(
        self,
        user_turn_end: bool = None,
        version: int = None,
    ):
        self.user_turn_end = user_turn_end
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_turn_end is not None:
            result['UserTurnEnd'] = self.user_turn_end

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserTurnEnd') is not None:
            self.user_turn_end = m.get('UserTurnEnd')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class StartAgentRequestVoiceChatConfigAmbientSoundConfig(DaraModel):
    def __init__(
        self,
        sound_id: str = None,
        volume: int = None,
    ):
        self.sound_id = sound_id
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sound_id is not None:
            result['SoundId'] = self.sound_id

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SoundId') is not None:
            self.sound_id = m.get('SoundId')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class StartAgentRequestVoiceChatConfigAgentSilenceConfig(DaraModel):
    def __init__(
        self,
        alert_timeout: int = None,
        content: str = None,
        enable: bool = None,
        strategy: int = None,
        webhook_trigger_timeout: int = None,
    ):
        self.alert_timeout = alert_timeout
        self.content = content
        self.enable = enable
        self.strategy = strategy
        self.webhook_trigger_timeout = webhook_trigger_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_timeout is not None:
            result['AlertTimeout'] = self.alert_timeout

        if self.content is not None:
            result['Content'] = self.content

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        if self.webhook_trigger_timeout is not None:
            result['WebhookTriggerTimeout'] = self.webhook_trigger_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTimeout') is not None:
            self.alert_timeout = m.get('AlertTimeout')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        if m.get('WebhookTriggerTimeout') is not None:
            self.webhook_trigger_timeout = m.get('WebhookTriggerTimeout')

        return self

class StartAgentRequestVoiceChatConfigASRConfig(DaraModel):
    def __init__(
        self,
        language_hints: List[str] = None,
        max_sentence_silence: int = None,
        semantic_punctuation_enabled: bool = None,
        source_language: str = None,
        vad_config: main_models.StartAgentRequestVoiceChatConfigASRConfigVadConfig = None,
        vocabulary_id: str = None,
    ):
        self.language_hints = language_hints
        self.max_sentence_silence = max_sentence_silence
        self.semantic_punctuation_enabled = semantic_punctuation_enabled
        self.source_language = source_language
        self.vad_config = vad_config
        self.vocabulary_id = vocabulary_id

    def validate(self):
        if self.vad_config:
            self.vad_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language_hints is not None:
            result['LanguageHints'] = self.language_hints

        if self.max_sentence_silence is not None:
            result['MaxSentenceSilence'] = self.max_sentence_silence

        if self.semantic_punctuation_enabled is not None:
            result['SemanticPunctuationEnabled'] = self.semantic_punctuation_enabled

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.vad_config is not None:
            result['VadConfig'] = self.vad_config.to_map()

        if self.vocabulary_id is not None:
            result['VocabularyId'] = self.vocabulary_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LanguageHints') is not None:
            self.language_hints = m.get('LanguageHints')

        if m.get('MaxSentenceSilence') is not None:
            self.max_sentence_silence = m.get('MaxSentenceSilence')

        if m.get('SemanticPunctuationEnabled') is not None:
            self.semantic_punctuation_enabled = m.get('SemanticPunctuationEnabled')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('VadConfig') is not None:
            temp_model = main_models.StartAgentRequestVoiceChatConfigASRConfigVadConfig()
            self.vad_config = temp_model.from_map(m.get('VadConfig'))

        if m.get('VocabularyId') is not None:
            self.vocabulary_id = m.get('VocabularyId')

        return self

class StartAgentRequestVoiceChatConfigASRConfigVadConfig(DaraModel):
    def __init__(
        self,
        interrupt_speech_duration: int = None,
    ):
        self.interrupt_speech_duration = interrupt_speech_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interrupt_speech_duration is not None:
            result['InterruptSpeechDuration'] = self.interrupt_speech_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InterruptSpeechDuration') is not None:
            self.interrupt_speech_duration = m.get('InterruptSpeechDuration')

        return self

class StartAgentRequestRtcConfig(DaraModel):
    def __init__(
        self,
        target_user_ids: List[str] = None,
        user_id: str = None,
        user_inactivity_timeout: int = None,
    ):
        self.target_user_ids = target_user_ids
        # This parameter is required.
        self.user_id = user_id
        self.user_inactivity_timeout = user_inactivity_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_user_ids is not None:
            result['TargetUserIds'] = self.target_user_ids

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_inactivity_timeout is not None:
            result['UserInactivityTimeout'] = self.user_inactivity_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetUserIds') is not None:
            self.target_user_ids = m.get('TargetUserIds')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserInactivityTimeout') is not None:
            self.user_inactivity_timeout = m.get('UserInactivityTimeout')

        return self

