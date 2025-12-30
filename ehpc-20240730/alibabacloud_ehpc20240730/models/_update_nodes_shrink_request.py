# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNodesShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        instances_shrink: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The information about the compute nodes that you want to update.
        self.instances_shrink = instances_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.instances_shrink is not None:
            result['Instances'] = self.instances_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Instances') is not None:
            self.instances_shrink = m.get('Instances')

        return self

