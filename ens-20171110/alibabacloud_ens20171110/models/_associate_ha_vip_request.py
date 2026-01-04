# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociateHaVipRequest(DaraModel):
    def __init__(
        self,
        ha_vip_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
    ):
        # The ID of the HAVIP.
        # 
        # This parameter is required.
        self.ha_vip_id = ha_vip_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the instance to be associated with the HAVIP. Valid values:
        # 
        # *   EnsInstance (default): ENS instance
        # *   NetworkInterface: elastic network interface (ENI)
        self.instance_type = instance_type

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

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HaVipId') is not None:
            self.ha_vip_id = m.get('HaVipId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

