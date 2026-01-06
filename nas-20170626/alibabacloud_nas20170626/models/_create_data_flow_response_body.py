# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataFlowResponseBody(DaraModel):
    def __init__(
        self,
        data_flow_id: str = None,
        request_id: str = None,
    ):
        # The ID of the dataflow.
        self.data_flow_id = data_flow_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

