# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePerspectiveRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        perspective_id: str = None,
    ):
        # The key for the business space. If you do not specify this parameter, the default business space is used. You can get the key from your main account\\"s Business Management page.
        self.agent_key = agent_key
        # The ID of the perspective.
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')

        return self

