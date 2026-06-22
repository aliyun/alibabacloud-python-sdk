# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetNodeGroupResponseBody(DaraModel):
    def __init__(
        self,
        node_group: main_models.NodeGroup = None,
        request_id: str = None,
    ):
        # The node group.
        self.node_group = node_group
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.node_group:
            self.node_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_group is not None:
            result['NodeGroup'] = self.node_group.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeGroup') is not None:
            temp_model = main_models.NodeGroup()
            self.node_group = temp_model.from_map(m.get('NodeGroup'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

