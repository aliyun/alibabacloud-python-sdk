# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOperationPlansForRegionRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        state: str = None,
        type: str = None,
    ):
        self.cluster_id = cluster_id
        self.state = state
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.state is not None:
            result['state'] = self.state

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

