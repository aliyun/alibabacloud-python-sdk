# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFlowRequest(DaraModel):
    def __init__(
        self,
        flow_id: str = None,
        flow_version: int = None,
    ):
        # This parameter is required.
        self.flow_id = flow_id
        self.flow_version = flow_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')

        return self

