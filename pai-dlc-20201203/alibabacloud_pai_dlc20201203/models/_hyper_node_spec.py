# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HyperNodeSpec(DaraModel):
    def __init__(
        self,
        hyper_node_name: str = None,
        node_names: str = None,
    ):
        self.hyper_node_name = hyper_node_name
        self.node_names = node_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hyper_node_name is not None:
            result['HyperNodeName'] = self.hyper_node_name

        if self.node_names is not None:
            result['NodeNames'] = self.node_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HyperNodeName') is not None:
            self.hyper_node_name = m.get('HyperNodeName')

        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')

        return self

