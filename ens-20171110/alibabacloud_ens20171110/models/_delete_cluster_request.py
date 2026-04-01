# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        retain_resources: bool = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        self.retain_resources = retain_resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.retain_resources is not None:
            result['RetainResources'] = self.retain_resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RetainResources') is not None:
            self.retain_resources = m.get('RetainResources')

        return self

