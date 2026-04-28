# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LinkInfo(DaraModel):
    def __init__(
        self,
        extra: str = None,
        identity: str = None,
        type: str = None,
    ):
        self.extra = extra
        self.identity = identity
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['extra'] = self.extra

        if self.identity is not None:
            result['identity'] = self.identity

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('identity') is not None:
            self.identity = m.get('identity')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

