# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateClusterAgentConfigRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        cluster_id: str = None,
        config_id: str = None,
    ):
        # The ID of the component whose configuration you want to update.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The ID of the cluster. You can call the ListClusters operation to obtain the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the component configuration to be installed on the cluster.
        # 
        # This parameter is required.
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.config_id is not None:
            result['configId'] = self.config_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('configId') is not None:
            self.config_id = m.get('configId')

        return self

