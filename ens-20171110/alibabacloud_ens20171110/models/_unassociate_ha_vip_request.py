# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnassociateHaVipRequest(DaraModel):
    def __init__(
        self,
        ha_vip_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the HaVip to disassociate.
        # 
        # This parameter is required.
        self.ha_vip_id = ha_vip_id
        # The ID of the ENS instance or network interface controller (NIC) to disassociate from the HaVip.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ha_vip_id is not None:
            result['HaVipId'] = self.ha_vip_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HaVipId') is not None:
            self.ha_vip_id = m.get('HaVipId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

