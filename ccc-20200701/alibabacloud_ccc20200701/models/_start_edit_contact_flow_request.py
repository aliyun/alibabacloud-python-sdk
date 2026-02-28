# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartEditContactFlowRequest(DaraModel):
    def __init__(
        self,
        contact_flow_id: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.contact_flow_id = contact_flow_id
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_flow_id is not None:
            result['ContactFlowId'] = self.contact_flow_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactFlowId') is not None:
            self.contact_flow_id = m.get('ContactFlowId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

