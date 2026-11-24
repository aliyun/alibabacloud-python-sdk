# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TranscriptionTextDelta(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        session_id: str = None,
        text: str = None,
        start_ms: int = None,
        end_ms: int = None,
        transcription_id: str = None,
        revision: int = None,
        stash: str = None,
    ):
        self.type = type
        self.event_id = event_id
        self.session_id = session_id
        # 可回改的累计全文，按最新 revision 覆盖，不作增量拼接。
        self.text = text
        # 仅已知原文起始边界时返回。
        self.start_ms = start_ms
        # 仅已知原文结束边界时返回。
        self.end_ms = end_ms
        # 同一原文的快照与完成事件共享此标识，不关联翻译 segment_id。
        self.transcription_id = transcription_id
        # 同一 transcription_id 内单调递增；中间快照可能合并，版本号不保证连续。
        self.revision = revision
        # 可被修正的暂存文本，可为空；仅 stash 变化也会产生新版本。
        self.stash = stash

    def validate(self):
        pass

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

        if self.text is not None:
            result['text'] = self.text

        if self.start_ms is not None:
            result['start_ms'] = self.start_ms

        if self.end_ms is not None:
            result['end_ms'] = self.end_ms

        if self.transcription_id is not None:
            result['transcription_id'] = self.transcription_id

        if self.revision is not None:
            result['revision'] = self.revision

        if self.stash is not None:
            result['stash'] = self.stash

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('start_ms') is not None:
            self.start_ms = m.get('start_ms')

        if m.get('end_ms') is not None:
            self.end_ms = m.get('end_ms')

        if m.get('transcription_id') is not None:
            self.transcription_id = m.get('transcription_id')

        if m.get('revision') is not None:
            self.revision = m.get('revision')

        if m.get('stash') is not None:
            self.stash = m.get('stash')

        return self

