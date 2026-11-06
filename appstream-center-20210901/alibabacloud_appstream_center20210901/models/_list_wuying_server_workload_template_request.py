# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWuyingServerWorkloadTemplateRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        virtual_node_pool_id: str = None,
    ):
        # A compatibility field. The current version does not read this parameter. The operation returns a fixed maximum of the first 100 templates.
        self.max_results = max_results
        # A compatibility field. The current version does not read this parameter and does not support token-based pagination.
        self.next_token = next_token
        # The ID of the virtual node pool. This parameter is **required**. The node pool must belong to the current account. You can call [ListWuyingServer](~~ListWuyingServer~~) to obtain the ID.
        # 
        # This parameter is required.
        self.virtual_node_pool_id = virtual_node_pool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.virtual_node_pool_id is not None:
            result['VirtualNodePoolId'] = self.virtual_node_pool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('VirtualNodePoolId') is not None:
            self.virtual_node_pool_id = m.get('VirtualNodePoolId')

        return self

