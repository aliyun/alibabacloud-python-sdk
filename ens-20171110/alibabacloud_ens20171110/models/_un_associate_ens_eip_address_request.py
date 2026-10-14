# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnAssociateEnsEipAddressRequest(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        force: bool = None,
    ):
        # The instance ID of the edge elastic IP address (EIP).
        # 
        # If the EIP is referenced by an SNAT entry, invoke DeleteSnatIpForSnatEntry to remove it first. If the EIP is referenced by a DNAT entry, invoke DeleteForwardEntry to delete it first, or set Force to true under Settings as needed.
        # 
        # This parameter is required.
        self.allocation_id = allocation_id
        # Specifies whether to forcibly disassociate the EIP when the EIP is bound to a NAT gateway that has DNAT or SNAT entries. Valid values:
        # 
        # - **false** (default): does not forcibly disassociate the EIP.
        # - **true**: forcibly disassociates the EIP.
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.force is not None:
            result['Force'] = self.force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        return self

