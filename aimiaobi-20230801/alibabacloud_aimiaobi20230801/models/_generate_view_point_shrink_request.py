# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateViewPointShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        reference_data_shrink: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.reference_data_shrink = reference_data_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.reference_data_shrink is not None:
            result['ReferenceData'] = self.reference_data_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('ReferenceData') is not None:
            self.reference_data_shrink = m.get('ReferenceData')

        return self

