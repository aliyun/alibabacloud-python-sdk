# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourcesRequest(DaraModel):
    def __init__(
        self,
        cluster: str = None,
        instance: str = None,
        type: str = None,
    ):
        self.cluster = cluster
        self.instance = instance
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.instance is not None:
            result['instance'] = self.instance

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

