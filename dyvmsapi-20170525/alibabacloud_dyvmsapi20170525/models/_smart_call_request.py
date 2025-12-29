# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SmartCallRequest(DaraModel):
    def __init__(
        self,
        action_code_break: bool = None,
        action_code_time_break: int = None,
        asr_base_id: str = None,
        asr_model_id: str = None,
        background_file_code: str = None,
        background_speed: int = None,
        background_volume: int = None,
        called_number: str = None,
        called_show_number: str = None,
        dynamic_id: str = None,
        early_media_asr: bool = None,
        enable_itn: bool = None,
        mute_time: int = None,
        noise_threshold: float = None,
        out_id: str = None,
        owner_id: int = None,
        pause_time: int = None,
        record_flag: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        session_timeout: int = None,
        speed: int = None,
        stream_asr: int = None,
        tts_conf: bool = None,
        tts_speed: int = None,
        tts_style: str = None,
        tts_volume: int = None,
        voice_code: str = None,
        voice_code_param: str = None,
        volume: int = None,
    ):
        # Specifies whether the playback of the recording file can be interrupted. Default value: **true**. The default value indicates that the playback of the recording file can be interrupted.
        # 
        # If you set the value of this parameter to false, the playback of the recording file cannot be interrupted even if the value of action_break is set to true.
        # 
        # > The value of action_code_break takes precedence over the value of action_break.
        self.action_code_break = action_code_break
        # The duration that the user keeps speaking. The playback of the recording file is interrupted when this duration is reached. Unit: milliseconds.
        # 
        # If the value of ActionCodeBreak is set to **true** for the recording file and the duration that the user keeps speaking reaches the specified duration, the playback of the recording file is interrupted. If you do not specify ActionCodeTimeBreak or set the value of ActionCodeTimeBreak to 0, the setting of ActionCodeBreak does not take effect.
        self.action_code_time_break = action_code_time_break
        # The ASR base model. Valid values:
        # 
        # *   **customer_service_8k** (default): Chinese Mandarin.
        # *   **dialect_customer_service_8k**: a heavy accent.
        # 
        # > You must specify the ASR model when you call the SmartCall operation. We recommend that you specify either of the AsrModelId and AsrBaseId parameters.
        # 
        # *   If you specify only the AsrModelId parameter, the specified ASR model is used.
        # 
        # *   If you specify only the AsrBaseId parameter, the ASR base model is used.
        # 
        # *   If you specify neither of the two parameters, the default ASR base model is used, that is, the default value customer_service_8k is used for the AsrBaseId parameter.
        # 
        # *   If you specify both parameters, make sure that their values do not conflict with each other.
        self.asr_base_id = asr_base_id
        # The ID of the Automatic Speech Recognition (ASR) model.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and view the ID of the ASR model on the **ASR Model Management** page.
        # 
        # > You must specify the ASR model when you call the SmartCall operation. We recommend that you specify either of the AsrModelId and AsrBaseId parameters.
        # 
        # *   If you specify only the AsrModelId parameter, the specified ASR model is used.
        # 
        # *   If you specify only the AsrBaseId parameter, the specified ASR base model is used.
        # 
        # *   If you specify neither of the two parameters, the default value customer_service_8k is used for the AsrBaseId parameter. This means that the default Mandarin ASR base model is used.
        # 
        # *   If you specify both parameters, make sure that their values do not conflict with each other.
        self.asr_model_id = asr_model_id
        # The ID of the background voice file that is played back when the user talks with the robot.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice File Management**, click the **Intelligent Speech Interaction Recording File** tab, and then click **Details** in the Actions column to view the voice ID.
        self.background_file_code = background_file_code
        # This parameter is unavailable.
        self.background_speed = background_speed
        # This parameter is unavailable.
        self.background_volume = background_volume
        # The called number. Only phone numbers in the Chinese mainland are supported.
        # 
        # This parameter is required.
        self.called_number = called_number
        # The number displayed to the called party. The value must be the number you purchased.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and choose **Voice Numbers** > **Real Number Management** to view the number you purchased.
        # 
        # This parameter is required.
        self.called_show_number = called_show_number
        # The dynamic extension ID that is reserved for the caller of the operation. This ID is returned in the callback URL and is used as the development identifier of the customer.
        self.dynamic_id = dynamic_id
        # Specifies whether to enable speech recognition of early media. Valid values:
        # 
        # *   **false** (default): Speech recognition of early media is disabled.
        # *   **true**: Speech recognition of early media is enabled.
        # 
        # > If you set the value of this parameter to **true**, the reason why the call is not answered is recorded.
        self.early_media_asr = early_media_asr
        # Specifies whether to enable Inverse Text Normalization (ITN) during post-processing. Default value: **false**. If you set the value to false, ITN is not enabled during post-processing.
        # 
        # If you set the value to **true**, Chinese numerals are converted into Arabic numerals for output.
        self.enable_itn = enable_itn
        # The silence duration. The system determines the end of the conversation based on the silence duration of the user. Unit: milliseconds. Valid values: 1000 to 20000.****
        # 
        # > 
        # 
        # *   If you specify a value out of the valid range, the default value **10000** is used.
        # 
        # *   The parameter value can be adjusted during the conversation. The last setting prevails.
        self.mute_time = mute_time
        self.noise_threshold = noise_threshold
        # The ID that is reserved for the caller of the operation. This ID is returned to the caller in a receipt message.
        # 
        # The value is of the STRING type and must be 1 to 15 bytes in length.
        self.out_id = out_id
        self.owner_id = owner_id
        # The pause duration. The system determines the end of a sentence based on the pause duration of the user in the conversation. Unit: milliseconds. Valid values: 300 to 1200.****
        # 
        # > 
        # 
        # *   If you specify a value out of the valid range, the default value **800** is used.
        # 
        # *   You cannot change the parameter value after specifying it.
        self.pause_time = pause_time
        # Specifies whether to record the conversation. Valid values:
        # 
        # *   **true**: The conversation is recorded.
        # *   **false**: The conversation is not recorded.
        self.record_flag = record_flag
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The maximum call duration. The call is automatically hung up when the maximum call duration is reached. Unit: seconds.
        # 
        # > The maximum call duration is 3,600 seconds.
        self.session_timeout = session_timeout
        # This parameter is unavailable.
        self.speed = speed
        # Specifies whether to enable streaming ASR, which intelligently judges what the user wants to express based on the first few words spoken by the user. Valid values:
        # 
        # *   **0**: Streaming ASR is disabled.
        # *   **1**: Streaming ASR is enabled.
        self.stream_asr = stream_asr
        # Specifies whether to set TTS sound parameters. Valid values:
        # 
        # *   **true**: TTS sound parameters must be set. You must set the **TtsStyle**, **TtsColume**, and **TtsSpeed** parameters to specify a sound style.
        # *   **false**: TTS sound parameters do not need to be set. The values of TTS sound parameters do not take effect even if you set them.
        self.tts_conf = tts_conf
        # The speed of TTS variable playback. Valid values: -200 to 200. Default value: 0.
        self.tts_speed = tts_speed
        # The sound style for TTS variable playback. Default value: **xiaoyun**. For more information about the sound styles, see the **Sound styles** table below.
        self.tts_style = tts_style
        # The volume of TTS variable playback. Valid values: 0 to 100. Default value: 0.
        self.tts_volume = tts_volume
        # The recording file that is played back in the intelligent outbound call.
        # 
        # The file can be an online file, a voice file uploaded from the Voice Messaging Service console, or a text-to-speech (TTS) template that contains variables. You can specify multiple files and a TTS variable together. Separate them with commas (,). The values of the variables in the TTS template are specified by the **VoiceCodeParam** parameter.
        # 
        # *   If you use an online file as the recording file, set the value of **VoiceCode** to the URL of the file that can be accessed over the Internet.
        # *   If you use a voice file uploaded from the Voice Messaging Service console as the recording file, set the value of **VoiceCode** to the voice ID of the file. You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home), choose **Voice File Management**, click the **Intelligent Speech Interaction Recording File** tab, and then click **Details** in the Actions column to view the voice ID.
        # *   If you use a TTS template that contains variables as the recording file, set the value of **VoiceCode** to a variable name such as $name$, and also set a value for the variable in the **VoiceCodeParam** parameter.
        # 
        # This parameter is required.
        self.voice_code = voice_code
        # The value of the TTS variable, in the JSON format. This value must match the TTS variable specified by the **VoiceCode** parameter.
        self.voice_code_param = voice_code_param
        # The volume at which the recording file is played. Valid values: -4 to 4. We recommend that you set the value of this parameter to **1**.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_code_break is not None:
            result['ActionCodeBreak'] = self.action_code_break

        if self.action_code_time_break is not None:
            result['ActionCodeTimeBreak'] = self.action_code_time_break

        if self.asr_base_id is not None:
            result['AsrBaseId'] = self.asr_base_id

        if self.asr_model_id is not None:
            result['AsrModelId'] = self.asr_model_id

        if self.background_file_code is not None:
            result['BackgroundFileCode'] = self.background_file_code

        if self.background_speed is not None:
            result['BackgroundSpeed'] = self.background_speed

        if self.background_volume is not None:
            result['BackgroundVolume'] = self.background_volume

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number

        if self.dynamic_id is not None:
            result['DynamicId'] = self.dynamic_id

        if self.early_media_asr is not None:
            result['EarlyMediaAsr'] = self.early_media_asr

        if self.enable_itn is not None:
            result['EnableITN'] = self.enable_itn

        if self.mute_time is not None:
            result['MuteTime'] = self.mute_time

        if self.noise_threshold is not None:
            result['NoiseThreshold'] = self.noise_threshold

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pause_time is not None:
            result['PauseTime'] = self.pause_time

        if self.record_flag is not None:
            result['RecordFlag'] = self.record_flag

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.stream_asr is not None:
            result['StreamAsr'] = self.stream_asr

        if self.tts_conf is not None:
            result['TtsConf'] = self.tts_conf

        if self.tts_speed is not None:
            result['TtsSpeed'] = self.tts_speed

        if self.tts_style is not None:
            result['TtsStyle'] = self.tts_style

        if self.tts_volume is not None:
            result['TtsVolume'] = self.tts_volume

        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code

        if self.voice_code_param is not None:
            result['VoiceCodeParam'] = self.voice_code_param

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCodeBreak') is not None:
            self.action_code_break = m.get('ActionCodeBreak')

        if m.get('ActionCodeTimeBreak') is not None:
            self.action_code_time_break = m.get('ActionCodeTimeBreak')

        if m.get('AsrBaseId') is not None:
            self.asr_base_id = m.get('AsrBaseId')

        if m.get('AsrModelId') is not None:
            self.asr_model_id = m.get('AsrModelId')

        if m.get('BackgroundFileCode') is not None:
            self.background_file_code = m.get('BackgroundFileCode')

        if m.get('BackgroundSpeed') is not None:
            self.background_speed = m.get('BackgroundSpeed')

        if m.get('BackgroundVolume') is not None:
            self.background_volume = m.get('BackgroundVolume')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')

        if m.get('DynamicId') is not None:
            self.dynamic_id = m.get('DynamicId')

        if m.get('EarlyMediaAsr') is not None:
            self.early_media_asr = m.get('EarlyMediaAsr')

        if m.get('EnableITN') is not None:
            self.enable_itn = m.get('EnableITN')

        if m.get('MuteTime') is not None:
            self.mute_time = m.get('MuteTime')

        if m.get('NoiseThreshold') is not None:
            self.noise_threshold = m.get('NoiseThreshold')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PauseTime') is not None:
            self.pause_time = m.get('PauseTime')

        if m.get('RecordFlag') is not None:
            self.record_flag = m.get('RecordFlag')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('StreamAsr') is not None:
            self.stream_asr = m.get('StreamAsr')

        if m.get('TtsConf') is not None:
            self.tts_conf = m.get('TtsConf')

        if m.get('TtsSpeed') is not None:
            self.tts_speed = m.get('TtsSpeed')

        if m.get('TtsStyle') is not None:
            self.tts_style = m.get('TtsStyle')

        if m.get('TtsVolume') is not None:
            self.tts_volume = m.get('TtsVolume')

        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')

        if m.get('VoiceCodeParam') is not None:
            self.voice_code_param = m.get('VoiceCodeParam')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

