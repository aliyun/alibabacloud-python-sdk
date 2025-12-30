# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMediaConnectFlowInputRequest(DaraModel):
    def __init__(
        self,
        flow_id: str = None,
        input_name: str = None,
    ):
        # The flow ID.
        # 
        # This parameter is required.
        self.flow_id = flow_id
        self.input_name = input_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.input_name is not None:
            result['InputName'] = self.input_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('InputName') is not None:
            self.input_name = m.get('InputName')

        return self

