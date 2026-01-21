# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVpcEndpointZoneConnectionResourceAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_id: str = None,
        region_id: str = None,
        resource_allocate_mode: str = None,
        resource_id: str = None,
        resource_replace_mode: str = None,
        resource_type: str = None,
        service_id: str = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The endpoint ID.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # The region ID of the endpoint connection whose bandwidth you want to modify.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/120468.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource allocation mode. You can change the resource allocation mode only if the endpoint connection is in the **Disconnected** state. Valid values:
        # 
        # *   **Auto**: automatically and randomly allocates service resources. In this mode, the specified service resource is deleted.
        # *   **Manual**: manually allocates service resources. If you set the value to Manual, you must also specify the **ResourceId** and **ResourceType** parameters.
        self.resource_allocate_mode = resource_allocate_mode
        # The ID of the service resource that you want to manually allocate or migrate in the zone where the endpoint connection is deployed.
        # 
        # > If **ResourceAllocateMode** is set to **Mannual**, or **ResourceReplaceMode** is set, this parameter is required.
        self.resource_id = resource_id
        # The migration mode of the service resource. Valid values:
        # 
        # *   **Graceful**: smooth migration. Service resources in the zone are smoothly migrated.
        # *   **Force**: forced migration. Service resources in the zone are forcefully migrated.
        # 
        # >  You need to specify this parameter only if you want to migrate service resources and the endpoint connection is in the **Connected** state. If you specify this parameter, you must also specify the **ResourceId** and **ResourceType** parameters.
        self.resource_replace_mode = resource_replace_mode
        # The type of the service resource. Valid values:
        # 
        # *   **slb**: a CLB instance that supports PrivateLink. In addition, the CLB instance is deployed in a VPC.
        # *   **alb**: an Application Load Balancer (ALB) instance that supports PrivateLink. In addition, the ALB instance is deployed in a VPC.
        # 
        # > If **ResourceAllocateMode** is set to **Mannual**, or **ResourceReplaceMode** is set, this parameter is required.
        self.resource_type = resource_type
        # The endpoint service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The zone ID.
        # 
        # This parameter is required.
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

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_allocate_mode is not None:
            result['ResourceAllocateMode'] = self.resource_allocate_mode

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_replace_mode is not None:
            result['ResourceReplaceMode'] = self.resource_replace_mode

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

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceAllocateMode') is not None:
            self.resource_allocate_mode = m.get('ResourceAllocateMode')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceReplaceMode') is not None:
            self.resource_replace_mode = m.get('ResourceReplaceMode')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

