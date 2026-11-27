# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class ModifyAppAgentTemplateRequest(DaraModel):
    def __init__(
        self,
        agent_silence_config: main_models.ModifyAppAgentTemplateRequestAgentSilenceConfig = None,
        ambient_sound_config: main_models.ModifyAppAgentTemplateRequestAmbientSoundConfig = None,
        app_id: str = None,
        asr_config: main_models.ModifyAppAgentTemplateRequestAsrConfig = None,
        back_channel_config: main_models.ModifyAppAgentTemplateRequestBackChannelConfig = None,
        chat_mode: int = None,
        enable_video_understanding: bool = None,
        greeting: str = None,
        id: str = None,
        interrupt_config: main_models.ModifyAppAgentTemplateRequestInterruptConfig = None,
        interrupt_mode: int = None,
        llm_config: main_models.ModifyAppAgentTemplateRequestLlmConfig = None,
        name: str = None,
        prefer_video: int = None,
        tts_config: main_models.ModifyAppAgentTemplateRequestTtsConfig = None,
        type: int = None,
    ):
        # The agent silence configuration.
        self.agent_silence_config = agent_silence_config
        # The agent ambient environment configuration. If this parameter is not specified, the ambient environment configuration is not used.
        self.ambient_sound_config = ambient_sound_config
        # The application ID. You can create and query the ID in the console. Only a single ID is supported.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The speech-to-text settings.
        self.asr_config = asr_config
        # The agent backchannel configuration.
        self.back_channel_config = back_channel_config
        # The conversation mode. Valid values:
        # - 1: Natural conversation mode (default).
        # - 2: Walkie-talkie mode.
        self.chat_mode = chat_mode
        # If enabled, the LLM must support multimodal data.
        self.enable_video_understanding = enable_video_understanding
        # The greeting message. The maximum length is 500 characters.
        self.greeting = greeting
        # The template ID.
        # 
        # This parameter is required.
        self.id = id
        # The agent interruption configuration.
        self.interrupt_config = interrupt_config
        # The interruption mode. Valid values:
        # - 1: Interruption supported (default).
        # - 2: Interruption disabled.
        self.interrupt_mode = interrupt_mode
        # The large language model settings.
        self.llm_config = llm_config
        # The template name.
        # 
        # This parameter is required.
        self.name = name
        # The preferred video stream for the agent to understand after visual understanding is enabled. The agent can understand only one video stream. When both the camera stream and the screen sharing stream are pushed:
        # 
        # 1 - The agent prioritizes understanding the camera stream.
        # 
        # 2 - The agent prioritizes understanding the screen sharing stream.
        # 
        # By default, the agent prioritizes understanding the camera stream.
        self.prefer_video = prefer_video
        # The text-to-speech settings.
        self.tts_config = tts_config
        # The agent type. Valid values:
        # - 1: Voice call (default).
        self.type = type

    def validate(self):
        if self.agent_silence_config:
            self.agent_silence_config.validate()
        if self.ambient_sound_config:
            self.ambient_sound_config.validate()
        if self.asr_config:
            self.asr_config.validate()
        if self.back_channel_config:
            self.back_channel_config.validate()
        if self.interrupt_config:
            self.interrupt_config.validate()
        if self.llm_config:
            self.llm_config.validate()
        if self.tts_config:
            self.tts_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_silence_config is not None:
            result['AgentSilenceConfig'] = self.agent_silence_config.to_map()

        if self.ambient_sound_config is not None:
            result['AmbientSoundConfig'] = self.ambient_sound_config.to_map()

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.asr_config is not None:
            result['AsrConfig'] = self.asr_config.to_map()

        if self.back_channel_config is not None:
            result['BackChannelConfig'] = self.back_channel_config.to_map()

        if self.chat_mode is not None:
            result['ChatMode'] = self.chat_mode

        if self.enable_video_understanding is not None:
            result['EnableVideoUnderstanding'] = self.enable_video_understanding

        if self.greeting is not None:
            result['Greeting'] = self.greeting

        if self.id is not None:
            result['Id'] = self.id

        if self.interrupt_config is not None:
            result['InterruptConfig'] = self.interrupt_config.to_map()

        if self.interrupt_mode is not None:
            result['InterruptMode'] = self.interrupt_mode

        if self.llm_config is not None:
            result['LlmConfig'] = self.llm_config.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.prefer_video is not None:
            result['PreferVideo'] = self.prefer_video

        if self.tts_config is not None:
            result['TtsConfig'] = self.tts_config.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentSilenceConfig') is not None:
            temp_model = main_models.ModifyAppAgentTemplateRequestAgentSilenceConfig()
            self.agent_silence_config = temp_model.from_map(m.get('AgentSilenceConfig'))

        if m.get('AmbientSoundConfig') is not None:
            temp_model = main_models.ModifyAppAgentTemplateRequestAmbientSoundConfig()
            self.ambient_sound_config = temp_model.from_map(m.get('AmbientSoundConfig'))

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AsrConfig') is not None:
            temp_model = main_models.ModifyAppAgentTemplateRequestAsrConfig()
            self.asr_config = temp_model.from_map(m.get('AsrConfig'))

        if m.get('BackChannelConfig') is not None:
            temp_model = main_models.ModifyAppAgentTemplateRequestBackChannelConfig()
            self.back_channel_config = temp_model.from_map(m.get('BackChannelConfig'))

        if m.get('ChatMode') is not None:
            self.chat_mode = m.get('ChatMode')

        if m.get('EnableVideoUnderstanding') is not None:
            self.enable_video_understanding = m.get('EnableVideoUnderstanding')

        if m.get('Greeting') is not None:
            self.greeting = m.get('Greeting')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InterruptConfig') is not None:
            temp_model = main_models.ModifyAppAgentTemplateRequestInterruptConfig()
            self.interrupt_config = temp_model.from_map(m.get('InterruptConfig'))

        if m.get('InterruptMode') is not None:
            self.interrupt_mode = m.get('InterruptMode')

        if m.get('LlmConfig') is not None:
            temp_model = main_models.ModifyAppAgentTemplateRequestLlmConfig()
            self.llm_config = temp_model.from_map(m.get('LlmConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PreferVideo') is not None:
            self.prefer_video = m.get('PreferVideo')

        if m.get('TtsConfig') is not None:
            temp_model = main_models.ModifyAppAgentTemplateRequestTtsConfig()
            self.tts_config = temp_model.from_map(m.get('TtsConfig'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ModifyAppAgentTemplateRequestTtsConfig(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        filter_brackets: List[int] = None,
        name: str = None,
        pitch: float = None,
        rate: float = None,
        vendor: str = None,
        voice: str = None,
        volume: int = None,
    ):
        # The API key required by the large language model service provider.
        # 
        # This parameter is required.
        self.api_key = api_key
        # The filter brackets. Valid values:
        # - 1: Chinese parentheses （）
        # - 2: English parentheses ()
        # - 3: Chinese square brackets 【】
        # - 4: English square brackets []
        # - 5: English curly braces {}
        self.filter_brackets = filter_brackets
        # The name.
        # 
        # This parameter is required.
        self.name = name
        # The pitch. Valid values: 0.5 to 2.0. Default value: 1.0.
        self.pitch = pitch
        # The speech rate. Valid values: 0.5 to 2.0. Default value: 1.0.
        self.rate = rate
        # The provider. Alibaba Cloud Model Studio is supported.
        # 
        # This parameter is required.
        self.vendor = vendor
        # The voice. Default value: longxiaoxia. Valid values:
        # - longwan
        # - longcheng
        # - longhua
        # - longxiaochun
        # - longxiaoxia
        # - longxiaocheng
        # - longxiaobai
        # - longlaotie
        # - longshu
        # - longshuo
        # - longjing
        # - longmiao
        # - longyue
        # - longyuan
        # - longfei
        # - longjielidou
        # - longtong
        # - longxiang
        # - loongstella
        # - loongbella
        self.voice = voice
        # The volume. Valid values: 0 to 100. Default value: 50.
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

        if self.name is not None:
            result['Name'] = self.name

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

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

class ModifyAppAgentTemplateRequestLlmConfig(DaraModel):
    def __init__(
        self,
        agent_app_id: str = None,
        api_key: str = None,
        history_depth: int = None,
        max_token: int = None,
        name: str = None,
        prompt: str = None,
        temperature: float = None,
        top_p: float = None,
        url: str = None,
        vendor: str = None,
    ):
        # The ID of the Model Studio agent.
        self.agent_app_id = agent_app_id
        # The API key required by the large language model service provider.
        # 
        # This parameter is required.
        self.api_key = api_key
        # The number of historical conversation turns provided to the large language model. Maximum value: 100. Default value: 50.
        self.history_depth = history_depth
        # The maximum number of tokens for the output text. Default value: 8192.
        self.max_token = max_token
        # The name.
        # 
        # This parameter is required.
        self.name = name
        # The prompt for the large language model. The maximum length is 5,000 characters.
        self.prompt = prompt
        # The sampling temperature. Valid values: [0, 2). Default value: 0.7.
        self.temperature = temperature
        # The top-p sampling range. Valid values: (0, 1]. Default value: 0.8.
        self.top_p = top_p
        # The endpoint URL for connecting to a third-party large language model.
        self.url = url
        # The provider. Alibaba Cloud Model Studio and third-party configurations that comply with the OpenAI API specification are supported.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_app_id is not None:
            result['AgentAppId'] = self.agent_app_id

        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.history_depth is not None:
            result['HistoryDepth'] = self.history_depth

        if self.max_token is not None:
            result['MaxToken'] = self.max_token

        if self.name is not None:
            result['Name'] = self.name

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.temperature is not None:
            result['Temperature'] = self.temperature

        if self.top_p is not None:
            result['TopP'] = self.top_p

        if self.url is not None:
            result['Url'] = self.url

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentAppId') is not None:
            self.agent_app_id = m.get('AgentAppId')

        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('HistoryDepth') is not None:
            self.history_depth = m.get('HistoryDepth')

        if m.get('MaxToken') is not None:
            self.max_token = m.get('MaxToken')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')

        if m.get('TopP') is not None:
            self.top_p = m.get('TopP')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class ModifyAppAgentTemplateRequestInterruptConfig(DaraModel):
    def __init__(
        self,
        semantics_interrupt: bool = None,
    ):
        # Specifies whether to interrupt based on semantics.
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

class ModifyAppAgentTemplateRequestBackChannelConfig(DaraModel):
    def __init__(
        self,
        user_turn_end: bool = None,
    ):
        # Specifies whether to enable the backchannel.
        self.user_turn_end = user_turn_end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_turn_end is not None:
            result['UserTurnEnd'] = self.user_turn_end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserTurnEnd') is not None:
            self.user_turn_end = m.get('UserTurnEnd')

        return self

class ModifyAppAgentTemplateRequestAsrConfig(DaraModel):
    def __init__(
        self,
        max_sentence_silence: int = None,
        name: str = None,
        vad_config: main_models.ModifyAppAgentTemplateRequestAsrConfigVadConfig = None,
        vocabulary_id: str = None,
        word_weights: List[main_models.ModifyAppAgentTemplateRequestAsrConfigWordWeights] = None,
    ):
        # The speech segmentation detection threshold. The default value is 500 ms. Valid values: 200 to 6000. If VadConfig is set, we recommend that you set this value to be greater than VadConfig.InterruptSpeechDuration and less than 1500 ms.
        self.max_sentence_silence = max_sentence_silence
        # The name.
        # 
        # This parameter is required.
        self.name = name
        # The voice activity detection (VAD) configuration.
        self.vad_config = vad_config
        # The hot word ID.
        self.vocabulary_id = vocabulary_id
        # The hot word weights. Each vocabulary can contain up to 500 hot words, and each hot word can be up to 10 Chinese characters in length. Hot words must be UTF-8 encoded and cannot contain punctuation marks or special characters. Otherwise, the hot words do not take effect.
        self.word_weights = word_weights

    def validate(self):
        if self.vad_config:
            self.vad_config.validate()
        if self.word_weights:
            for v1 in self.word_weights:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_sentence_silence is not None:
            result['MaxSentenceSilence'] = self.max_sentence_silence

        if self.name is not None:
            result['Name'] = self.name

        if self.vad_config is not None:
            result['VadConfig'] = self.vad_config.to_map()

        if self.vocabulary_id is not None:
            result['VocabularyId'] = self.vocabulary_id

        result['WordWeights'] = []
        if self.word_weights is not None:
            for k1 in self.word_weights:
                result['WordWeights'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxSentenceSilence') is not None:
            self.max_sentence_silence = m.get('MaxSentenceSilence')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VadConfig') is not None:
            temp_model = main_models.ModifyAppAgentTemplateRequestAsrConfigVadConfig()
            self.vad_config = temp_model.from_map(m.get('VadConfig'))

        if m.get('VocabularyId') is not None:
            self.vocabulary_id = m.get('VocabularyId')

        self.word_weights = []
        if m.get('WordWeights') is not None:
            for k1 in m.get('WordWeights'):
                temp_model = main_models.ModifyAppAgentTemplateRequestAsrConfigWordWeights()
                self.word_weights.append(temp_model.from_map(k1))

        return self

class ModifyAppAgentTemplateRequestAsrConfigWordWeights(DaraModel):
    def __init__(
        self,
        lang: str = None,
        weight: int = None,
        word: str = None,
    ):
        # The language code. This parameter is optional. The large language model automatically identifies the language. Valid values:
        # - zh: Chinese.
        # - en: English.
        self.lang = lang
        # The hot word weight. The value must be an integer in the range of [1, 5]. Common value: 4. If the effect is not obvious, you can increase the weight. However, a large weight may cause negative effects and lead to inaccurate recognition of other words.
        # 
        # This parameter is required.
        self.weight = weight
        # The hot word text. Each word can be up to 10 Chinese characters or English words in length.
        # 
        # This parameter is required.
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.weight is not None:
            result['Weight'] = self.weight

        if self.word is not None:
            result['Word'] = self.word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        if m.get('Word') is not None:
            self.word = m.get('Word')

        return self

class ModifyAppAgentTemplateRequestAsrConfigVadConfig(DaraModel):
    def __init__(
        self,
        interrupt_speech_duration: int = None,
    ):
        # The voice duration threshold. Unit: milliseconds. Valid values: [0, 3000]. This parameter specifies the minimum duration of continuous voice signal detection to avoid false interruptions. Default value: 300.
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

class ModifyAppAgentTemplateRequestAmbientSoundConfig(DaraModel):
    def __init__(
        self,
        sound_id: str = None,
        volume: int = None,
    ):
        # The default ambient sounds provided by the agent:
        #     - white_noise 
        #     - office
        self.sound_id = sound_id
        # The volume.
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

class ModifyAppAgentTemplateRequestAgentSilenceConfig(DaraModel):
    def __init__(
        self,
        alert_timeout: int = None,
        content: str = None,
        strategy: int = None,
        webhook_trigger_timeout: int = None,
    ):
        # The timeout period for silence alerts, in seconds. This alert can be triggered multiple times. If the agent remains silent after the silence alert times out, the alert is triggered again upon the next timeout. Valid values: 5 to 600. Default value: 0. A value of 0 indicates that no alert is sent.
        self.alert_timeout = alert_timeout
        # The content of the silence prompt message.
        self.content = content
        # The silence timeout handling strategy. Valid values:
        # - 1: Broadcast the prompt message specified by Content to the user via voice.
        # - 2: Send the prompt message specified by Content and the conversation history to the LLM, and broadcast the reply generated by the model.
        # Default value: 1.
        self.strategy = strategy
        # The silence timeout period for triggering the agent silence timeout webhook, in seconds. This webhook can be triggered multiple times. If the agent remains silent after the webhook silence timeout, the webhook is triggered again upon the next timeout. Valid values: 10 to 600. Default value: 0. A value of 0 indicates that the webhook is not triggered.
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

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        if m.get('WebhookTriggerTimeout') is not None:
            self.webhook_trigger_timeout = m.get('WebhookTriggerTimeout')

        return self

