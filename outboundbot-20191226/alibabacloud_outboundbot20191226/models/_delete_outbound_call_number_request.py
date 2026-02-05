# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteOutboundCallNumberRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        outbound_call_number_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.outbound_call_number_id = outbound_call_number_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.outbound_call_number_id is not None:
            result['OutboundCallNumberId'] = self.outbound_call_number_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OutboundCallNumberId') is not None:
            self.outbound_call_number_id = m.get('OutboundCallNumberId')

        return self

