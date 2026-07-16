# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVpcEndpointServiceResourceAttributeRequest(DaraModel):
    def __init__(
        self,
        auto_allocated_enabled: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        resource_id: str = None,
        service_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether to enable automatic resource allocation. Valid values:
        # 
        # - **true**: Enables automatic resource allocation.
        # 
        # - **false**: Disables automatic resource allocation.
        # 
        # This parameter is required.
        self.auto_allocated_enabled = auto_allocated_enabled
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a parameter value from your client to ensure that the value is unique among different requests. **ClientToken** can contain only ASCII characters.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: sends a check request without modifying the properties of the service resource. The system checks the required parameters, request format, and service limits. If the request fails the check, an error is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): sends a normal request. After the request passes the check, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the region where you want to modify the service resource.
        # 
        # Call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The ID of the endpoint service.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The zone where the service resource is located. This parameter is required if the service resource is an Application Load Balancer (ALB), a Network Load Balancer (NLB), or a Gateway Load Balancer (GWLB).
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_allocated_enabled is not None:
            result['AutoAllocatedEnabled'] = self.auto_allocated_enabled

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAllocatedEnabled') is not None:
            self.auto_allocated_enabled = m.get('AutoAllocatedEnabled')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

