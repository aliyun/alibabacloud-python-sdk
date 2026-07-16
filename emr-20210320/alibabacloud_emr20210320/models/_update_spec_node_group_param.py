# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSpecNodeGroupParam(DaraModel):
    def __init__(
        self,
        new_instance_type: str = None,
        node_group_id: str = None,
    ):
        self.new_instance_type = new_instance_type
        self.node_group_id = node_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_instance_type is not None:
            result['NewInstanceType'] = self.new_instance_type

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewInstanceType') is not None:
            self.new_instance_type = m.get('NewInstanceType')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        return self

