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
        back_channeling_configs: List[main_models.AIAgentConfigBackChannelingConfigs] = None,
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
        # Configuration for ambient sound during the call.
        self.ambient_sound_config = ambient_sound_config
        # Configuration for automatic speech recognition (ASR).
        self.asr_config = asr_config
        # Configuration for the agent\\"s automatic speech, including prompts for LLM latency and long periods of user silence.
        self.auto_speech_config = auto_speech_config
        # Configuration for the avatar. This takes effect only if the workflow includes an avatar node.
        self.avatar_config = avatar_config
        # The URL of the avatar to display during voice calls. If omitted, no avatar is displayed.
        self.avatar_url = avatar_url
        # The type of the avatar URL. By default, this parameter is not set.
        self.avatar_url_type = avatar_url_type
        # >Notice: 
        # 
        # 已废弃，请使用 BackChannelingConfigs
        self.back_channeling_config = back_channeling_config
        # Configuration for back-channeling. When enabled, the system plays short, responsive phrases at specific trigger points.
        self.back_channeling_configs = back_channeling_configs
        # Specifies whether to enable intelligent segmentation. When enabled, short user utterances are merged into a single sentence. Default: `true`.
        self.enable_intelligent_segment = enable_intelligent_segment
        # Specifies whether to enable push-to-talk mode. Default: `false`.
        self.enable_push_to_talk = enable_push_to_talk
        # Parameters for experimental features. Contact support for assistance.
        self.experimental_config = experimental_config
        # Specifies whether to enable graceful shutdown. Default: `false`.
        # 
        # If enabled, the AI agent completes its current utterance before disconnecting when the task is stopped. The agent will not speak for more than 10 seconds.
        self.graceful_shutdown = graceful_shutdown
        # The welcome message the AI agent plays when joining the session. Changes apply to subsequent sessions. If omitted, no welcome message is played.
        self.greeting = greeting
        # Configuration for the speech interruption policy.
        self.interrupt_config = interrupt_config
        # Configuration for the large language model (LLM).
        self.llm_config = llm_config
        # The maximum idle duration in seconds before the AI agent disconnects. If the agent receives no user interaction within this period, it ends the task. Default: 600.
        self.max_idle_time = max_idle_time
        # Configuration for text-to-speech (TTS).
        self.tts_config = tts_config
        # Configuration for conversational turn detection.
        self.turn_detection_config = turn_detection_config
        # The duration in seconds the AI agent waits before terminating the task after a user leaves the session. Default: 5.
        self.user_offline_timeout = user_offline_timeout
        # The duration in seconds the AI agent waits for a user to join. If the user does not join within this time, the agent terminates the task. Default: 60.
        self.user_online_timeout = user_online_timeout
        # Configuration for video content recognition. This enables the system to send callbacks to the client about events detected in the video stream.
        self.vcr_config = vcr_config
        # Configuration for voiceprint recognition.
        self.voiceprint_config = voiceprint_config
        # The speaking volume of the AI agent.
        # 
        # - If not set, the adaptive volume mode recommended by Alibaba Cloud is used by default.
        # 
        # - If set, the value must be in the range of 0 to 400. The final output volume is calculated as: `(Workflow volume) * (volume / 100)`. For example:
        # 
        # 1. If `volume` is 0, the output volume is 0.
        # 
        # 2. If `volume` is 100, the output volume is the same as the original volume.
        # 
        # 3. If `volume` is 200, the output volume is twice the original volume.
        self.volume = volume
        # A user-provided command that the AI agent responds to immediately after the call starts.
        self.wake_up_query = wake_up_query
        # A JSON string containing parameters to override the default workflow configuration.
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

        result['BackChannelingConfigs'] = []
        if self.back_channeling_configs is not None:
            for k1 in self.back_channeling_configs:
                result['BackChannelingConfigs'].append(k1.to_map() if k1 else None)

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

        self.back_channeling_configs = []
        if m.get('BackChannelingConfigs') is not None:
            for k1 in m.get('BackChannelingConfigs'):
                temp_model = main_models.AIAgentConfigBackChannelingConfigs()
                self.back_channeling_configs.append(temp_model.from_map(k1))

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
        registration_mode: str = None,
        use_voiceprint: bool = None,
        voiceprint_id: str = None,
    ):
        # The voiceprint registration mode. Default: `Explicit`.
        # 
        # | Value      | Description                                                                                                         |
        # | ---------- | ------------------------------------------------------------------------------------------------------------------- |
        # | `Explicit` | In `Explicit` mode, the user must register their voiceprint in advance by using the voiceprint registration API.    |
        # | `Implicit` | In `Implicit` mode, the system automatically collects user speech during the conversation to register a voiceprint. |
        self.registration_mode = registration_mode
        # Specifies whether to enable voiceprint recognition. Default: `false`. If set to `true`, you must also provide a valid `VoiceprintId`.
        self.use_voiceprint = use_voiceprint
        # The unique identifier for the voiceprint. This is not set by default. The ID must correspond to a voiceprint registered using the voiceprint registration API. For more information, see [Register a voiceprint](https://help.aliyun.com/document_detail/2964738.html).
        self.voiceprint_id = voiceprint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.registration_mode is not None:
            result['RegistrationMode'] = self.registration_mode

        if self.use_voiceprint is not None:
            result['UseVoiceprint'] = self.use_voiceprint

        if self.voiceprint_id is not None:
            result['VoiceprintId'] = self.voiceprint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegistrationMode') is not None:
            self.registration_mode = m.get('RegistrationMode')

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
        # Configuration for device identification.
        self.equipment = equipment
        # Configuration for head motion detection.
        self.head_motion = head_motion
        # Configuration for invalid frame detection.
        self.invalid_frame_motion = invalid_frame_motion
        # Configuration for look-away detection.
        self.look_away = look_away
        # Configuration for the people counting feature.
        self.people_count = people_count
        # Configuration for still frame detection.
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
        # The duration in milliseconds that a frame must remain still before a notification is sent. If not specified, the setting from the console is used. Range: 200–5000.
        self.callback_delay = callback_delay
        # Specifies whether to enable still frame detection. Default: `false`.
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
        # Specifies whether to enable people counting. Default: `false`.
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
        # Specifies whether to enable look-away detection. Default: `false`.
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
        # The duration in milliseconds that an invalid frame must persist before a notification is sent. If not specified, the setting from the console is used. Range: 200–5000.
        self.callback_delay = callback_delay
        # Specifies whether to enable invalid frame detection.
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
        # Specifies whether to enable head motion detection. Default: `false`.
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
        # Specifies whether to enable device identification. Default: `false`.
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
        # Controls the agent\\"s response speed after detecting a user pause. This parameter applies only in `Semantic` mode. A higher setting results in a faster response but increases the risk of interrupting the user:
        # 
        # - `Low`: Waits patiently with a maximum wait time of 6 seconds, reducing the risk of interruption.
        # 
        # - `Medium`: A balanced wait time (up to 4 seconds), suitable for most scenarios.
        # 
        # - `High`: Responds quickly (up to 2 seconds), which improves speed but may increase the risk of incorrect turn-taking.
        # 
        # This field is empty by default.
        self.eagerness = eagerness
        # The conversational turn detection mode.
        # 
        # - `Normal` (Default): The agent relies on pauses to detect the end of a user\\"s turn.
        # 
        # - `Semantic`: The agent uses AI to analyze conversational context to determine if the user has finished speaking.
        self.mode = mode
        # The pause detection time in AI mode, in milliseconds. Default: -1.
        # 
        # - -1: The AI automatically determines a suitable wait time.
        # 
        # - 0–10000: A custom wait time. A range of 0–1500 ms is recommended.
        # 
        # > This parameter has no effect in `Normal` mode.
        self.semantic_wait_duration = semantic_wait_duration
        # A list of keywords used to determine the end of a user\\"s conversational turn.
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
        # This parameter applies only to the Minimax provider. Supported emotions include:
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
        # This parameter is for the minimax provider only. It enhances recognition for specific low-resource languages and dialects. If the language is unknown, set this to `auto` for automatic detection. By default, this parameter is not set. Supported values include:
        # 
        # <details>
        # 
        # <summary>
        # 
        # Supported languages
        # 
        # </summary>
        # 
        # - Chinese
        # 
        # - Chinese,Yue: Cantonese
        # 
        # - English
        # 
        # - Arabic
        # 
        # - Russian
        # 
        # - Spanish
        # 
        # - French
        # 
        # - Portuguese
        # 
        # - German
        # 
        # - Turkish
        # 
        # - Dutch
        # 
        # - Ukrainian
        # 
        # - Vietnamese
        # 
        # - Indonesian
        # 
        # - Japanese
        # 
        # - Italian
        # 
        # - Korean
        # 
        # - Thai
        # 
        # - Polish
        # 
        # - Romanian
        # 
        # - Greek
        # 
        # - Czech
        # 
        # - Finnish
        # 
        # - Hindi
        # 
        # - auto
        # 
        # </details>
        self.language_id = language_id
        # This parameter applies only to the Minimax provider. Valid values:
        # `speech-01-turbo`, `speech-02-turbo`
        self.model_id = model_id
        # A list of TTS pronunciation rules, executed in order. You can specify a maximum of 20 rules.
        self.pronunciation_rules = pronunciation_rules
        # The speech rate, where a value of 1.0 is normal speed. The supported range can vary by provider. For CosyVoice, the range is 0.5 to 2.0 (default: 1.0). For Minimax, the range is 0.5 to 2.0 (default: 1.0).
        self.speech_rate = speech_rate
        # The ID of the preset TTS voice. Changes apply to the next utterance. If omitted, the voice from the AI agent template is used. The ID can be a maximum of 64 characters. For available voices, see [Intelligent Voice Samples](https://help.aliyun.com/document_detail/449563.html).
        self.voice_id = voice_id
        # A list of available voices.
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
        # The replacement pronunciation. It must be 1 to 9 Chinese characters long and cannot contain spaces.
        self.pronunciation = pronunciation
        # The type of pronunciation rule.
        # Valid value:
        # 
        # - `replacement`: Replaces the specified `Word` with the `Pronunciation`.
        self.type = type
        # The word to be replaced. It must be 1 to 9 Chinese characters long and cannot contain spaces.
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
        # Parameters for Alibaba Cloud Model Studio, provided as a JSON string. For the parameter format, see
        # [Alibaba Cloud Model Studio Parameters](https://help.aliyun.com/document_detail/2858132.html)
        self.bailian_app_params = bailian_app_params
        # Maps built-in agent functions to custom LLM functions. Currently, this only supports function calling for custom, OpenAI-compatible LLMs.
        self.function_map = function_map
        # Specifies whether the LLM message history is synchronized with the content played by the TTS. Default: `false`. When enabled, the saved LLM messages match the content actually played by the TTS.
        # 
        # > When a user interrupts the agent, the `<ims_agent_interrupted>` tag is inserted into the message history at the point of interruption. This affects the next message sent to the LLM. For example:
        # 
        # ```
        # [
        #   {"role": "user", "content": "Tell me a story."},
        #   {"role": "assistant", "content": "Okay, I can tell you a story about the Three Kingdoms. Would you<ims_agent_interrupted> like that?"},
        #   {"role": "user", "content": "Tell me a different one."}
        # ]
        # ```
        self.history_sync_with_tts = history_sync_with_tts
        # When set to `true`, the agent sends the entire LLM response in a single message after it is fully generated, rather than streaming it. This setting does not affect the streaming of subtitles.
        self.llm_complete_reply = llm_complete_reply
        # The conversation history context for the LLM/MLLM.
        self.llm_history = llm_history
        # The maximum number of recent conversational turns to include in the LLM/MLLM context. Default: 10.
        self.llm_history_limit = llm_history_limit
        # The system prompt for the LLM after the call starts.
        self.llm_system_prompt = llm_system_prompt
        # Additional query parameters for an OpenAI-compatible LLM. Parameters must be provided as a URL query string (e.g., `key1=value1&key2=value2`). All values must be strings.
        self.open_aiextra_query = open_aiextra_query
        # The maximum delay in milliseconds before buffered text is sent to the TTS engine, even if `OutputMinLength` is not met. Range: 1000–10000. A value of `0` or omitting this parameter disables the delay limit. Default: Not set.
        self.output_max_delay = output_max_delay
        # The minimum number of characters in a text chunk before it is sent to the TTS engine. Shorter chunks are buffered. Range: 0–100. A value of `0` or omitting this parameter disables buffering. Default: Not set.
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
        # The text content of the message from this role.
        self.content = content
        # The role of the participant in the conversation. Valid values:
        # 
        # - `user`
        # 
        # - `assistant`
        # 
        # - `system`
        # 
        # - `function`
        # 
        # - `plugin`
        # 
        # - `tool`
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
        # The name of a built-in function provided by the AI agent system. Currently, only `hangup` is supported.
        self.function = function
        # The name of the custom LLM function that maps to the agent\\"s built-in function. For details on the custom LLM protocol, see [LLM Standard Interface](https://help.aliyun.com/document_detail/2839094.html).
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
        keep_interrupt_words_for_llm: bool = None,
        no_interrupt_mode: str = None,
    ):
        # Specifies whether to enable speech interruption. Default: `true`.
        self.enable_voice_interrupt = enable_voice_interrupt
        # A list of specific words or phrases that trigger an interruption.
        self.interrupt_words = interrupt_words
        # Specifies whether to include the interrupt words in the text sent to the LLM. Default: `false` (words are discarded).
        # 
        # > For example, if "hold on" is an interrupt word and the user says "hold on, what is the weather like today?", setting this to `false` results in only "what is the weather like today?" being sent to the LLM.
        self.keep_interrupt_words_for_llm = keep_interrupt_words_for_llm
        # Specifies how to handle user speech that occurs during a non-interruptible section of the agent\\"s utterance.
        # 
        # - `cache`: Caches the user\\"s speech and processes it in the next conversational turn.
        # 
        # - `discard`: Discards the user\\"s speech.
        # 
        # Default: `cache`.
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

        if self.keep_interrupt_words_for_llm is not None:
            result['KeepInterruptWordsForLLM'] = self.keep_interrupt_words_for_llm

        if self.no_interrupt_mode is not None:
            result['NoInterruptMode'] = self.no_interrupt_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableVoiceInterrupt') is not None:
            self.enable_voice_interrupt = m.get('EnableVoiceInterrupt')

        if m.get('InterruptWords') is not None:
            self.interrupt_words = m.get('InterruptWords')

        if m.get('KeepInterruptWordsForLLM') is not None:
            self.keep_interrupt_words_for_llm = m.get('KeepInterruptWordsForLLM')

        if m.get('NoInterruptMode') is not None:
            self.no_interrupt_mode = m.get('NoInterruptMode')

        return self

class AIAgentConfigBackChannelingConfigs(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        probability: float = None,
        trigger_stage: str = None,
        words: List[main_models.AIAgentConfigBackChannelingConfigsWords] = None,
    ):
        # Specifies whether to enable this back-channeling rule. This is a required field.
        self.enabled = enabled
        # The trigger probability. Range: 0.0–1.0. This is a required field.
        self.probability = probability
        # The trigger for the back-channeling. Valid value:
        # 
        # - `pause_detected`: Triggered when a short pause in speech is detected.
        self.trigger_stage = trigger_stage
        # A collection of acknowledgment phrases. You can specify a maximum of 10 phrases. Each phrase must be 20 characters or less, and the sum of their probabilities must be 1.0.
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
                temp_model = main_models.AIAgentConfigBackChannelingConfigsWords()
                self.words.append(temp_model.from_map(k1))

        return self

class AIAgentConfigBackChannelingConfigsWords(DaraModel):
    def __init__(
        self,
        probability: float = None,
        text: str = None,
    ):
        # 本短语的触发概率，范围 0.0–1.0，必填。
        self.probability = probability
        # 短语文本，长度 ≤ 20 字符，支持多语言。必填。
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

class AIAgentConfigBackChannelingConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        probability: float = None,
        trigger_stage: str = None,
        words: List[main_models.AIAgentConfigBackChannelingConfigWords] = None,
    ):
        # 是否启用附和功能。必填，取值 true/false。
        self.enabled = enabled
        # 功能触发概率。范围 0.0–1.0。必填。
        self.probability = probability
        # 附和触发的时机。可选值：
        # 
        # - pause_detected（检测到说话短暂停顿）
        self.trigger_stage = trigger_stage
        # 附和短语集合。最大 10 条，每条短语长度 ≤ 20 字符，概率总和为 1.0。
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
        # 本短语的触发概率，范围 0.0–1.0，必填。
        self.probability = probability
        # 短语文本，长度 ≤ 20 字符，支持多语言。必填。
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
        # The model ID of the avatar.
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
        # Configuration for prompts to play during LLM response latency.
        self.llm_pending = llm_pending
        # Configuration for prompts to play when the user is silent for an extended period.
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
        hangup_end_word: str = None,
        max_repeats: int = None,
        messages: List[main_models.AIAgentConfigAutoSpeechConfigUserIdleMessages] = None,
        wait_time: int = None,
    ):
        # A farewell message played before hanging up due to user inactivity.
        self.hangup_end_word = hangup_end_word
        # The maximum number of times the prompt can be repeated. Range: 0–10. This is a required field. If the limit is exceeded, the call is terminated.
        self.max_repeats = max_repeats
        # A collection of prompt messages. A maximum of 10 messages are supported, each up to 100 characters. The sum of all probabilities must be 100%.
        self.messages = messages
        # The silence duration threshold in milliseconds. If the user is silent for longer than this period, a prompt is triggered. Range: 5000–600000. This is a required field.
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
        # The probability of this message being selected. Range: 0–1, corresponding to 0%–100%.
        self.probability = probability
        # The text of the prompt message, up to 100 characters.
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
        mode: str = None,
        wait_time: int = None,
    ):
        # A collection of prompt messages. A maximum of 10 messages are supported, each up to 100 characters. The sum of all probabilities must be 100%.
        self.messages = messages
        # The mode for handling LLM latency prompts. `random`: Plays a random message from the list. `sequence`: Plays messages in order. This is a required field.
        self.mode = mode
        # The wait time threshold for LLM responses. If the threshold is exceeded, a prompt is played. This is a required field. Unit: ms. Range: 500–10000. Set this value based on the actual performance of your LLM.
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
                temp_model = main_models.AIAgentConfigAutoSpeechConfigLlmPendingMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('WaitTime') is not None:
            self.wait_time = m.get('WaitTime')

        return self

class AIAgentConfigAutoSpeechConfigLlmPendingMessages(DaraModel):
    def __init__(
        self,
        probability: float = None,
        text: str = None,
    ):
        # The probability of this message being selected. Range: 0–1, corresponding to 0%–100%.
        self.probability = probability
        # The text of the prompt message, up to 100 characters.
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
        # A list of hotwords to improve ASR accuracy. You can specify a maximum of 128 hotwords.
        self.asr_hot_words = asr_hot_words
        # The language for ASR. Valid values:
        # 
        # - `zh_mandarin`: Chinese (Mandarin)
        # 
        # - `en`: English
        # 
        # - `zh_en`: Chinese-English mixed
        # 
        # - `es`: Spanish
        # 
        # - `jp`: Japanese
        self.asr_language_id = asr_language_id
        # The maximum duration of silence in milliseconds before the ASR engine finalizes an utterance. A pause longer than this value signals a sentence break. Range: 200–1200. Default: 400.
        self.asr_max_silence = asr_max_silence
        # Passthrough parameters for proprietary ASR integrations.
        self.custom_params = custom_params
        # The minimum duration in milliseconds of continuous user speech required to trigger an interruption. This controls interruption sensitivity. A value of 0 disables this feature. Range: 200–2000. A common range is 200–500 ms, which typically corresponds to 1 to 4 Chinese characters. If omitted, this feature is disabled.
        self.vad_duration = vad_duration
        # The Voice Activity Detection (VAD) threshold for interruptions. Range: 0–11. Default: 11.
        # 
        # - `0`: Disables VAD.
        # 
        # - `1`–`10`: Sets the interruption sensitivity. A higher value makes the agent harder to interrupt.
        # 
        # - `11`: An enhanced mode with lower audio distortion and stronger noise resistance.
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
        # The ID of the ambient sound resource. You can obtain this ID from the advanced settings of the agent configuration in the console.
        self.resource_id = resource_id
        # The volume of the ambient sound. Range: 0–100. A value of 0 disables the sound.
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

