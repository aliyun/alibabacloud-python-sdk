# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAgentInstanceConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        attributes_shrink: str = None,
    ):
        self.attributes_shrink = attributes_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes_shrink is not None:
            result['attributes'] = self.attributes_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes_shrink = m.get('attributes')

        return self

