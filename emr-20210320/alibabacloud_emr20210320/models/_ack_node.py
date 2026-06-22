# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class AckNode(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        node_selector: main_models.AckNodeSelector = None,
    ):
        # 节点ID。
        self.node_id = node_id
        # ACK节点选择器。
        self.node_selector = node_selector

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeSelector') is not None:
            temp_model = main_models.AckNodeSelector()
            self.node_selector = temp_model.from_map(m.get('NodeSelector'))

        return self

