# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DecreaseNodeGroupParam(DaraModel):
    def __init__(
        self,
        node_group_id: str = None,
        release_instance_ids: List[str] = None,
    ):
        # This parameter is required.
        self.node_group_id = node_group_id
        # This parameter is required.
        self.release_instance_ids = release_instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.release_instance_ids is not None:
            result['ReleaseInstanceIds'] = self.release_instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('ReleaseInstanceIds') is not None:
            self.release_instance_ids = m.get('ReleaseInstanceIds')

        return self

