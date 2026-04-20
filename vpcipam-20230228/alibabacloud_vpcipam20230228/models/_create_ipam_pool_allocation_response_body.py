# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIpamPoolAllocationResponseBody(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        ipam_pool_allocation_id: str = None,
        request_id: str = None,
        source_cidr: str = None,
    ):
        # The custom reserved CIDR block.
        self.cidr = cidr
        # The ID of the custom reserved CIDR block.
        self.ipam_pool_allocation_id = ipam_pool_allocation_id
        # The request ID.
        self.request_id = request_id
        # The source CIDR block.
        self.source_cidr = source_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.ipam_pool_allocation_id is not None:
            result['IpamPoolAllocationId'] = self.ipam_pool_allocation_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('IpamPoolAllocationId') is not None:
            self.ipam_pool_allocation_id = m.get('IpamPoolAllocationId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')

        return self

