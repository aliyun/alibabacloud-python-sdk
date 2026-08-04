# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceGroupRequestRequest(DaraModel):
    def __init__(
        self,
        pod_status: str = None,
        resource_group_id: str = None,
    ):
        # The container status. Valid values:
        # 
        # - Waiting
        # - Running
        # - Terminated
        self.pod_status = pod_status
        # The resource group ID. Each resource group has a globally unique resource group ID. You can use the resource group ID to obtain information about the resource group.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pod_status is not None:
            result['PodStatus'] = self.pod_status

        if self.resource_group_id is not None:
            result['ResourceGroupID'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PodStatus') is not None:
            self.pod_status = m.get('PodStatus')

        if m.get('ResourceGroupID') is not None:
            self.resource_group_id = m.get('ResourceGroupID')

        return self

