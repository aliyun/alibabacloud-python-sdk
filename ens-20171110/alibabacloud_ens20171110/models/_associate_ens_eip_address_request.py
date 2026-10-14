# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociateEnsEipAddressRequest(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        standby: bool = None,
    ):
        # The ID of the EIP to be associated.
        # 
        # This parameter is required.
        self.allocation_id = allocation_id
        # The ID of the cloud product instance to attach the EIP to.
        # >Load balancing (ELB) instance IDs are supported.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the EIP instance. Valid values:
        # 
        # - **Nat**: NAT gateway.
        # - **SlbInstance**: load balancing (ELB).
        # - **NetworkInterface**: secondary network interface controller (NIC).
        # - **NatSlbInstance**: select this value when attaching multiple EIPs to an ELB.
        # - **EnsInstance** (default): ENS instance.
        self.instance_type = instance_type
        # Specifies whether the EIP is a standby EIP. Valid values:
        # 
        # - true: standby.
        # 
        # - false: not standby.
        self.standby = standby

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.standby is not None:
            result['Standby'] = self.standby

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Standby') is not None:
            self.standby = m.get('Standby')

        return self

