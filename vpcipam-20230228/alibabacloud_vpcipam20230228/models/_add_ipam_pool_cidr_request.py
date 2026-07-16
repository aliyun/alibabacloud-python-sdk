# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddIpamPoolCidrRequest(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ipam_pool_id: str = None,
        netmask_length: int = None,
        region_id: str = None,
    ):
        # The CIDR block to provision.
        # 
        # > Private top-level pools support provisioning only by specifying a CIDR block.
        self.cidr = cidr
        # The client token that is used to ensure the idempotence of the request. A client-generated value that is unique across different requests. ClientToken supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the RequestId of the API request as the ClientToken. The RequestId is different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without provisioning a CIDR block for the IPAM pool. The system checks the required parameters, request format, and business limits. If the check fails, the corresponding error is returned. If the check succeeds, the error code DryRunOperation is returned.
        # - **false** (default): sends the request. After the check succeeds, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The instance ID of the IPAM pool.
        # 
        # This parameter is required.
        self.ipam_pool_id = ipam_pool_id
        # Provisions a CIDR block by specifying a netmask length.
        # 
        # > Public IPv6 top-level pools support provisioning only by specifying a netmask length.
        self.netmask_length = netmask_length
        # The ID of the IPAM hosted region.
        # 
        # You can call [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) to obtain the region ID.
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
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id

        if self.netmask_length is not None:
            result['NetmaskLength'] = self.netmask_length

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')

        if m.get('NetmaskLength') is not None:
            self.netmask_length = m.get('NetmaskLength')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

