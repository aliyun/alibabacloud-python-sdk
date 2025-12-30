# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ChangeNodeTypesRequest(DaraModel):
    def __init__(
        self,
        node_ids: List[str] = None,
        node_type: str = None,
    ):
        self.node_ids = node_ids
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        return self

