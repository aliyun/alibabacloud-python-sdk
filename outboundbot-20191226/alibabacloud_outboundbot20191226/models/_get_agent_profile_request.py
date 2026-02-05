# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentProfileRequest(DaraModel):
    def __init__(
        self,
        agent_profile_id: str = None,
        app_ip: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.agent_profile_id = agent_profile_id
        self.app_ip = app_ip
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_profile_id is not None:
            result['AgentProfileId'] = self.agent_profile_id

        if self.app_ip is not None:
            result['AppIp'] = self.app_ip

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentProfileId') is not None:
            self.agent_profile_id = m.get('AgentProfileId')

        if m.get('AppIp') is not None:
            self.app_ip = m.get('AppIp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

