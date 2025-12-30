# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMediaConnectFlowRequest(DaraModel):
    def __init__(
        self,
        flow_name: str = None,
        flow_region: str = None,
    ):
        # The flow name.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The region in which the flow resides.
        # 
        # This parameter is required.
        self.flow_region = flow_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.flow_region is not None:
            result['FlowRegion'] = self.flow_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('FlowRegion') is not None:
            self.flow_region = m.get('FlowRegion')

        return self

