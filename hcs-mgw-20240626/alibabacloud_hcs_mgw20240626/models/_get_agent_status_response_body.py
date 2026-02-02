# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class GetAgentStatusResponseBody(DaraModel):
    def __init__(
        self,
        import_agent_status: main_models.GetAgentStatusResp = None,
    ):
        # The details for obtaining the status of the agent.
        self.import_agent_status = import_agent_status

    def validate(self):
        if self.import_agent_status:
            self.import_agent_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_agent_status is not None:
            result['ImportAgentStatus'] = self.import_agent_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportAgentStatus') is not None:
            temp_model = main_models.GetAgentStatusResp()
            self.import_agent_status = temp_model.from_map(m.get('ImportAgentStatus'))

        return self

