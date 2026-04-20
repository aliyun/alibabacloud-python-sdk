# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIpamPoolNextAvailableCidrRequest(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        cidr_mask: int = None,
        client_token: str = None,
        ipam_pool_id: str = None,
        region_id: str = None,
    ):
        # CIDR to be allocated.
        # 
        # >  You must enter at least one of the CidrBlock and CidrMask fields.
        self.cidr_block = cidr_block
        # The length of the CIDR mask to be allocated.
        # 
        # >  You must enter at least one of the CidrBlock and CidrMask fields.
        self.cidr_mask = cidr_mask
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The ID of the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_id = ipam_pool_id
        # The region of the IPAM pool.
        # 
        # >  If the IPAM pool has the region attribute, this parameter is set to the effective region of the IPAM pool. If not, this is set to the hosted region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.cidr_mask is not None:
            result['CidrMask'] = self.cidr_mask

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('CidrMask') is not None:
            self.cidr_mask = m.get('CidrMask')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

