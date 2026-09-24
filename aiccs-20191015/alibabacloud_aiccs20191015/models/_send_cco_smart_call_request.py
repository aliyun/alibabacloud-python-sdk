# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendCcoSmartCallRequest(DaraModel):
    def __init__(
        self,
        action_code_break: bool = None,
        action_code_time_break: int = None,
        asr_als_am_id: str = None,
        asr_base_id: str = None,
        asr_model_id: str = None,
        asr_vocabulary_id: str = None,
        background_file_code: str = None,
        background_speed: int = None,
        background_volume: int = None,
        called_number: str = None,
        called_show_number: str = None,
        dynamic_id: str = None,
        early_media_asr: bool = None,
        enable_itn: bool = None,
        mute_time: int = None,
        out_id: str = None,
        owner_id: int = None,
        pause_time: int = None,
        play_times: int = None,
        prod_code: str = None,
        record_flag: bool = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        session_timeout: int = None,
        speed: int = None,
        tts_conf: bool = None,
        tts_speed: int = None,
        tts_style: str = None,
        tts_volume: int = None,
        voice_code: str = None,
        voice_code_param: str = None,
        volume: int = None,
    ):
        # Specifies whether the opening audio file can be interrupted. Default value: **true**, which indicates the opening audio file can be interrupted.
        self.action_code_break = action_code_break
        # The duration threshold for interrupting based on continuous user speech. This parameter takes effect only when ActionCodeBreak is set to **true**. Unit: milliseconds.
        self.action_code_time_break = action_code_time_break
        # The acoustic model ID.
        self.asr_als_am_id = asr_als_am_id
        # The ASR foundation model.
        # 
        # - **customer_service_8k**: Mandarin.
        # - **dialect_customer_service_8k**: Heavy accent.
        # - If only **asrModelId** is set, the specified ASR model is used.
        # - If only **AsrBaseId** is set, the specified ASR foundation model is used.
        # - If neither is set, the default ASR foundation model is used. The default value of **AsrBaseId** is **customer_service_8k**, which indicates the ASR Mandarin foundation model.
        # - If both are set, make sure they correspond correctly. 
        # 
        # > When you call the **SendCcoSmartCall** operation, specify the ASR model to use. Set either **asrModelId** or **AsrBaseId**.
        self.asr_base_id = asr_base_id
        # The ASR model ID. View the ASR model ID on the [ASR Model Management page](https://aiccs.console.aliyun.com/sentence/model/private?spm=a2c4g.11186623.0.0.7f9b2964fYSGv4).
        self.asr_model_id = asr_model_id
        # The hot word ID. View the ASR hot word ID on the [ASR Hot Word Management page](https://aiccs.console.aliyun.com/sentence/vocab?spm=a2c4g.11186623.0.0.7f9bf965IKBpsi).
        self.asr_vocabulary_id = asr_vocabulary_id
        # The ID of the background audio file played during the conversation between the user and the robot. Log on to the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview), choose **Intelligent Interaction > Voice File Management**, and click **Details** to view the corresponding voice ID.
        self.background_file_code = background_file_code
        # This parameter is not supported.
        self.background_speed = background_speed
        # This parameter is not supported.
        self.background_volume = background_volume
        # The called number. Only numbers in the Chinese mainland are supported.
        # 
        # This parameter is required.
        self.called_number = called_number
        # The China-only caller ID displayed to the called party. The number must be a purchased number.
        # 
        # Log on to the [Contact Center console](https://aiccs.console.aliyun.com/overview?spm=a2c4g.11186623.0.0.7f9bf9658X6jte) to view purchased numbers.
        # 
        # This parameter is required.
        self.called_show_number = called_show_number
        # The dynamic extension ID reserved for the caller. This ID is returned in the callback URL for the caller\\"s development identifier.
        self.dynamic_id = dynamic_id
        # The early media speech recognition flag. If set to true, the reason for unanswered calls is recorded. Default value: **false**, which indicates the feature is disabled.
        # 
        # > To enable early media speech recognition, manually set this parameter to **true**.
        self.early_media_asr = early_media_asr
        # Specifies whether to perform Inverse Text Normalization (ITN) in post-processing.
        # 
        # > When set to **true**, Chinese numerals are converted to Arabic numerals in the output. Default value: **false**.
        self.enable_itn = enable_itn
        # The silence duration. Specifies how long the call ends after the user stops speaking. Unit: milliseconds. Valid values: **1000 to 20000**.
        # 
        # - If the specified value is outside this range, the default value of **10000** is used.
        # - This parameter can be dynamically set during the call. The last setting takes effect.
        self.mute_time = mute_time
        # The ID reserved for the caller. This ID is returned to the caller in the receipt message. The value is a string of 1 to 15 bytes.
        self.out_id = out_id
        self.owner_id = owner_id
        # The pause duration. Specifies how long a user pause indicates the end of a sentence. Unit: milliseconds. Valid values: **300 to 1200**. If the specified value is outside this range, the default value of **800** is used.
        # 
        # > Only the first setting takes effect. Subsequent settings are ignored.
        self.pause_time = pause_time
        # This parameter is not supported.
        self.play_times = play_times
        # The product name. Default value: **aiccs**.
        self.prod_code = prod_code
        # Specifies whether to record the call. Valid values:
        # - **true**: Record the call.
        # - **false**: Do not record the call.
        self.record_flag = record_flag
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The maximum call duration. Unit: seconds. The call is automatically hung up after the timeout.
        self.session_timeout = session_timeout
        # This parameter is not supported.
        self.speed = speed
        # Specifies whether to set TTS voice parameters. Valid values:
        # - **true**: Set the voice style by using the TtsStyle, TtsVolume, and TtsSpeed parameters.
        # - **false**: Do not set the related parameters. Even if they are set, they do not take effect.
        self.tts_conf = tts_conf
        # The voice speed for TTS variable playback. Valid values: -200 to 200. Default value: 0.
        self.tts_speed = tts_speed
        # The voice style for TTS variable playback. Default value: **xiaoyun**. For specific styles, refer to the voice style list.
        self.tts_style = tts_style
        # The volume for TTS variable playback. Valid values: **0 to 100**. Default value: **0**.
        self.tts_volume = tts_volume
        # The intelligent outbound call audio file. Network files and text-to-speech (TTS) are supported. Multiple files and TTS parameters can be mixed and separated by commas (,). The replacement values for TTS parameters are specified in **VoiceCodeParam**.
        # 
        # - When the audio file is a network file: Set VoiceCode to a public network access audio file URL. Use a WAV format audio file with a sampling frequency of 8000 Hz or 16000 Hz.
        # - When the audio file is TTS: Set VoiceCode to a variable name such as $name$, and set the corresponding content for the variable in VoiceCodeParam in **Settings**.
        # 
        # This parameter is required.
        self.voice_code = voice_code
        # The TTS parameter string in JSON format. This parameter must correspond to the TTS parameters in VoiceCode.
        self.voice_code_param = voice_code_param
        # The volume for playing user audio. Valid values: -4 to 4. Set this parameter to 1.
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

        if self.asr_als_am_id is not None:
            result['AsrAlsAmId'] = self.asr_als_am_id

        if self.asr_base_id is not None:
            result['AsrBaseId'] = self.asr_base_id

        if self.asr_model_id is not None:
            result['AsrModelId'] = self.asr_model_id

        if self.asr_vocabulary_id is not None:
            result['AsrVocabularyId'] = self.asr_vocabulary_id

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

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pause_time is not None:
            result['PauseTime'] = self.pause_time

        if self.play_times is not None:
            result['PlayTimes'] = self.play_times

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

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

        if m.get('AsrAlsAmId') is not None:
            self.asr_als_am_id = m.get('AsrAlsAmId')

        if m.get('AsrBaseId') is not None:
            self.asr_base_id = m.get('AsrBaseId')

        if m.get('AsrModelId') is not None:
            self.asr_model_id = m.get('AsrModelId')

        if m.get('AsrVocabularyId') is not None:
            self.asr_vocabulary_id = m.get('AsrVocabularyId')

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

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PauseTime') is not None:
            self.pause_time = m.get('PauseTime')

        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

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

