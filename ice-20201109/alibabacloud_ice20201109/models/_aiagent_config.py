# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class AIAgentConfig(DaraModel):
    def __init__(
        self,
        ambient_sound_config: main_models.AIAgentConfigAmbientSoundConfig = None,
        asr_config: main_models.AIAgentConfigAsrConfig = None,
        auto_speech_config: main_models.AIAgentConfigAutoSpeechConfig = None,
        avatar_config: main_models.AIAgentConfigAvatarConfig = None,
        avatar_url: str = None,
        avatar_url_type: str = None,
        back_channeling_config: List[main_models.AIAgentConfigBackChannelingConfig] = None,
        enable_intelligent_segment: bool = None,
        enable_push_to_talk: bool = None,
        experimental_config: str = None,
        graceful_shutdown: bool = None,
        greeting: str = None,
        interrupt_config: main_models.AIAgentConfigInterruptConfig = None,
        llm_config: main_models.AIAgentConfigLlmConfig = None,
        max_idle_time: int = None,
        tts_config: main_models.AIAgentConfigTtsConfig = None,
        turn_detection_config: main_models.AIAgentConfigTurnDetectionConfig = None,
        user_offline_timeout: int = None,
        user_online_timeout: int = None,
        vcr_config: main_models.AIAgentConfigVcrConfig = None,
        voiceprint_config: main_models.AIAgentConfigVoiceprintConfig = None,
        volume: int = None,
        wake_up_query: str = None,
        workflow_override_params: str = None,
    ):
        self.ambient_sound_config = ambient_sound_config
        self.asr_config = asr_config
        self.auto_speech_config = auto_speech_config
        self.avatar_config = avatar_config
        self.avatar_url = avatar_url
        self.avatar_url_type = avatar_url_type
        self.back_channeling_config = back_channeling_config
        self.enable_intelligent_segment = enable_intelligent_segment
        self.enable_push_to_talk = enable_push_to_talk
        self.experimental_config = experimental_config
        self.graceful_shutdown = graceful_shutdown
        self.greeting = greeting
        self.interrupt_config = interrupt_config
        self.llm_config = llm_config
        self.max_idle_time = max_idle_time
        self.tts_config = tts_config
        self.turn_detection_config = turn_detection_config
        self.user_offline_timeout = user_offline_timeout
        self.user_online_timeout = user_online_timeout
        self.vcr_config = vcr_config
        self.voiceprint_config = voiceprint_config
        self.volume = volume
        self.wake_up_query = wake_up_query
        self.workflow_override_params = workflow_override_params

    def validate(self):
        if self.ambient_sound_config:
            self.ambient_sound_config.validate()
        if self.asr_config:
            self.asr_config.validate()
        if self.auto_speech_config:
            self.auto_speech_config.validate()
        if self.avatar_config:
            self.avatar_config.validate()
        if self.back_channeling_config:
            for v1 in self.back_channeling_config:
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
        if self.vcr_config:
            self.vcr_config.validate()
        if self.voiceprint_config:
            self.voiceprint_config.validate()

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

        if self.avatar_config is not None:
            result['AvatarConfig'] = self.avatar_config.to_map()

        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url

        if self.avatar_url_type is not None:
            result['AvatarUrlType'] = self.avatar_url_type

        result['BackChannelingConfig'] = []
        if self.back_channeling_config is not None:
            for k1 in self.back_channeling_config:
                result['BackChannelingConfig'].append(k1.to_map() if k1 else None)

        if self.enable_intelligent_segment is not None:
            result['EnableIntelligentSegment'] = self.enable_intelligent_segment

        if self.enable_push_to_talk is not None:
            result['EnablePushToTalk'] = self.enable_push_to_talk

        if self.experimental_config is not None:
            result['ExperimentalConfig'] = self.experimental_config

        if self.graceful_shutdown is not None:
            result['GracefulShutdown'] = self.graceful_shutdown

        if self.greeting is not None:
            result['Greeting'] = self.greeting

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

        if self.user_offline_timeout is not None:
            result['UserOfflineTimeout'] = self.user_offline_timeout

        if self.user_online_timeout is not None:
            result['UserOnlineTimeout'] = self.user_online_timeout

        if self.vcr_config is not None:
            result['VcrConfig'] = self.vcr_config.to_map()

        if self.voiceprint_config is not None:
            result['VoiceprintConfig'] = self.voiceprint_config.to_map()

        if self.volume is not None:
            result['Volume'] = self.volume

        if self.wake_up_query is not None:
            result['WakeUpQuery'] = self.wake_up_query

        if self.workflow_override_params is not None:
            result['WorkflowOverrideParams'] = self.workflow_override_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AmbientSoundConfig') is not None:
            temp_model = main_models.AIAgentConfigAmbientSoundConfig()
            self.ambient_sound_config = temp_model.from_map(m.get('AmbientSoundConfig'))

        if m.get('AsrConfig') is not None:
            temp_model = main_models.AIAgentConfigAsrConfig()
            self.asr_config = temp_model.from_map(m.get('AsrConfig'))

        if m.get('AutoSpeechConfig') is not None:
            temp_model = main_models.AIAgentConfigAutoSpeechConfig()
            self.auto_speech_config = temp_model.from_map(m.get('AutoSpeechConfig'))

        if m.get('AvatarConfig') is not None:
            temp_model = main_models.AIAgentConfigAvatarConfig()
            self.avatar_config = temp_model.from_map(m.get('AvatarConfig'))

        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')

        if m.get('AvatarUrlType') is not None:
            self.avatar_url_type = m.get('AvatarUrlType')

        self.back_channeling_config = []
        if m.get('BackChannelingConfig') is not None:
            for k1 in m.get('BackChannelingConfig'):
                temp_model = main_models.AIAgentConfigBackChannelingConfig()
                self.back_channeling_config.append(temp_model.from_map(k1))

        if m.get('EnableIntelligentSegment') is not None:
            self.enable_intelligent_segment = m.get('EnableIntelligentSegment')

        if m.get('EnablePushToTalk') is not None:
            self.enable_push_to_talk = m.get('EnablePushToTalk')

        if m.get('ExperimentalConfig') is not None:
            self.experimental_config = m.get('ExperimentalConfig')

        if m.get('GracefulShutdown') is not None:
            self.graceful_shutdown = m.get('GracefulShutdown')

        if m.get('Greeting') is not None:
            self.greeting = m.get('Greeting')

        if m.get('InterruptConfig') is not None:
            temp_model = main_models.AIAgentConfigInterruptConfig()
            self.interrupt_config = temp_model.from_map(m.get('InterruptConfig'))

        if m.get('LlmConfig') is not None:
            temp_model = main_models.AIAgentConfigLlmConfig()
            self.llm_config = temp_model.from_map(m.get('LlmConfig'))

        if m.get('MaxIdleTime') is not None:
            self.max_idle_time = m.get('MaxIdleTime')

        if m.get('TtsConfig') is not None:
            temp_model = main_models.AIAgentConfigTtsConfig()
            self.tts_config = temp_model.from_map(m.get('TtsConfig'))

        if m.get('TurnDetectionConfig') is not None:
            temp_model = main_models.AIAgentConfigTurnDetectionConfig()
            self.turn_detection_config = temp_model.from_map(m.get('TurnDetectionConfig'))

        if m.get('UserOfflineTimeout') is not None:
            self.user_offline_timeout = m.get('UserOfflineTimeout')

        if m.get('UserOnlineTimeout') is not None:
            self.user_online_timeout = m.get('UserOnlineTimeout')

        if m.get('VcrConfig') is not None:
            temp_model = main_models.AIAgentConfigVcrConfig()
            self.vcr_config = temp_model.from_map(m.get('VcrConfig'))

        if m.get('VoiceprintConfig') is not None:
            temp_model = main_models.AIAgentConfigVoiceprintConfig()
            self.voiceprint_config = temp_model.from_map(m.get('VoiceprintConfig'))

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        if m.get('WakeUpQuery') is not None:
            self.wake_up_query = m.get('WakeUpQuery')

        if m.get('WorkflowOverrideParams') is not None:
            self.workflow_override_params = m.get('WorkflowOverrideParams')

        return self

class AIAgentConfigVoiceprintConfig(DaraModel):
    def __init__(
        self,
        use_voiceprint: bool = None,
        voiceprint_id: str = None,
    ):
        self.use_voiceprint = use_voiceprint
        self.voiceprint_id = voiceprint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.use_voiceprint is not None:
            result['UseVoiceprint'] = self.use_voiceprint

        if self.voiceprint_id is not None:
            result['VoiceprintId'] = self.voiceprint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UseVoiceprint') is not None:
            self.use_voiceprint = m.get('UseVoiceprint')

        if m.get('VoiceprintId') is not None:
            self.voiceprint_id = m.get('VoiceprintId')

        return self

class AIAgentConfigVcrConfig(DaraModel):
    def __init__(
        self,
        equipment: main_models.AIAgentConfigVcrConfigEquipment = None,
        head_motion: main_models.AIAgentConfigVcrConfigHeadMotion = None,
        invalid_frame_motion: main_models.AIAgentConfigVcrConfigInvalidFrameMotion = None,
        look_away: main_models.AIAgentConfigVcrConfigLookAway = None,
        people_count: main_models.AIAgentConfigVcrConfigPeopleCount = None,
        still_frame_motion: main_models.AIAgentConfigVcrConfigStillFrameMotion = None,
    ):
        self.equipment = equipment
        self.head_motion = head_motion
        self.invalid_frame_motion = invalid_frame_motion
        self.look_away = look_away
        self.people_count = people_count
        self.still_frame_motion = still_frame_motion

    def validate(self):
        if self.equipment:
            self.equipment.validate()
        if self.head_motion:
            self.head_motion.validate()
        if self.invalid_frame_motion:
            self.invalid_frame_motion.validate()
        if self.look_away:
            self.look_away.validate()
        if self.people_count:
            self.people_count.validate()
        if self.still_frame_motion:
            self.still_frame_motion.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.equipment is not None:
            result['Equipment'] = self.equipment.to_map()

        if self.head_motion is not None:
            result['HeadMotion'] = self.head_motion.to_map()

        if self.invalid_frame_motion is not None:
            result['InvalidFrameMotion'] = self.invalid_frame_motion.to_map()

        if self.look_away is not None:
            result['LookAway'] = self.look_away.to_map()

        if self.people_count is not None:
            result['PeopleCount'] = self.people_count.to_map()

        if self.still_frame_motion is not None:
            result['StillFrameMotion'] = self.still_frame_motion.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Equipment') is not None:
            temp_model = main_models.AIAgentConfigVcrConfigEquipment()
            self.equipment = temp_model.from_map(m.get('Equipment'))

        if m.get('HeadMotion') is not None:
            temp_model = main_models.AIAgentConfigVcrConfigHeadMotion()
            self.head_motion = temp_model.from_map(m.get('HeadMotion'))

        if m.get('InvalidFrameMotion') is not None:
            temp_model = main_models.AIAgentConfigVcrConfigInvalidFrameMotion()
            self.invalid_frame_motion = temp_model.from_map(m.get('InvalidFrameMotion'))

        if m.get('LookAway') is not None:
            temp_model = main_models.AIAgentConfigVcrConfigLookAway()
            self.look_away = temp_model.from_map(m.get('LookAway'))

        if m.get('PeopleCount') is not None:
            temp_model = main_models.AIAgentConfigVcrConfigPeopleCount()
            self.people_count = temp_model.from_map(m.get('PeopleCount'))

        if m.get('StillFrameMotion') is not None:
            temp_model = main_models.AIAgentConfigVcrConfigStillFrameMotion()
            self.still_frame_motion = temp_model.from_map(m.get('StillFrameMotion'))

        return self

class AIAgentConfigVcrConfigStillFrameMotion(DaraModel):
    def __init__(
        self,
        callback_delay: int = None,
        enabled: bool = None,
    ):
        self.callback_delay = callback_delay
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_delay is not None:
            result['CallbackDelay'] = self.callback_delay

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackDelay') is not None:
            self.callback_delay = m.get('CallbackDelay')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

class AIAgentConfigVcrConfigPeopleCount(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

class AIAgentConfigVcrConfigLookAway(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

class AIAgentConfigVcrConfigInvalidFrameMotion(DaraModel):
    def __init__(
        self,
        callback_delay: int = None,
        enabled: bool = None,
    ):
        self.callback_delay = callback_delay
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_delay is not None:
            result['CallbackDelay'] = self.callback_delay

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackDelay') is not None:
            self.callback_delay = m.get('CallbackDelay')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

class AIAgentConfigVcrConfigHeadMotion(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

class AIAgentConfigVcrConfigEquipment(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

class AIAgentConfigTurnDetectionConfig(DaraModel):
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

class AIAgentConfigTtsConfig(DaraModel):
    def __init__(
        self,
        emotion: str = None,
        language_id: str = None,
        model_id: str = None,
        pronunciation_rules: List[main_models.AIAgentConfigTtsConfigPronunciationRules] = None,
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
                temp_model = main_models.AIAgentConfigTtsConfigPronunciationRules()
                self.pronunciation_rules.append(temp_model.from_map(k1))

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        if m.get('VoiceIdList') is not None:
            self.voice_id_list = m.get('VoiceIdList')

        return self

class AIAgentConfigTtsConfigPronunciationRules(DaraModel):
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

class AIAgentConfigLlmConfig(DaraModel):
    def __init__(
        self,
        bailian_app_params: str = None,
        function_map: List[main_models.AIAgentConfigLlmConfigFunctionMap] = None,
        history_sync_with_tts: bool = None,
        llm_complete_reply: bool = None,
        llm_history: List[main_models.AIAgentConfigLlmConfigLlmHistory] = None,
        llm_history_limit: int = None,
        llm_system_prompt: str = None,
        open_aiextra_query: str = None,
        output_max_delay: int = None,
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
                temp_model = main_models.AIAgentConfigLlmConfigFunctionMap()
                self.function_map.append(temp_model.from_map(k1))

        if m.get('HistorySyncWithTTS') is not None:
            self.history_sync_with_tts = m.get('HistorySyncWithTTS')

        if m.get('LlmCompleteReply') is not None:
            self.llm_complete_reply = m.get('LlmCompleteReply')

        self.llm_history = []
        if m.get('LlmHistory') is not None:
            for k1 in m.get('LlmHistory'):
                temp_model = main_models.AIAgentConfigLlmConfigLlmHistory()
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

class AIAgentConfigLlmConfigLlmHistory(DaraModel):
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

class AIAgentConfigLlmConfigFunctionMap(DaraModel):
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

class AIAgentConfigInterruptConfig(DaraModel):
    def __init__(
        self,
        enable_voice_interrupt: bool = None,
        interrupt_words: List[str] = None,
        no_interrupt_mode: str = None,
    ):
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
        if self.enable_voice_interrupt is not None:
            result['EnableVoiceInterrupt'] = self.enable_voice_interrupt

        if self.interrupt_words is not None:
            result['InterruptWords'] = self.interrupt_words

        if self.no_interrupt_mode is not None:
            result['NoInterruptMode'] = self.no_interrupt_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableVoiceInterrupt') is not None:
            self.enable_voice_interrupt = m.get('EnableVoiceInterrupt')

        if m.get('InterruptWords') is not None:
            self.interrupt_words = m.get('InterruptWords')

        if m.get('NoInterruptMode') is not None:
            self.no_interrupt_mode = m.get('NoInterruptMode')

        return self

class AIAgentConfigBackChannelingConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        probability: float = None,
        trigger_stage: str = None,
        words: List[main_models.AIAgentConfigBackChannelingConfigWords] = None,
    ):
        self.enabled = enabled
        self.probability = probability
        self.trigger_stage = trigger_stage
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
                temp_model = main_models.AIAgentConfigBackChannelingConfigWords()
                self.words.append(temp_model.from_map(k1))

        return self

class AIAgentConfigBackChannelingConfigWords(DaraModel):
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

class AIAgentConfigAvatarConfig(DaraModel):
    def __init__(
        self,
        avatar_id: str = None,
    ):
        self.avatar_id = avatar_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_id is not None:
            result['AvatarId'] = self.avatar_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarId') is not None:
            self.avatar_id = m.get('AvatarId')

        return self

class AIAgentConfigAutoSpeechConfig(DaraModel):
    def __init__(
        self,
        llm_pending: main_models.AIAgentConfigAutoSpeechConfigLlmPending = None,
        user_idle: main_models.AIAgentConfigAutoSpeechConfigUserIdle = None,
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
            temp_model = main_models.AIAgentConfigAutoSpeechConfigLlmPending()
            self.llm_pending = temp_model.from_map(m.get('LlmPending'))

        if m.get('UserIdle') is not None:
            temp_model = main_models.AIAgentConfigAutoSpeechConfigUserIdle()
            self.user_idle = temp_model.from_map(m.get('UserIdle'))

        return self

class AIAgentConfigAutoSpeechConfigUserIdle(DaraModel):
    def __init__(
        self,
        max_repeats: int = None,
        messages: List[main_models.AIAgentConfigAutoSpeechConfigUserIdleMessages] = None,
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
                temp_model = main_models.AIAgentConfigAutoSpeechConfigUserIdleMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('WaitTime') is not None:
            self.wait_time = m.get('WaitTime')

        return self

class AIAgentConfigAutoSpeechConfigUserIdleMessages(DaraModel):
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

class AIAgentConfigAutoSpeechConfigLlmPending(DaraModel):
    def __init__(
        self,
        messages: List[main_models.AIAgentConfigAutoSpeechConfigLlmPendingMessages] = None,
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
                temp_model = main_models.AIAgentConfigAutoSpeechConfigLlmPendingMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('WaitTime') is not None:
            self.wait_time = m.get('WaitTime')

        return self

class AIAgentConfigAutoSpeechConfigLlmPendingMessages(DaraModel):
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

class AIAgentConfigAsrConfig(DaraModel):
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



class AIAgentConfigAmbientSoundConfig(DaraModel):
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

