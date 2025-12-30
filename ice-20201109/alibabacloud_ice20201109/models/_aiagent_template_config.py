# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class AIAgentTemplateConfig(DaraModel):
    def __init__(
        self,
        avatar_chat_3d: main_models.AIAgentTemplateConfigAvatarChat3D = None,
        vision_chat: main_models.AIAgentTemplateConfigVisionChat = None,
        voice_chat: main_models.AIAgentTemplateConfigVoiceChat = None,
    ):
        self.avatar_chat_3d = avatar_chat_3d
        self.vision_chat = vision_chat
        self.voice_chat = voice_chat

    def validate(self):
        if self.avatar_chat_3d:
            self.avatar_chat_3d.validate()
        if self.vision_chat:
            self.vision_chat.validate()
        if self.voice_chat:
            self.voice_chat.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_chat_3d is not None:
            result['AvatarChat3D'] = self.avatar_chat_3d.to_map()

        if self.vision_chat is not None:
            result['VisionChat'] = self.vision_chat.to_map()

        if self.voice_chat is not None:
            result['VoiceChat'] = self.voice_chat.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarChat3D') is not None:
            temp_model = main_models.AIAgentTemplateConfigAvatarChat3D()
            self.avatar_chat_3d = temp_model.from_map(m.get('AvatarChat3D'))

        if m.get('VisionChat') is not None:
            temp_model = main_models.AIAgentTemplateConfigVisionChat()
            self.vision_chat = temp_model.from_map(m.get('VisionChat'))

        if m.get('VoiceChat') is not None:
            temp_model = main_models.AIAgentTemplateConfigVoiceChat()
            self.voice_chat = temp_model.from_map(m.get('VoiceChat'))

        return self

class AIAgentTemplateConfigVoiceChat(DaraModel):
    def __init__(
        self,
        asr_hot_words: List[str] = None,
        asr_language_id: str = None,
        asr_max_silence: int = None,
        avatar_url: str = None,
        avatar_url_type: str = None,
        bailian_app_params: str = None,
        char_break: bool = None,
        enable_intelligent_segment: bool = None,
        enable_push_to_talk: bool = None,
        enable_voice_interrupt: bool = None,
        graceful_shutdown: bool = None,
        greeting: str = None,
        interrupt_words: List[str] = None,
        llm_history: List[main_models.AIAgentTemplateConfigVoiceChatLlmHistory] = None,
        llm_history_limit: int = None,
        llm_system_prompt: str = None,
        max_idle_time: int = None,
        use_voiceprint: bool = None,
        user_offline_timeout: int = None,
        user_online_timeout: int = None,
        vad_level: int = None,
        voice_id: str = None,
        voice_id_list: List[str] = None,
        voiceprint_id: str = None,
        volume: int = None,
        wake_up_query: str = None,
        workflow_override_params: str = None,
    ):
        self.asr_hot_words = asr_hot_words
        self.asr_language_id = asr_language_id
        self.asr_max_silence = asr_max_silence
        self.avatar_url = avatar_url
        self.avatar_url_type = avatar_url_type
        self.bailian_app_params = bailian_app_params
        self.char_break = char_break
        self.enable_intelligent_segment = enable_intelligent_segment
        self.enable_push_to_talk = enable_push_to_talk
        self.enable_voice_interrupt = enable_voice_interrupt
        self.graceful_shutdown = graceful_shutdown
        self.greeting = greeting
        self.interrupt_words = interrupt_words
        self.llm_history = llm_history
        self.llm_history_limit = llm_history_limit
        self.llm_system_prompt = llm_system_prompt
        self.max_idle_time = max_idle_time
        self.use_voiceprint = use_voiceprint
        self.user_offline_timeout = user_offline_timeout
        self.user_online_timeout = user_online_timeout
        self.vad_level = vad_level
        self.voice_id = voice_id
        self.voice_id_list = voice_id_list
        self.voiceprint_id = voiceprint_id
        self.volume = volume
        self.wake_up_query = wake_up_query
        self.workflow_override_params = workflow_override_params

    def validate(self):
        if self.llm_history:
            for v1 in self.llm_history:
                 if v1:
                    v1.validate()

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

        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url

        if self.avatar_url_type is not None:
            result['AvatarUrlType'] = self.avatar_url_type

        if self.bailian_app_params is not None:
            result['BailianAppParams'] = self.bailian_app_params

        if self.char_break is not None:
            result['CharBreak'] = self.char_break

        if self.enable_intelligent_segment is not None:
            result['EnableIntelligentSegment'] = self.enable_intelligent_segment

        if self.enable_push_to_talk is not None:
            result['EnablePushToTalk'] = self.enable_push_to_talk

        if self.enable_voice_interrupt is not None:
            result['EnableVoiceInterrupt'] = self.enable_voice_interrupt

        if self.graceful_shutdown is not None:
            result['GracefulShutdown'] = self.graceful_shutdown

        if self.greeting is not None:
            result['Greeting'] = self.greeting

        if self.interrupt_words is not None:
            result['InterruptWords'] = self.interrupt_words

        result['LlmHistory'] = []
        if self.llm_history is not None:
            for k1 in self.llm_history:
                result['LlmHistory'].append(k1.to_map() if k1 else None)

        if self.llm_history_limit is not None:
            result['LlmHistoryLimit'] = self.llm_history_limit

        if self.llm_system_prompt is not None:
            result['LlmSystemPrompt'] = self.llm_system_prompt

        if self.max_idle_time is not None:
            result['MaxIdleTime'] = self.max_idle_time

        if self.use_voiceprint is not None:
            result['UseVoiceprint'] = self.use_voiceprint

        if self.user_offline_timeout is not None:
            result['UserOfflineTimeout'] = self.user_offline_timeout

        if self.user_online_timeout is not None:
            result['UserOnlineTimeout'] = self.user_online_timeout

        if self.vad_level is not None:
            result['VadLevel'] = self.vad_level

        if self.voice_id is not None:
            result['VoiceId'] = self.voice_id

        if self.voice_id_list is not None:
            result['VoiceIdList'] = self.voice_id_list

        if self.voiceprint_id is not None:
            result['VoiceprintId'] = self.voiceprint_id

        if self.volume is not None:
            result['Volume'] = self.volume

        if self.wake_up_query is not None:
            result['WakeUpQuery'] = self.wake_up_query

        if self.workflow_override_params is not None:
            result['WorkflowOverrideParams'] = self.workflow_override_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrHotWords') is not None:
            self.asr_hot_words = m.get('AsrHotWords')

        if m.get('AsrLanguageId') is not None:
            self.asr_language_id = m.get('AsrLanguageId')

        if m.get('AsrMaxSilence') is not None:
            self.asr_max_silence = m.get('AsrMaxSilence')

        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')

        if m.get('AvatarUrlType') is not None:
            self.avatar_url_type = m.get('AvatarUrlType')

        if m.get('BailianAppParams') is not None:
            self.bailian_app_params = m.get('BailianAppParams')

        if m.get('CharBreak') is not None:
            self.char_break = m.get('CharBreak')

        if m.get('EnableIntelligentSegment') is not None:
            self.enable_intelligent_segment = m.get('EnableIntelligentSegment')

        if m.get('EnablePushToTalk') is not None:
            self.enable_push_to_talk = m.get('EnablePushToTalk')

        if m.get('EnableVoiceInterrupt') is not None:
            self.enable_voice_interrupt = m.get('EnableVoiceInterrupt')

        if m.get('GracefulShutdown') is not None:
            self.graceful_shutdown = m.get('GracefulShutdown')

        if m.get('Greeting') is not None:
            self.greeting = m.get('Greeting')

        if m.get('InterruptWords') is not None:
            self.interrupt_words = m.get('InterruptWords')

        self.llm_history = []
        if m.get('LlmHistory') is not None:
            for k1 in m.get('LlmHistory'):
                temp_model = main_models.AIAgentTemplateConfigVoiceChatLlmHistory()
                self.llm_history.append(temp_model.from_map(k1))

        if m.get('LlmHistoryLimit') is not None:
            self.llm_history_limit = m.get('LlmHistoryLimit')

        if m.get('LlmSystemPrompt') is not None:
            self.llm_system_prompt = m.get('LlmSystemPrompt')

        if m.get('MaxIdleTime') is not None:
            self.max_idle_time = m.get('MaxIdleTime')

        if m.get('UseVoiceprint') is not None:
            self.use_voiceprint = m.get('UseVoiceprint')

        if m.get('UserOfflineTimeout') is not None:
            self.user_offline_timeout = m.get('UserOfflineTimeout')

        if m.get('UserOnlineTimeout') is not None:
            self.user_online_timeout = m.get('UserOnlineTimeout')

        if m.get('VadLevel') is not None:
            self.vad_level = m.get('VadLevel')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        if m.get('VoiceIdList') is not None:
            self.voice_id_list = m.get('VoiceIdList')

        if m.get('VoiceprintId') is not None:
            self.voiceprint_id = m.get('VoiceprintId')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        if m.get('WakeUpQuery') is not None:
            self.wake_up_query = m.get('WakeUpQuery')

        if m.get('WorkflowOverrideParams') is not None:
            self.workflow_override_params = m.get('WorkflowOverrideParams')

        return self

class AIAgentTemplateConfigVoiceChatLlmHistory(DaraModel):
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

class AIAgentTemplateConfigVisionChat(DaraModel):
    def __init__(
        self,
        asr_hot_words: List[str] = None,
        asr_language_id: str = None,
        asr_max_silence: int = None,
        bailian_app_params: str = None,
        char_break: bool = None,
        enable_intelligent_segment: bool = None,
        enable_push_to_talk: bool = None,
        enable_voice_interrupt: bool = None,
        graceful_shutdown: bool = None,
        greeting: str = None,
        interrupt_words: List[str] = None,
        llm_history: List[main_models.AIAgentTemplateConfigVisionChatLlmHistory] = None,
        llm_history_limit: int = None,
        llm_system_prompt: str = None,
        max_idle_time: int = None,
        use_voiceprint: bool = None,
        user_offline_timeout: int = None,
        user_online_timeout: int = None,
        vad_level: int = None,
        voice_id: str = None,
        voice_id_list: List[str] = None,
        voiceprint_id: str = None,
        volume: int = None,
        wake_up_query: str = None,
        workflow_override_params: str = None,
    ):
        self.asr_hot_words = asr_hot_words
        self.asr_language_id = asr_language_id
        self.asr_max_silence = asr_max_silence
        self.bailian_app_params = bailian_app_params
        self.char_break = char_break
        self.enable_intelligent_segment = enable_intelligent_segment
        self.enable_push_to_talk = enable_push_to_talk
        self.enable_voice_interrupt = enable_voice_interrupt
        self.graceful_shutdown = graceful_shutdown
        self.greeting = greeting
        self.interrupt_words = interrupt_words
        self.llm_history = llm_history
        self.llm_history_limit = llm_history_limit
        self.llm_system_prompt = llm_system_prompt
        self.max_idle_time = max_idle_time
        self.use_voiceprint = use_voiceprint
        self.user_offline_timeout = user_offline_timeout
        self.user_online_timeout = user_online_timeout
        self.vad_level = vad_level
        self.voice_id = voice_id
        self.voice_id_list = voice_id_list
        self.voiceprint_id = voiceprint_id
        self.volume = volume
        self.wake_up_query = wake_up_query
        self.workflow_override_params = workflow_override_params

    def validate(self):
        if self.llm_history:
            for v1 in self.llm_history:
                 if v1:
                    v1.validate()

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

        if self.bailian_app_params is not None:
            result['BailianAppParams'] = self.bailian_app_params

        if self.char_break is not None:
            result['CharBreak'] = self.char_break

        if self.enable_intelligent_segment is not None:
            result['EnableIntelligentSegment'] = self.enable_intelligent_segment

        if self.enable_push_to_talk is not None:
            result['EnablePushToTalk'] = self.enable_push_to_talk

        if self.enable_voice_interrupt is not None:
            result['EnableVoiceInterrupt'] = self.enable_voice_interrupt

        if self.graceful_shutdown is not None:
            result['GracefulShutdown'] = self.graceful_shutdown

        if self.greeting is not None:
            result['Greeting'] = self.greeting

        if self.interrupt_words is not None:
            result['InterruptWords'] = self.interrupt_words

        result['LlmHistory'] = []
        if self.llm_history is not None:
            for k1 in self.llm_history:
                result['LlmHistory'].append(k1.to_map() if k1 else None)

        if self.llm_history_limit is not None:
            result['LlmHistoryLimit'] = self.llm_history_limit

        if self.llm_system_prompt is not None:
            result['LlmSystemPrompt'] = self.llm_system_prompt

        if self.max_idle_time is not None:
            result['MaxIdleTime'] = self.max_idle_time

        if self.use_voiceprint is not None:
            result['UseVoiceprint'] = self.use_voiceprint

        if self.user_offline_timeout is not None:
            result['UserOfflineTimeout'] = self.user_offline_timeout

        if self.user_online_timeout is not None:
            result['UserOnlineTimeout'] = self.user_online_timeout

        if self.vad_level is not None:
            result['VadLevel'] = self.vad_level

        if self.voice_id is not None:
            result['VoiceId'] = self.voice_id

        if self.voice_id_list is not None:
            result['VoiceIdList'] = self.voice_id_list

        if self.voiceprint_id is not None:
            result['VoiceprintId'] = self.voiceprint_id

        if self.volume is not None:
            result['Volume'] = self.volume

        if self.wake_up_query is not None:
            result['WakeUpQuery'] = self.wake_up_query

        if self.workflow_override_params is not None:
            result['WorkflowOverrideParams'] = self.workflow_override_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrHotWords') is not None:
            self.asr_hot_words = m.get('AsrHotWords')

        if m.get('AsrLanguageId') is not None:
            self.asr_language_id = m.get('AsrLanguageId')

        if m.get('AsrMaxSilence') is not None:
            self.asr_max_silence = m.get('AsrMaxSilence')

        if m.get('BailianAppParams') is not None:
            self.bailian_app_params = m.get('BailianAppParams')

        if m.get('CharBreak') is not None:
            self.char_break = m.get('CharBreak')

        if m.get('EnableIntelligentSegment') is not None:
            self.enable_intelligent_segment = m.get('EnableIntelligentSegment')

        if m.get('EnablePushToTalk') is not None:
            self.enable_push_to_talk = m.get('EnablePushToTalk')

        if m.get('EnableVoiceInterrupt') is not None:
            self.enable_voice_interrupt = m.get('EnableVoiceInterrupt')

        if m.get('GracefulShutdown') is not None:
            self.graceful_shutdown = m.get('GracefulShutdown')

        if m.get('Greeting') is not None:
            self.greeting = m.get('Greeting')

        if m.get('InterruptWords') is not None:
            self.interrupt_words = m.get('InterruptWords')

        self.llm_history = []
        if m.get('LlmHistory') is not None:
            for k1 in m.get('LlmHistory'):
                temp_model = main_models.AIAgentTemplateConfigVisionChatLlmHistory()
                self.llm_history.append(temp_model.from_map(k1))

        if m.get('LlmHistoryLimit') is not None:
            self.llm_history_limit = m.get('LlmHistoryLimit')

        if m.get('LlmSystemPrompt') is not None:
            self.llm_system_prompt = m.get('LlmSystemPrompt')

        if m.get('MaxIdleTime') is not None:
            self.max_idle_time = m.get('MaxIdleTime')

        if m.get('UseVoiceprint') is not None:
            self.use_voiceprint = m.get('UseVoiceprint')

        if m.get('UserOfflineTimeout') is not None:
            self.user_offline_timeout = m.get('UserOfflineTimeout')

        if m.get('UserOnlineTimeout') is not None:
            self.user_online_timeout = m.get('UserOnlineTimeout')

        if m.get('VadLevel') is not None:
            self.vad_level = m.get('VadLevel')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        if m.get('VoiceIdList') is not None:
            self.voice_id_list = m.get('VoiceIdList')

        if m.get('VoiceprintId') is not None:
            self.voiceprint_id = m.get('VoiceprintId')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        if m.get('WakeUpQuery') is not None:
            self.wake_up_query = m.get('WakeUpQuery')

        if m.get('WorkflowOverrideParams') is not None:
            self.workflow_override_params = m.get('WorkflowOverrideParams')

        return self

class AIAgentTemplateConfigVisionChatLlmHistory(DaraModel):
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

class AIAgentTemplateConfigAvatarChat3D(DaraModel):
    def __init__(
        self,
        asr_hot_words: List[str] = None,
        asr_language_id: str = None,
        asr_max_silence: int = None,
        avatar_id: str = None,
        bailian_app_params: str = None,
        char_break: bool = None,
        enable_intelligent_segment: bool = None,
        enable_push_to_talk: bool = None,
        enable_voice_interrupt: bool = None,
        graceful_shutdown: bool = None,
        greeting: str = None,
        interrupt_words: List[str] = None,
        llm_history: List[main_models.AIAgentTemplateConfigAvatarChat3DLlmHistory] = None,
        llm_history_limit: int = None,
        llm_system_prompt: str = None,
        max_idle_time: int = None,
        use_voiceprint: bool = None,
        user_offline_timeout: int = None,
        user_online_timeout: int = None,
        vad_level: int = None,
        voice_id: str = None,
        voice_id_list: List[str] = None,
        voiceprint_id: str = None,
        volume: int = None,
        wake_up_query: str = None,
        workflow_override_params: str = None,
    ):
        self.asr_hot_words = asr_hot_words
        self.asr_language_id = asr_language_id
        self.asr_max_silence = asr_max_silence
        self.avatar_id = avatar_id
        self.bailian_app_params = bailian_app_params
        self.char_break = char_break
        self.enable_intelligent_segment = enable_intelligent_segment
        self.enable_push_to_talk = enable_push_to_talk
        self.enable_voice_interrupt = enable_voice_interrupt
        self.graceful_shutdown = graceful_shutdown
        self.greeting = greeting
        self.interrupt_words = interrupt_words
        self.llm_history = llm_history
        self.llm_history_limit = llm_history_limit
        self.llm_system_prompt = llm_system_prompt
        self.max_idle_time = max_idle_time
        self.use_voiceprint = use_voiceprint
        self.user_offline_timeout = user_offline_timeout
        self.user_online_timeout = user_online_timeout
        self.vad_level = vad_level
        self.voice_id = voice_id
        self.voice_id_list = voice_id_list
        self.voiceprint_id = voiceprint_id
        self.volume = volume
        self.wake_up_query = wake_up_query
        self.workflow_override_params = workflow_override_params

    def validate(self):
        if self.llm_history:
            for v1 in self.llm_history:
                 if v1:
                    v1.validate()

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

        if self.avatar_id is not None:
            result['AvatarId'] = self.avatar_id

        if self.bailian_app_params is not None:
            result['BailianAppParams'] = self.bailian_app_params

        if self.char_break is not None:
            result['CharBreak'] = self.char_break

        if self.enable_intelligent_segment is not None:
            result['EnableIntelligentSegment'] = self.enable_intelligent_segment

        if self.enable_push_to_talk is not None:
            result['EnablePushToTalk'] = self.enable_push_to_talk

        if self.enable_voice_interrupt is not None:
            result['EnableVoiceInterrupt'] = self.enable_voice_interrupt

        if self.graceful_shutdown is not None:
            result['GracefulShutdown'] = self.graceful_shutdown

        if self.greeting is not None:
            result['Greeting'] = self.greeting

        if self.interrupt_words is not None:
            result['InterruptWords'] = self.interrupt_words

        result['LlmHistory'] = []
        if self.llm_history is not None:
            for k1 in self.llm_history:
                result['LlmHistory'].append(k1.to_map() if k1 else None)

        if self.llm_history_limit is not None:
            result['LlmHistoryLimit'] = self.llm_history_limit

        if self.llm_system_prompt is not None:
            result['LlmSystemPrompt'] = self.llm_system_prompt

        if self.max_idle_time is not None:
            result['MaxIdleTime'] = self.max_idle_time

        if self.use_voiceprint is not None:
            result['UseVoiceprint'] = self.use_voiceprint

        if self.user_offline_timeout is not None:
            result['UserOfflineTimeout'] = self.user_offline_timeout

        if self.user_online_timeout is not None:
            result['UserOnlineTimeout'] = self.user_online_timeout

        if self.vad_level is not None:
            result['VadLevel'] = self.vad_level

        if self.voice_id is not None:
            result['VoiceId'] = self.voice_id

        if self.voice_id_list is not None:
            result['VoiceIdList'] = self.voice_id_list

        if self.voiceprint_id is not None:
            result['VoiceprintId'] = self.voiceprint_id

        if self.volume is not None:
            result['Volume'] = self.volume

        if self.wake_up_query is not None:
            result['WakeUpQuery'] = self.wake_up_query

        if self.workflow_override_params is not None:
            result['WorkflowOverrideParams'] = self.workflow_override_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrHotWords') is not None:
            self.asr_hot_words = m.get('AsrHotWords')

        if m.get('AsrLanguageId') is not None:
            self.asr_language_id = m.get('AsrLanguageId')

        if m.get('AsrMaxSilence') is not None:
            self.asr_max_silence = m.get('AsrMaxSilence')

        if m.get('AvatarId') is not None:
            self.avatar_id = m.get('AvatarId')

        if m.get('BailianAppParams') is not None:
            self.bailian_app_params = m.get('BailianAppParams')

        if m.get('CharBreak') is not None:
            self.char_break = m.get('CharBreak')

        if m.get('EnableIntelligentSegment') is not None:
            self.enable_intelligent_segment = m.get('EnableIntelligentSegment')

        if m.get('EnablePushToTalk') is not None:
            self.enable_push_to_talk = m.get('EnablePushToTalk')

        if m.get('EnableVoiceInterrupt') is not None:
            self.enable_voice_interrupt = m.get('EnableVoiceInterrupt')

        if m.get('GracefulShutdown') is not None:
            self.graceful_shutdown = m.get('GracefulShutdown')

        if m.get('Greeting') is not None:
            self.greeting = m.get('Greeting')

        if m.get('InterruptWords') is not None:
            self.interrupt_words = m.get('InterruptWords')

        self.llm_history = []
        if m.get('LlmHistory') is not None:
            for k1 in m.get('LlmHistory'):
                temp_model = main_models.AIAgentTemplateConfigAvatarChat3DLlmHistory()
                self.llm_history.append(temp_model.from_map(k1))

        if m.get('LlmHistoryLimit') is not None:
            self.llm_history_limit = m.get('LlmHistoryLimit')

        if m.get('LlmSystemPrompt') is not None:
            self.llm_system_prompt = m.get('LlmSystemPrompt')

        if m.get('MaxIdleTime') is not None:
            self.max_idle_time = m.get('MaxIdleTime')

        if m.get('UseVoiceprint') is not None:
            self.use_voiceprint = m.get('UseVoiceprint')

        if m.get('UserOfflineTimeout') is not None:
            self.user_offline_timeout = m.get('UserOfflineTimeout')

        if m.get('UserOnlineTimeout') is not None:
            self.user_online_timeout = m.get('UserOnlineTimeout')

        if m.get('VadLevel') is not None:
            self.vad_level = m.get('VadLevel')

        if m.get('VoiceId') is not None:
            self.voice_id = m.get('VoiceId')

        if m.get('VoiceIdList') is not None:
            self.voice_id_list = m.get('VoiceIdList')

        if m.get('VoiceprintId') is not None:
            self.voiceprint_id = m.get('VoiceprintId')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        if m.get('WakeUpQuery') is not None:
            self.wake_up_query = m.get('WakeUpQuery')

        if m.get('WorkflowOverrideParams') is not None:
            self.workflow_override_params = m.get('WorkflowOverrideParams')

        return self

class AIAgentTemplateConfigAvatarChat3DLlmHistory(DaraModel):
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

