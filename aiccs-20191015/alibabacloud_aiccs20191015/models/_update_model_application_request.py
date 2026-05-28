# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class UpdateModelApplicationRequest(DaraModel):
    def __init__(
        self,
        application_code: str = None,
        application_cps: int = None,
        application_name: str = None,
        call_assistant_hangup: bool = None,
        call_assistant_recognize: bool = None,
        call_connected_trigger_model: bool = None,
        dtmf_allowed_digits: str = None,
        dtmf_auto_validate_enable: bool = None,
        dtmf_digit_count: int = None,
        dtmf_input_timeout: int = None,
        dtmf_out_of_range_action: str = None,
        dtmf_retry_play_times: int = None,
        dtmf_retry_prompt_text: str = None,
        dyvms_scene_name: str = None,
        enable_dtmf_receive: bool = None,
        enable_morse: bool = None,
        interrupt_config: main_models.UpdateModelApplicationRequestInterruptConfig = None,
        model_code: str = None,
        model_version: str = None,
        mute_active: bool = None,
        mute_duration: int = None,
        mute_hangup_num: int = None,
        owner_id: int = None,
        prompt: str = None,
        qualification_id: int = None,
        qualification_name: str = None,
        recording_file: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        session_timeout: int = None,
        source: str = None,
        speech_content: str = None,
        speech_id: int = None,
        start_word: str = None,
        start_word_type: int = None,
        tts_config: main_models.UpdateModelApplicationRequestTtsConfig = None,
        usage_desc: str = None,
    ):
        # 应用编码
        # 
        # This parameter is required.
        self.application_code = application_code
        # 应用并发请求数
        self.application_cps = application_cps
        # 模型应用名称
        self.application_name = application_name
        self.call_assistant_hangup = call_assistant_hangup
        # 通话助手识别
        self.call_assistant_recognize = call_assistant_recognize
        self.call_connected_trigger_model = call_connected_trigger_model
        self.dtmf_allowed_digits = dtmf_allowed_digits
        self.dtmf_auto_validate_enable = dtmf_auto_validate_enable
        self.dtmf_digit_count = dtmf_digit_count
        self.dtmf_input_timeout = dtmf_input_timeout
        self.dtmf_out_of_range_action = dtmf_out_of_range_action
        self.dtmf_retry_play_times = dtmf_retry_play_times
        self.dtmf_retry_prompt_text = dtmf_retry_prompt_text
        # 场景名称
        self.dyvms_scene_name = dyvms_scene_name
        self.enable_dtmf_receive = enable_dtmf_receive
        self.enable_morse = enable_morse
        # 打断配置
        self.interrupt_config = interrupt_config
        # 模型编码
        self.model_code = model_code
        # 模型版本
        self.model_version = model_version
        # 第一个静音是否唤起模型
        self.mute_active = mute_active
        # 静音时长
        self.mute_duration = mute_duration
        # 连续多少个静音事件主动挂机
        self.mute_hangup_num = mute_hangup_num
        self.owner_id = owner_id
        # 提示词
        self.prompt = prompt
        # 资质ID
        self.qualification_id = qualification_id
        # 资质名称
        self.qualification_name = qualification_name
        self.recording_file = recording_file
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 最大通话时长
        self.session_timeout = session_timeout
        # 来源
        self.source = source
        # 话术内容
        self.speech_content = speech_content
        # 话束id
        self.speech_id = speech_id
        # 开场白
        self.start_word = start_word
        self.start_word_type = start_word_type
        # tts配置，包括音色、音量、音速等。
        self.tts_config = tts_config
        # 用途
        self.usage_desc = usage_desc

    def validate(self):
        if self.interrupt_config:
            self.interrupt_config.validate()
        if self.tts_config:
            self.tts_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_code is not None:
            result['ApplicationCode'] = self.application_code

        if self.application_cps is not None:
            result['ApplicationCps'] = self.application_cps

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.call_assistant_hangup is not None:
            result['CallAssistantHangup'] = self.call_assistant_hangup

        if self.call_assistant_recognize is not None:
            result['CallAssistantRecognize'] = self.call_assistant_recognize

        if self.call_connected_trigger_model is not None:
            result['CallConnectedTriggerModel'] = self.call_connected_trigger_model

        if self.dtmf_allowed_digits is not None:
            result['DtmfAllowedDigits'] = self.dtmf_allowed_digits

        if self.dtmf_auto_validate_enable is not None:
            result['DtmfAutoValidateEnable'] = self.dtmf_auto_validate_enable

        if self.dtmf_digit_count is not None:
            result['DtmfDigitCount'] = self.dtmf_digit_count

        if self.dtmf_input_timeout is not None:
            result['DtmfInputTimeout'] = self.dtmf_input_timeout

        if self.dtmf_out_of_range_action is not None:
            result['DtmfOutOfRangeAction'] = self.dtmf_out_of_range_action

        if self.dtmf_retry_play_times is not None:
            result['DtmfRetryPlayTimes'] = self.dtmf_retry_play_times

        if self.dtmf_retry_prompt_text is not None:
            result['DtmfRetryPromptText'] = self.dtmf_retry_prompt_text

        if self.dyvms_scene_name is not None:
            result['DyvmsSceneName'] = self.dyvms_scene_name

        if self.enable_dtmf_receive is not None:
            result['EnableDtmfReceive'] = self.enable_dtmf_receive

        if self.enable_morse is not None:
            result['EnableMorse'] = self.enable_morse

        if self.interrupt_config is not None:
            result['InterruptConfig'] = self.interrupt_config.to_map()

        if self.model_code is not None:
            result['ModelCode'] = self.model_code

        if self.model_version is not None:
            result['ModelVersion'] = self.model_version

        if self.mute_active is not None:
            result['MuteActive'] = self.mute_active

        if self.mute_duration is not None:
            result['MuteDuration'] = self.mute_duration

        if self.mute_hangup_num is not None:
            result['MuteHangupNum'] = self.mute_hangup_num

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id

        if self.qualification_name is not None:
            result['QualificationName'] = self.qualification_name

        if self.recording_file is not None:
            result['RecordingFile'] = self.recording_file

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout

        if self.source is not None:
            result['Source'] = self.source

        if self.speech_content is not None:
            result['SpeechContent'] = self.speech_content

        if self.speech_id is not None:
            result['SpeechId'] = self.speech_id

        if self.start_word is not None:
            result['StartWord'] = self.start_word

        if self.start_word_type is not None:
            result['StartWordType'] = self.start_word_type

        if self.tts_config is not None:
            result['TtsConfig'] = self.tts_config.to_map()

        if self.usage_desc is not None:
            result['UsageDesc'] = self.usage_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCode') is not None:
            self.application_code = m.get('ApplicationCode')

        if m.get('ApplicationCps') is not None:
            self.application_cps = m.get('ApplicationCps')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('CallAssistantHangup') is not None:
            self.call_assistant_hangup = m.get('CallAssistantHangup')

        if m.get('CallAssistantRecognize') is not None:
            self.call_assistant_recognize = m.get('CallAssistantRecognize')

        if m.get('CallConnectedTriggerModel') is not None:
            self.call_connected_trigger_model = m.get('CallConnectedTriggerModel')

        if m.get('DtmfAllowedDigits') is not None:
            self.dtmf_allowed_digits = m.get('DtmfAllowedDigits')

        if m.get('DtmfAutoValidateEnable') is not None:
            self.dtmf_auto_validate_enable = m.get('DtmfAutoValidateEnable')

        if m.get('DtmfDigitCount') is not None:
            self.dtmf_digit_count = m.get('DtmfDigitCount')

        if m.get('DtmfInputTimeout') is not None:
            self.dtmf_input_timeout = m.get('DtmfInputTimeout')

        if m.get('DtmfOutOfRangeAction') is not None:
            self.dtmf_out_of_range_action = m.get('DtmfOutOfRangeAction')

        if m.get('DtmfRetryPlayTimes') is not None:
            self.dtmf_retry_play_times = m.get('DtmfRetryPlayTimes')

        if m.get('DtmfRetryPromptText') is not None:
            self.dtmf_retry_prompt_text = m.get('DtmfRetryPromptText')

        if m.get('DyvmsSceneName') is not None:
            self.dyvms_scene_name = m.get('DyvmsSceneName')

        if m.get('EnableDtmfReceive') is not None:
            self.enable_dtmf_receive = m.get('EnableDtmfReceive')

        if m.get('EnableMorse') is not None:
            self.enable_morse = m.get('EnableMorse')

        if m.get('InterruptConfig') is not None:
            temp_model = main_models.UpdateModelApplicationRequestInterruptConfig()
            self.interrupt_config = temp_model.from_map(m.get('InterruptConfig'))

        if m.get('ModelCode') is not None:
            self.model_code = m.get('ModelCode')

        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')

        if m.get('MuteActive') is not None:
            self.mute_active = m.get('MuteActive')

        if m.get('MuteDuration') is not None:
            self.mute_duration = m.get('MuteDuration')

        if m.get('MuteHangupNum') is not None:
            self.mute_hangup_num = m.get('MuteHangupNum')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')

        if m.get('QualificationName') is not None:
            self.qualification_name = m.get('QualificationName')

        if m.get('RecordingFile') is not None:
            self.recording_file = m.get('RecordingFile')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SpeechContent') is not None:
            self.speech_content = m.get('SpeechContent')

        if m.get('SpeechId') is not None:
            self.speech_id = m.get('SpeechId')

        if m.get('StartWord') is not None:
            self.start_word = m.get('StartWord')

        if m.get('StartWordType') is not None:
            self.start_word_type = m.get('StartWordType')

        if m.get('TtsConfig') is not None:
            temp_model = main_models.UpdateModelApplicationRequestTtsConfig()
            self.tts_config = temp_model.from_map(m.get('TtsConfig'))

        if m.get('UsageDesc') is not None:
            self.usage_desc = m.get('UsageDesc')

        return self

class UpdateModelApplicationRequestTtsConfig(DaraModel):
    def __init__(
        self,
        background_enabled: bool = None,
        background_sound: int = None,
        background_volume: int = None,
        customer_account_id: int = None,
        mixing_enabled: bool = None,
        mixing_template: int = None,
        resource_id: str = None,
        tts_speed: int = None,
        tts_style: str = None,
        tts_volume: int = None,
        voice_code: str = None,
        voice_type: str = None,
    ):
        self.background_enabled = background_enabled
        # 背景音id
        self.background_sound = background_sound
        # 背景音音量(id)
        self.background_volume = background_volume
        self.customer_account_id = customer_account_id
        self.mixing_enabled = mixing_enabled
        # 混音模版id
        self.mixing_template = mixing_template
        self.resource_id = resource_id
        # TTS 变量播放时的声音速度。取值范围：-200~200，默认值为 0。
        self.tts_speed = tts_speed
        # 声音风格
        self.tts_style = tts_style
        # TTS 变量播放的音量。取值范围：0~100，默认值为 0。
        self.tts_volume = tts_volume
        # 声音编码
        self.voice_code = voice_code
        # 声音类型
        self.voice_type = voice_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_enabled is not None:
            result['BackgroundEnabled'] = self.background_enabled

        if self.background_sound is not None:
            result['BackgroundSound'] = self.background_sound

        if self.background_volume is not None:
            result['BackgroundVolume'] = self.background_volume

        if self.customer_account_id is not None:
            result['CustomerAccountId'] = self.customer_account_id

        if self.mixing_enabled is not None:
            result['MixingEnabled'] = self.mixing_enabled

        if self.mixing_template is not None:
            result['MixingTemplate'] = self.mixing_template

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.tts_speed is not None:
            result['TtsSpeed'] = self.tts_speed

        if self.tts_style is not None:
            result['TtsStyle'] = self.tts_style

        if self.tts_volume is not None:
            result['TtsVolume'] = self.tts_volume

        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code

        if self.voice_type is not None:
            result['VoiceType'] = self.voice_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundEnabled') is not None:
            self.background_enabled = m.get('BackgroundEnabled')

        if m.get('BackgroundSound') is not None:
            self.background_sound = m.get('BackgroundSound')

        if m.get('BackgroundVolume') is not None:
            self.background_volume = m.get('BackgroundVolume')

        if m.get('CustomerAccountId') is not None:
            self.customer_account_id = m.get('CustomerAccountId')

        if m.get('MixingEnabled') is not None:
            self.mixing_enabled = m.get('MixingEnabled')

        if m.get('MixingTemplate') is not None:
            self.mixing_template = m.get('MixingTemplate')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('TtsSpeed') is not None:
            self.tts_speed = m.get('TtsSpeed')

        if m.get('TtsStyle') is not None:
            self.tts_style = m.get('TtsStyle')

        if m.get('TtsVolume') is not None:
            self.tts_volume = m.get('TtsVolume')

        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')

        if m.get('VoiceType') is not None:
            self.voice_type = m.get('VoiceType')

        return self

class UpdateModelApplicationRequestInterruptConfig(DaraModel):
    def __init__(
        self,
        avoid_interrupt_dto: main_models.UpdateModelApplicationRequestInterruptConfigAvoidInterruptDTO = None,
        enable_avoid_interrupt: bool = None,
        enable_interrupt_backchannel: bool = None,
        enable_startword_entire_not_interrupt: bool = None,
        enable_startword_not_interrupt: bool = None,
        startword_protect_duration: float = None,
    ):
        # 防止连续抢话功能配置
        self.avoid_interrupt_dto = avoid_interrupt_dto
        # 防止连续抢话功能是否开启
        self.enable_avoid_interrupt = enable_avoid_interrupt
        self.enable_interrupt_backchannel = enable_interrupt_backchannel
        # 开场白全程不打断
        self.enable_startword_entire_not_interrupt = enable_startword_entire_not_interrupt
        # 开场白不打断配置是否开启
        self.enable_startword_not_interrupt = enable_startword_not_interrupt
        # 开场白保护时长
        self.startword_protect_duration = startword_protect_duration

    def validate(self):
        if self.avoid_interrupt_dto:
            self.avoid_interrupt_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avoid_interrupt_dto is not None:
            result['AvoidInterruptDTO'] = self.avoid_interrupt_dto.to_map()

        if self.enable_avoid_interrupt is not None:
            result['EnableAvoidInterrupt'] = self.enable_avoid_interrupt

        if self.enable_interrupt_backchannel is not None:
            result['EnableInterruptBackchannel'] = self.enable_interrupt_backchannel

        if self.enable_startword_entire_not_interrupt is not None:
            result['EnableStartwordEntireNotInterrupt'] = self.enable_startword_entire_not_interrupt

        if self.enable_startword_not_interrupt is not None:
            result['EnableStartwordNotInterrupt'] = self.enable_startword_not_interrupt

        if self.startword_protect_duration is not None:
            result['StartwordProtectDuration'] = self.startword_protect_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvoidInterruptDTO') is not None:
            temp_model = main_models.UpdateModelApplicationRequestInterruptConfigAvoidInterruptDTO()
            self.avoid_interrupt_dto = temp_model.from_map(m.get('AvoidInterruptDTO'))

        if m.get('EnableAvoidInterrupt') is not None:
            self.enable_avoid_interrupt = m.get('EnableAvoidInterrupt')

        if m.get('EnableInterruptBackchannel') is not None:
            self.enable_interrupt_backchannel = m.get('EnableInterruptBackchannel')

        if m.get('EnableStartwordEntireNotInterrupt') is not None:
            self.enable_startword_entire_not_interrupt = m.get('EnableStartwordEntireNotInterrupt')

        if m.get('EnableStartwordNotInterrupt') is not None:
            self.enable_startword_not_interrupt = m.get('EnableStartwordNotInterrupt')

        if m.get('StartwordProtectDuration') is not None:
            self.startword_protect_duration = m.get('StartwordProtectDuration')

        return self

class UpdateModelApplicationRequestInterruptConfigAvoidInterruptDTO(DaraModel):
    def __init__(
        self,
        interrupt_num: int = None,
        interrupt_protect_duration: float = None,
    ):
        self.interrupt_num = interrupt_num
        self.interrupt_protect_duration = interrupt_protect_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interrupt_num is not None:
            result['InterruptNum'] = self.interrupt_num

        if self.interrupt_protect_duration is not None:
            result['InterruptProtectDuration'] = self.interrupt_protect_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InterruptNum') is not None:
            self.interrupt_num = m.get('InterruptNum')

        if m.get('InterruptProtectDuration') is not None:
            self.interrupt_protect_duration = m.get('InterruptProtectDuration')

        return self

