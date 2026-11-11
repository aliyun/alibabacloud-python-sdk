# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachCommonBandwidthPackageToLoadBalancerRequest(DaraModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
    ):
        # The ID of the Internet Shared Bandwidth to be associated.
        # 
        # This parameter is required.
        self.bandwidth_package_id = bandwidth_package_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the value from your client to ensure that it is unique among different requests. The client token only supports ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run and does not associate the Internet Shared Bandwidth. The system checks whether required parameters are specified, the request format is valid, and service limits are met. If the request fails the check, an error is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # - **false** (default): sends a normal request. If the request passes the check, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the Network Load Balancer (NLB) instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The region ID of the Network Load Balancer (NLB) instance. 
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query region IDs.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

