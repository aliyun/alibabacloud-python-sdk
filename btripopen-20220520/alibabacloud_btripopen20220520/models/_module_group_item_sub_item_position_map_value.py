# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModuleGroupItemSubItemPositionMapValue(DaraModel):
    def __init__(
        self,
        journey_index: int = None,
        segment_index: int = None,
    ):
        self.journey_index = journey_index
        self.segment_index = segment_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        return self

