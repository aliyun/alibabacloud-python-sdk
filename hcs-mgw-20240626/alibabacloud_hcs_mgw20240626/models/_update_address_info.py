# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAddressInfo(DaraModel):
    def __init__(
        self,
        agent_list: str = None,
    ):
        self.agent_list = agent_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_list is not None:
            result['AgentList'] = self.agent_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentList') is not None:
            self.agent_list = m.get('AgentList')

        return self

