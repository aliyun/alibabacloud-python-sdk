# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteContainerClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        force: bool = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.force is not None:
            result['Force'] = self.force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        return self

