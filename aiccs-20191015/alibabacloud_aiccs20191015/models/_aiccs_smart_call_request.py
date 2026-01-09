# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AiccsSmartCallRequest(DaraModel):
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
        self.action_code_break = action_code_break
        self.action_code_time_break = action_code_time_break
        self.asr_als_am_id = asr_als_am_id
        self.asr_base_id = asr_base_id
        self.asr_model_id = asr_model_id
        self.asr_vocabulary_id = asr_vocabulary_id
        self.background_file_code = background_file_code
        self.background_speed = background_speed
        self.background_volume = background_volume
        # This parameter is required.
        self.called_number = called_number
        # This parameter is required.
        self.called_show_number = called_show_number
        self.dynamic_id = dynamic_id
        self.early_media_asr = early_media_asr
        self.enable_itn = enable_itn
        self.mute_time = mute_time
        self.out_id = out_id
        self.owner_id = owner_id
        self.pause_time = pause_time
        self.play_times = play_times
        self.prod_code = prod_code
        self.record_flag = record_flag
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.session_timeout = session_timeout
        self.speed = speed
        self.tts_conf = tts_conf
        self.tts_speed = tts_speed
        self.tts_style = tts_style
        self.tts_volume = tts_volume
        # This parameter is required.
        self.voice_code = voice_code
        self.voice_code_param = voice_code_param
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

