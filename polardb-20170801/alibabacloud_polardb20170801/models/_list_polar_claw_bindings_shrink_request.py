# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPolarClawBindingsShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_list_shrink: str = None,
        application_id: str = None,
    ):
        self.agent_list_shrink = agent_list_shrink
        # This parameter is required.
        self.application_id = application_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_list_shrink is not None:
            result['AgentList'] = self.agent_list_shrink

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentList') is not None:
            self.agent_list_shrink = m.get('AgentList')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        return self

