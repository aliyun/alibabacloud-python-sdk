# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopInvocationShrinkRequest(DaraModel):
    def __init__(
        self,
        invoke_id: str = None,
        node_id_list_shrink: str = None,
    ):
        # The execution ID.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        # The nodes.
        self.node_id_list_shrink = node_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.node_id_list_shrink is not None:
            result['NodeIdList'] = self.node_id_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('NodeIdList') is not None:
            self.node_id_list_shrink = m.get('NodeIdList')

        return self

