# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DirectNotifyReceiver(DaraModel):
    def __init__(
        self,
        channels: List[str] = None,
        identifiers: List[str] = None,
        target_type: str = None,
    ):
        self.channels = channels
        self.identifiers = identifiers
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['channels'] = self.channels

        if self.identifiers is not None:
            result['identifiers'] = self.identifiers

        if self.target_type is not None:
            result['targetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channels') is not None:
            self.channels = m.get('channels')

        if m.get('identifiers') is not None:
            self.identifiers = m.get('identifiers')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        return self

