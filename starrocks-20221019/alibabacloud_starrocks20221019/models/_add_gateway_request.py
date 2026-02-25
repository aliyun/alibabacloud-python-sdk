# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddGatewayRequest(DaraModel):
    def __init__(
        self,
        fe_node_number: int = None,
        gateway_name: str = None,
        instance_id: str = None,
    ):
        self.fe_node_number = fe_node_number
        self.gateway_name = gateway_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fe_node_number is not None:
            result['FeNodeNumber'] = self.fe_node_number

        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeNodeNumber') is not None:
            self.fe_node_number = m.get('FeNodeNumber')

        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

