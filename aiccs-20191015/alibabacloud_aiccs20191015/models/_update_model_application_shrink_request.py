# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateModelApplicationShrinkRequest(DaraModel):
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
        dtmf_send_max_count: int = None,
        dtmf_send_wait_timeout: int = None,
        dyvms_scene_name: str = None,
        enable_dtmf_receive: bool = None,
        enable_dtmf_send: bool = None,
        enable_morse: bool = None,
        interrupt_config_shrink: str = None,
        model_code: str = None,
        model_version: str = None,
        mute_active: bool = None,
        mute_duration: int = None,
        mute_hangup_num: int = None,
        mute_push_mode: str = None,
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
        tts_config_shrink: str = None,
        usage_desc: str = None,
    ):
        # The application code.
        # 
        # This parameter is required.
        self.application_code = application_code
        # The number of concurrent requests for the application.
        self.application_cps = application_cps
        # The name of the model application.
        self.application_name = application_name
        # Specifies whether to hang up the call when a call assistant is detected.
        self.call_assistant_hangup = call_assistant_hangup
        # Specifies whether to enable call assistant recognition.
        self.call_assistant_recognize = call_assistant_recognize
        # Specifies whether to trigger the model immediately after the call is connected.
        self.call_connected_trigger_model = call_connected_trigger_model
        # The allowed DTMF digits, specified as a comma-separated string such as `1,2,3`. You can specify a maximum of 20 digits.
        self.dtmf_allowed_digits = dtmf_allowed_digits
        # Specifies whether to automatically validate the DTMF digits.
        self.dtmf_auto_validate_enable = dtmf_auto_validate_enable
        # The number of DTMF digits to collect. The value must be between 1 and 12.
        self.dtmf_digit_count = dtmf_digit_count
        # The timeout for DTMF input, in seconds. The value must be between 1 and 10.
        self.dtmf_input_timeout = dtmf_input_timeout
        # The action to take when the input is outside the allowed range. Valid values: `RETURN_MODEL` and `AUTO_RETRY`.
        self.dtmf_out_of_range_action = dtmf_out_of_range_action
        # The number of retry attempts. The value must be between 1 and 3. This parameter is effective only when `DtmfOutOfRangeAction` is set to `AUTO_RETRY`.
        self.dtmf_retry_play_times = dtmf_retry_play_times
        # The custom text for the retry prompt. The text can contain a maximum of 50 characters. If this parameter is empty, the system uses the default prompt: "Invalid input. Please try again."
        self.dtmf_retry_prompt_text = dtmf_retry_prompt_text
        self.dtmf_send_max_count = dtmf_send_max_count
        self.dtmf_send_wait_timeout = dtmf_send_wait_timeout
        # The scene name.
        self.dyvms_scene_name = dyvms_scene_name
        # Specifies whether to enable the collection of DTMF signals. The default value is `false`.
        self.enable_dtmf_receive = enable_dtmf_receive
        self.enable_dtmf_send = enable_dtmf_send
        # Specifies whether to enable the Morse code configuration. The default value is `false`.
        self.enable_morse = enable_morse
        # The interruption configuration.
        self.interrupt_config_shrink = interrupt_config_shrink
        # The model code.
        self.model_code = model_code
        # The model version.
        self.model_version = model_version
        # Specifies whether the first mute event triggers the model.
        self.mute_active = mute_active
        # The mute duration.
        self.mute_duration = mute_duration
        # The number of consecutive mute events that trigger an automatic hang-up.
        self.mute_hangup_num = mute_hangup_num
        # 静音事件推送模式
        self.mute_push_mode = mute_push_mode
        self.owner_id = owner_id
        # The prompt.
        self.prompt = prompt
        # The qualification ID.
        self.qualification_id = qualification_id
        # The name of the qualification.
        self.qualification_name = qualification_name
        # The URL of the recording file.
        self.recording_file = recording_file
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The session timeout, which is the maximum duration of a call.
        self.session_timeout = session_timeout
        # The value must be `USER`.
        self.source = source
        # The content of the speech.
        self.speech_content = speech_content
        # The speech ID.
        self.speech_id = speech_id
        # The opening statement.
        self.start_word = start_word
        # The type of the opening statement. Valid values:
        self.start_word_type = start_word_type
        # The TTS configuration, such as voice, volume, and speech rate.
        self.tts_config_shrink = tts_config_shrink
        # The purpose of the application.
        self.usage_desc = usage_desc

    def validate(self):
        pass

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

        if self.dtmf_send_max_count is not None:
            result['DtmfSendMaxCount'] = self.dtmf_send_max_count

        if self.dtmf_send_wait_timeout is not None:
            result['DtmfSendWaitTimeout'] = self.dtmf_send_wait_timeout

        if self.dyvms_scene_name is not None:
            result['DyvmsSceneName'] = self.dyvms_scene_name

        if self.enable_dtmf_receive is not None:
            result['EnableDtmfReceive'] = self.enable_dtmf_receive

        if self.enable_dtmf_send is not None:
            result['EnableDtmfSend'] = self.enable_dtmf_send

        if self.enable_morse is not None:
            result['EnableMorse'] = self.enable_morse

        if self.interrupt_config_shrink is not None:
            result['InterruptConfig'] = self.interrupt_config_shrink

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

        if self.mute_push_mode is not None:
            result['MutePushMode'] = self.mute_push_mode

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

        if self.tts_config_shrink is not None:
            result['TtsConfig'] = self.tts_config_shrink

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

        if m.get('DtmfSendMaxCount') is not None:
            self.dtmf_send_max_count = m.get('DtmfSendMaxCount')

        if m.get('DtmfSendWaitTimeout') is not None:
            self.dtmf_send_wait_timeout = m.get('DtmfSendWaitTimeout')

        if m.get('DyvmsSceneName') is not None:
            self.dyvms_scene_name = m.get('DyvmsSceneName')

        if m.get('EnableDtmfReceive') is not None:
            self.enable_dtmf_receive = m.get('EnableDtmfReceive')

        if m.get('EnableDtmfSend') is not None:
            self.enable_dtmf_send = m.get('EnableDtmfSend')

        if m.get('EnableMorse') is not None:
            self.enable_morse = m.get('EnableMorse')

        if m.get('InterruptConfig') is not None:
            self.interrupt_config_shrink = m.get('InterruptConfig')

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

        if m.get('MutePushMode') is not None:
            self.mute_push_mode = m.get('MutePushMode')

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
            self.tts_config_shrink = m.get('TtsConfig')

        if m.get('UsageDesc') is not None:
            self.usage_desc = m.get('UsageDesc')

        return self

