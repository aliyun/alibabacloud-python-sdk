# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteClusterNodesShrinkRequest(DaraModel):
    def __init__(
        self,
        body_shrink: str = None,
        cluster_id: str = None,
    ):
        # This parameter is required.
        self.body_shrink = body_shrink
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_shrink is not None:
            result['Body'] = self.body_shrink

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body_shrink = m.get('Body')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        return self

