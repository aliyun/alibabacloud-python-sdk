# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListScriptsByFlowRequest(DaraModel):
    def __init__(
        self,
        flow_id: str = None,
        instance_id: str = None,
    ):
        # 流程ID
        self.flow_id = flow_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

