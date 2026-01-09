# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class ListAvailableTtsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.ListAvailableTtsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAvailableTtsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAvailableTtsResponseBodyData(DaraModel):
    def __init__(
        self,
        tts_audition_file_url: str = None,
        tts_engine: str = None,
        tts_style: str = None,
        tts_voice_code: str = None,
        tts_voice_name: str = None,
    ):
        # 音色试听文件
        self.tts_audition_file_url = tts_audition_file_url
        # 音色平台CosyVoice/Volcano
        self.tts_engine = tts_engine
        # 音色cosy类型 cosyvoice-v2-XXXX-XXXX
        self.tts_style = tts_style
        # 音色编码
        self.tts_voice_code = tts_voice_code
        # 音色名称
        self.tts_voice_name = tts_voice_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tts_audition_file_url is not None:
            result['TtsAuditionFileUrl'] = self.tts_audition_file_url

        if self.tts_engine is not None:
            result['TtsEngine'] = self.tts_engine

        if self.tts_style is not None:
            result['TtsStyle'] = self.tts_style

        if self.tts_voice_code is not None:
            result['TtsVoiceCode'] = self.tts_voice_code

        if self.tts_voice_name is not None:
            result['TtsVoiceName'] = self.tts_voice_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TtsAuditionFileUrl') is not None:
            self.tts_audition_file_url = m.get('TtsAuditionFileUrl')

        if m.get('TtsEngine') is not None:
            self.tts_engine = m.get('TtsEngine')

        if m.get('TtsStyle') is not None:
            self.tts_style = m.get('TtsStyle')

        if m.get('TtsVoiceCode') is not None:
            self.tts_voice_code = m.get('TtsVoiceCode')

        if m.get('TtsVoiceName') is not None:
            self.tts_voice_name = m.get('TtsVoiceName')

        return self

