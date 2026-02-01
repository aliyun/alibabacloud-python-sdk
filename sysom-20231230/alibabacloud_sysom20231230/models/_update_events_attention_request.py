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
        self.mode = mode
        self.range = range
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

