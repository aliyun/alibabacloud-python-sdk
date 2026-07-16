# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentListRequest(DaraModel):
    def __init__(
        self,
        agent_ip: str = None,
        agent_os: str = None,
        agent_status: int = None,
        instance_id: str = None,
        lang: str = None,
        region_id: str = None,
    ):
        self.agent_ip = agent_ip
        self.agent_os = agent_os
        self.agent_status = agent_status
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_ip is not None:
            result['AgentIp'] = self.agent_ip

        if self.agent_os is not None:
            result['AgentOs'] = self.agent_os

        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIp') is not None:
            self.agent_ip = m.get('AgentIp')

        if m.get('AgentOs') is not None:
            self.agent_os = m.get('AgentOs')

        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

