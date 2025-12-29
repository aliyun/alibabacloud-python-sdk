# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExternalAgentRequest(DaraModel):
    def __init__(
        self,
        agent_mode: str = None,
        private_ip_address: str = None,
    ):
        # The permission mode of the agent. Valid values:
        # 
        # admin: the admin mode, which provides full permissions. restricted: the restricted mode, which provides partial permissions. Default value: admin.
        self.agent_mode = agent_mode
        # Specifies whether to obtain the credentials that are used to access the cluster over the internal network.
        # 
        # *   `true`: obtains the credentials that are used to access the cluster over the internal network.
        # *   `false`: obtains the credentials that are used to access the cluster over the Internet.
        # 
        # Default value: `false`.
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_mode is not None:
            result['AgentMode'] = self.agent_mode

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentMode') is not None:
            self.agent_mode = m.get('AgentMode')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        return self

