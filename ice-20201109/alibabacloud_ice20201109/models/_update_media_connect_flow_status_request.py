# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMediaConnectFlowStatusRequest(DaraModel):
    def __init__(
        self,
        flow_id: str = None,
        status: str = None,
    ):
        # The flow ID.
        # 
        # This parameter is required.
        self.flow_id = flow_id
        # The flow state. Valid values:
        # 
        # *   online: starts the flow.
        # *   offline: stops the flow.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

