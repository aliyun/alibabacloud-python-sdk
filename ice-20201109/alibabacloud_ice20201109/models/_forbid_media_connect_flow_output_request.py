# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ForbidMediaConnectFlowOutputRequest(DaraModel):
    def __init__(
        self,
        flow_id: str = None,
        output_name: str = None,
    ):
        # The ID of the MediaConnect flow.
        self.flow_id = flow_id
        # The name of the output.
        self.output_name = output_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.output_name is not None:
            result['OutputName'] = self.output_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('OutputName') is not None:
            self.output_name = m.get('OutputName')

        return self

