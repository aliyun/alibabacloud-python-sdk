# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAllNodeRequest(DaraModel):
    def __init__(
        self,
        extended: bool = None,
    ):
        # The Java Virtual Machine (JVM) heap memory usage of the node.
        self.extended = extended

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extended is not None:
            result['extended'] = self.extended

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extended') is not None:
            self.extended = m.get('extended')

        return self

