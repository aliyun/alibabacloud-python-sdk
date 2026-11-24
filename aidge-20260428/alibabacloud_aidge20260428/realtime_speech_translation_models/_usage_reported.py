# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aidge20260428 import realtime_speech_translation_models as main_models
from darabonba.model import DaraModel

class UsageReported(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        session_id: str = None,
        usage_id: str = None,
        status: str = None,
        usage_map: main_models.UsageReportedUsageMap = None,
    ):
        self.type = type
        self.event_id = event_id
        self.session_id = session_id
        # 与计量上报使用相同的稳定标识；不以 event_id 或翻译 segment_id 代替。
        self.usage_id = usage_id
        # 仅在真实 MQ 接收用量后发送；不表示已完成扣费或出账。
        self.status = status
        # 单次用量记录，不是会话累计值；字段名称及字符串值与计量上报保持一致。
        self.usage_map = usage_map

    def validate(self):
        if self.usage_map:
            self.usage_map.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.event_id is not None:
            result['event_id'] = self.event_id

        if self.session_id is not None:
            result['session_id'] = self.session_id

        if self.usage_id is not None:
            result['usage_id'] = self.usage_id

        if self.status is not None:
            result['status'] = self.status

        if self.usage_map is not None:
            result['usageMap'] = self.usage_map.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('usage_id') is not None:
            self.usage_id = m.get('usage_id')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('usageMap') is not None:
            temp_model = main_models.UsageReportedUsageMap()
            self.usage_map = temp_model.from_map(m.get('usageMap'))

        return self

class UsageReportedUsageMap(DaraModel):
    def __init__(
        self,
        input_audio_seconds: str = None,
        voice_translation_type: str = None,
    ):
        # 每段按采样时长独立四舍五入为整数秒，以字符串返回，允许为 "0"。
        self.input_audio_seconds = input_audio_seconds
        self.voice_translation_type = voice_translation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_audio_seconds is not None:
            result['InputAudioSeconds'] = self.input_audio_seconds

        if self.voice_translation_type is not None:
            result['VoiceTranslationType'] = self.voice_translation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputAudioSeconds') is not None:
            self.input_audio_seconds = m.get('InputAudioSeconds')

        if m.get('VoiceTranslationType') is not None:
            self.voice_translation_type = m.get('VoiceTranslationType')

        return self

