# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class Transcript(DaraModel):
    def __init__(
        self,
        content: str = None,
        speaker_id: str = None,
        time_range: List[int] = None,
        type: str = None,
    ):
        self.content = content
        self.speaker_id = speaker_id
        self.time_range = time_range
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.speaker_id is not None:
            result['SpeakerId'] = self.speaker_id

        if self.time_range is not None:
            result['TimeRange'] = self.time_range

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('SpeakerId') is not None:
            self.speaker_id = m.get('SpeakerId')

        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

