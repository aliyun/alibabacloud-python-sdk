# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentProfileTemplateRequest(DaraModel):
    def __init__(
        self,
        agent_profile_template_id: str = None,
        app_ip: str = None,
    ):
        # This parameter is required.
        self.agent_profile_template_id = agent_profile_template_id
        self.app_ip = app_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_profile_template_id is not None:
            result['AgentProfileTemplateId'] = self.agent_profile_template_id

        if self.app_ip is not None:
            result['AppIp'] = self.app_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentProfileTemplateId') is not None:
            self.agent_profile_template_id = m.get('AgentProfileTemplateId')

        if m.get('AppIp') is not None:
            self.app_ip = m.get('AppIp')

        return self

