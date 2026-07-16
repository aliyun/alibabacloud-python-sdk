# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachResourceFromVpcEndpointServiceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service_id: str = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a unique token for each request. The token can contain only ASCII characters.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: Performs a dry run. The system checks the request for potential issues, including missing required parameters, incorrect request format, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): Sends the request. If the request passes the check, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the region where the endpoint service is deployed. Call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to get a region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the service resource.
        # 
        # - **slb**: Classic Load Balancer (CLB).
        # 
        # - **alb**: Application Load Balancer (ALB).
        # 
        # - **nlb**: Network Load Balancer (NLB).
        # 
        # - **gwlb**: Gateway Load Balancer (GWLB).
        self.resource_type = resource_type
        # The ID of the endpoint service from which you want to remove the service resource.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The ID of the zone. This parameter is required if the service resource is an ALB, a NLB, or a GWLB. Call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to get a zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

