# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryIncidentTracingSubNodesCountRequest(DaraModel):
    def __init__(
        self,
        vertex_id_and_type_list: List[List[str]] = None,
    ):
        # The key-value pairs that consist of node IDs and node types. A key-value pair is an array.
        self.vertex_id_and_type_list = vertex_id_and_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vertex_id_and_type_list is not None:
            result['VertexIdAndTypeList'] = self.vertex_id_and_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VertexIdAndTypeList') is not None:
            self.vertex_id_and_type_list = m.get('VertexIdAndTypeList')

        return self

