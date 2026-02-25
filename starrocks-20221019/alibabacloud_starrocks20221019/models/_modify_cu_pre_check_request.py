# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCuPreCheckRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        node_group_id: str = None,
        target: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The warehouse ID.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        # The number of CUs to which you want to change.
        # 
        # Valid values:
        # 
        # *   2
        # *   4
        # *   8
        # *   16
        # *   32
        # *   64
        # 
        # This parameter is required.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

