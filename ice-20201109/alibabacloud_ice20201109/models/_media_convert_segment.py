# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MediaConvertSegment(DaraModel):
    def __init__(
        self,
        duration: int = None,
        force_seg_time: str = None,
    ):
        self.duration = duration
        self.force_seg_time = force_seg_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.force_seg_time is not None:
            result['ForceSegTime'] = self.force_seg_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ForceSegTime') is not None:
            self.force_seg_time = m.get('ForceSegTime')

        return self

