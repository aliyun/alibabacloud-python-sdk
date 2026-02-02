# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentRequest(DaraModel):
    def __init__(
        self,
        count: int = None,
        marker: str = None,
    ):
        # Specifies the number of agents to be returned.\\
        # Valid values: 0 - 1000.\\
        # Default value: 1000.
        self.count = count
        # The marker after which the agents are listed.\\
        # By default, this parameter is left empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.marker is not None:
            result['marker'] = self.marker

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        return self

