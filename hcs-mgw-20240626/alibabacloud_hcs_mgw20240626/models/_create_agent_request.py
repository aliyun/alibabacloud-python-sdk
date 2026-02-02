# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class CreateAgentRequest(DaraModel):
    def __init__(
        self,
        import_agent: main_models.CreateAgentInfo = None,
    ):
        # The details for creating the agent.
        self.import_agent = import_agent

    def validate(self):
        if self.import_agent:
            self.import_agent.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_agent is not None:
            result['ImportAgent'] = self.import_agent.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportAgent') is not None:
            temp_model = main_models.CreateAgentInfo()
            self.import_agent = temp_model.from_map(m.get('ImportAgent'))

        return self

