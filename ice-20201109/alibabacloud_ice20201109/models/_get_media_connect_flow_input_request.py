# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMediaConnectFlowInputRequest(DaraModel):
    def __init__(
        self,
        flow_id: str = None,
        with_internal_vip: str = None,
    ):
        # The flow ID.
        # 
        # This parameter is required.
        self.flow_id = flow_id
        self.with_internal_vip = with_internal_vip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.with_internal_vip is not None:
            result['WithInternalVip'] = self.with_internal_vip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('WithInternalVip') is not None:
            self.with_internal_vip = m.get('WithInternalVip')

        return self

