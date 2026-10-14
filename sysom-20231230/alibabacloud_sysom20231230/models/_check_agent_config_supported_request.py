# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAgentConfigSupportedRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        check_type: str = None,
        clusters: str = None,
        config_id: str = None,
        content: str = None,
        instances: str = None,
    ):
        # The ID of the component to update. You can obtain the component ID from the ListAgents operation.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The configuration dimension to check, such as cluster or node.
        self.check_type = check_type
        # The cluster ID.
        self.clusters = clusters
        # The ID of the component configuration to install.
        # 
        # This parameter is required.
        self.config_id = config_id
        # The configuration content.
        self.content = content
        # The list of instances. Separate multiple instance IDs with commas (,).
        self.instances = instances

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.check_type is not None:
            result['checkType'] = self.check_type

        if self.clusters is not None:
            result['clusters'] = self.clusters

        if self.config_id is not None:
            result['configId'] = self.config_id

        if self.content is not None:
            result['content'] = self.content

        if self.instances is not None:
            result['instances'] = self.instances

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('checkType') is not None:
            self.check_type = m.get('checkType')

        if m.get('clusters') is not None:
            self.clusters = m.get('clusters')

        if m.get('configId') is not None:
            self.config_id = m.get('configId')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('instances') is not None:
            self.instances = m.get('instances')

        return self

