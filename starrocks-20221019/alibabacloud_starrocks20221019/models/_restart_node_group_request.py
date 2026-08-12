# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestartNodeGroupRequest(DaraModel):
    def __init__(
        self,
        fast_mode: bool = None,
        instance_id: str = None,
        node_group_id: str = None,
    ):
        # Whether to restart in fast mode. Default value: false.
        # 
        # - true: Restart compute nodes in fast mode. Nodes restart in batches. Within each batch, nodes restart in parallel. Between batches, restarts run sequentially.
        # 
        # - false: Restart compute nodes using rolling restart.
        self.fast_mode = fast_mode
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the compute group.
        self.node_group_id = node_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fast_mode is not None:
            result['FastMode'] = self.fast_mode

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastMode') is not None:
            self.fast_mode = m.get('FastMode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        return self

