# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHyperNodeRequest(DaraModel):
    def __init__(
        self,
        hyper_node_id: str = None,
    ):
        # This parameter is required.
        self.hyper_node_id = hyper_node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hyper_node_id is not None:
            result['HyperNodeId'] = self.hyper_node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HyperNodeId') is not None:
            self.hyper_node_id = m.get('HyperNodeId')

        return self

