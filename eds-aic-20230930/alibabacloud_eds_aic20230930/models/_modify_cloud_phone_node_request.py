# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCloudPhoneNodeRequest(DaraModel):
    def __init__(
        self,
        new_node_name: str = None,
        node_id: str = None,
        stream_mode: int = None,
    ):
        # The name that you want to assign to the cloud phone matrix.
        self.new_node_name = new_node_name
        # The ID of the cloud phone matrix.
        self.node_id = node_id
        self.stream_mode = stream_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_node_name is not None:
            result['NewNodeName'] = self.new_node_name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.stream_mode is not None:
            result['StreamMode'] = self.stream_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewNodeName') is not None:
            self.new_node_name = m.get('NewNodeName')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('StreamMode') is not None:
            self.stream_mode = m.get('StreamMode')

        return self

