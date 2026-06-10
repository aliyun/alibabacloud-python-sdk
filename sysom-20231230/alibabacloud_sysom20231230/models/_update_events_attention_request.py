# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEventsAttentionRequest(DaraModel):
    def __init__(
        self,
        mode: int = None,
        range: str = None,
        uuid: str = None,
    ):
        # Sensitivity of the anomalous activity. Valid values are -1 to 3. A value of -1 decreases sensitivity by 1 degree, and a value of 0 increases sensitivity by 1 degree.
        self.mode = mode
        # Scope of effect: cluster or edge zone
        self.range = range
        # UUID corresponding to the anomalous activity
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['mode'] = self.mode

        if self.range is not None:
            result['range'] = self.range

        if self.uuid is not None:
            result['uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('range') is not None:
            self.range = m.get('range')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        return self

