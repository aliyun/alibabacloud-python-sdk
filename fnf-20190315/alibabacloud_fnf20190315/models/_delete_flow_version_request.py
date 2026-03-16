# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFlowVersionRequest(DaraModel):
    def __init__(
        self,
        flow_name: str = None,
        flow_version: str = None,
    ):
        # This parameter is required.
        self.flow_name = flow_name
        # This parameter is required.
        self.flow_version = flow_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')

        return self

