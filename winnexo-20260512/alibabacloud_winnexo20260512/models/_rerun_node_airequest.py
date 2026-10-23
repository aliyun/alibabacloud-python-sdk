# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RerunNodeAIRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        instance_id: str = None,
        node_id: str = None,
        tenant_id: str = None,
    ):
        # The collaboration workspace ID.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The physical workflow instance ID (planId).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The key of the failed node (nodeKey).
        # 
        # This parameter is required.
        self.node_id = node_id
        # The tenant ID. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

