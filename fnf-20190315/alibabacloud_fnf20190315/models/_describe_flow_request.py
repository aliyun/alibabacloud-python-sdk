# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFlowRequest(DaraModel):
    def __init__(
        self,
        flow_version: str = None,
        name: str = None,
    ):
        self.flow_version = flow_version
        # The name of the flow.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

