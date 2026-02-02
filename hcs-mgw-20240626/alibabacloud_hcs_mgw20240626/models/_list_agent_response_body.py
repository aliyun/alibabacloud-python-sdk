# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class ListAgentResponseBody(DaraModel):
    def __init__(
        self,
        import_agent_list: main_models.ListAgentResp = None,
    ):
        # The details of the agents.
        self.import_agent_list = import_agent_list

    def validate(self):
        if self.import_agent_list:
            self.import_agent_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_agent_list is not None:
            result['ImportAgentList'] = self.import_agent_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportAgentList') is not None:
            temp_model = main_models.ListAgentResp()
            self.import_agent_list = temp_model.from_map(m.get('ImportAgentList'))

        return self

