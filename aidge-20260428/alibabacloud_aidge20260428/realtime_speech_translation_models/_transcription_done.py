# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aidge20260428 import realtime_speech_translation_models as main_models
from darabonba.model import DaraModel

class TranscriptionDone(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        session_id: str = None,
        transcription_id: str = None,
        revision: int = None,
        text: str = None,
        start_ms: int = None,
        end_ms: int = None,
        error: main_models.TranscriptionDoneError = None,
    ):
        self.type = type
        self.event_id = event_id
        self.session_id = session_id
        # 与该原文的 TranscriptionTextDelta 共享标识，不关联翻译 segment_id。
        self.transcription_id = transcription_id
        # 同一 transcription_id 内单调递增，完成后不再更新。
        self.revision = revision
        # 最终原文，可以为空；转写失败时保留已收到的 text 与 stash 合并结果，并附带 error。
        self.text = text
        # 仅已知原文起始边界时返回。
        self.start_ms = start_ms
        # 仅已知原文结束边界时返回。
        self.end_ms = end_ms
        # 仅原文转写失败时返回；正常完成时省略。
        self.error = error

    def validate(self):
        if self.error:
            self.error.validate()

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

        if self.transcription_id is not None:
            result['transcription_id'] = self.transcription_id

        if self.revision is not None:
            result['revision'] = self.revision

        if self.text is not None:
            result['text'] = self.text

        if self.start_ms is not None:
            result['start_ms'] = self.start_ms

        if self.end_ms is not None:
            result['end_ms'] = self.end_ms

        if self.error is not None:
            result['error'] = self.error.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('transcription_id') is not None:
            self.transcription_id = m.get('transcription_id')

        if m.get('revision') is not None:
            self.revision = m.get('revision')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('start_ms') is not None:
            self.start_ms = m.get('start_ms')

        if m.get('end_ms') is not None:
            self.end_ms = m.get('end_ms')

        if m.get('error') is not None:
            temp_model = main_models.TranscriptionDoneError()
            self.error = temp_model.from_map(m.get('error'))

        return self

class TranscriptionDoneError(DaraModel):
    def __init__(
        self,
        code: str = None,
    ):
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        return self

