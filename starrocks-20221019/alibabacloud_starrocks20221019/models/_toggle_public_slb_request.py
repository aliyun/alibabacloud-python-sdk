# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TogglePublicSlbRequest(DaraModel):
    def __init__(
        self,
        enable_public_slb: bool = None,
        gateway_id: str = None,
        instance_id: str = None,
    ):
        self.enable_public_slb = enable_public_slb
        self.gateway_id = gateway_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_public_slb is not None:
            result['EnablePublicSlb'] = self.enable_public_slb

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePublicSlb') is not None:
            self.enable_public_slb = m.get('EnablePublicSlb')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

