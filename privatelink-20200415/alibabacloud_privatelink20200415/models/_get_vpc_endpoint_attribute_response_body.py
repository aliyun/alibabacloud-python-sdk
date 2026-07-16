# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVpcEndpointAttributeResponseBody(DaraModel):
    def __init__(
        self,
        address_ip_version: str = None,
        bandwidth: int = None,
        connection_status: str = None,
        create_time: str = None,
        cross_region_bandwidth: int = None,
        endpoint_business_status: str = None,
        endpoint_description: str = None,
        endpoint_domain: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        endpoint_status: str = None,
        endpoint_type: str = None,
        payer: str = None,
        policy_document: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        resource_owner: bool = None,
        service_id: str = None,
        service_name: str = None,
        service_region_id: str = None,
        vpc_id: str = None,
        zone_affinity_enabled: bool = None,
        zone_private_ip_address_count: int = None,
    ):
        # The IP version. Valid values:
        # 
        # - **IPv4**: Supports IPv4 only.
        # 
        # - **DualStack**: Supports both IPv4 and IPv6.
        self.address_ip_version = address_ip_version
        # The connection bandwidth of the endpoint, in Mbps.
        self.bandwidth = bandwidth
        # The state of the endpoint connection. Valid values:
        # 
        # - **Pending**: The connection is being modified.
        # 
        # - **Connecting**: The endpoint is connecting to the endpoint service.
        # 
        # - **Connected**: The endpoint is connected to the endpoint service.
        # 
        # - **Disconnecting**: The endpoint is disconnecting from the endpoint service.
        # 
        # - **Disconnected**: The endpoint is not connected to the endpoint service.
        # 
        # - **Deleting**: The endpoint is being deleted.
        # 
        # - **ServiceDeleted**: The associated endpoint service has been deleted.
        self.connection_status = connection_status
        # The time the endpoint was created.
        self.create_time = create_time
        # The cross-region bandwidth, in Mbps.
        self.cross_region_bandwidth = cross_region_bandwidth
        # The business status of the endpoint. Valid values:
        # 
        # - **Normal**: The endpoint is running as expected.
        # 
        # - **FinancialLocked**: The endpoint is locked due to an overdue payment.
        self.endpoint_business_status = endpoint_business_status
        # The description of the endpoint.
        self.endpoint_description = endpoint_description
        # The domain name of the endpoint.
        self.endpoint_domain = endpoint_domain
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The name of the endpoint.
        self.endpoint_name = endpoint_name
        # The status of the endpoint. Valid values:
        # 
        # - **Creating**: The endpoint is being created.
        # 
        # - **Active**: The endpoint is available.
        # 
        # - **Pending**: The endpoint is being modified.
        # 
        # - **Deleting**: The endpoint is being deleted.
        self.endpoint_status = endpoint_status
        # The type of the endpoint. Valid values:
        # 
        # - **Interface**: an interface endpoint.
        # 
        # - **Reverse**: a reverse endpoint.
        # 
        # - **GatewayLoadBalancer**: a Gateway Load Balancer endpoint (GWLBe).
        self.endpoint_type = endpoint_type
        # The payer. Valid values:
        # 
        # - **Endpoint**: the service consumer.
        # 
        # - **EndpointService**: the service provider.
        self.payer = payer
        # The RAM policy. For more information about policy elements, see [Basic elements of a policy](https://help.aliyun.com/document_detail/93738.html).
        self.policy_document = policy_document
        # The ID of the region where the endpoint is located.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Indicates whether the endpoint and the endpoint service belong to the same Alibaba Cloud account. Valid values:
        # 
        # - **true**: Yes.
        # 
        # - **false**: No.
        self.resource_owner = resource_owner
        # The ID of the associated endpoint service.
        self.service_id = service_id
        # The name of the associated endpoint service.
        self.service_name = service_name
        # The region ID of the associated endpoint service.
        self.service_region_id = service_region_id
        # The ID of the VPC to which the endpoint belongs.
        self.vpc_id = vpc_id
        # Indicates whether the endpoint service\\"s domain name resolves to the endpoint\\"s IP address in the nearest zone. Valid values:
        # 
        # - **true**: Yes.
        # 
        # - **false**: No.
        self.zone_affinity_enabled = zone_affinity_enabled
        # The number of private IP addresses for the elastic network interface (ENI) in each zone. This value is always **1**.
        self.zone_private_ip_address_count = zone_private_ip_address_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cross_region_bandwidth is not None:
            result['CrossRegionBandwidth'] = self.cross_region_bandwidth

        if self.endpoint_business_status is not None:
            result['EndpointBusinessStatus'] = self.endpoint_business_status

        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description

        if self.endpoint_domain is not None:
            result['EndpointDomain'] = self.endpoint_domain

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        if self.endpoint_status is not None:
            result['EndpointStatus'] = self.endpoint_status

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.payer is not None:
            result['Payer'] = self.payer

        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled

        if self.zone_private_ip_address_count is not None:
            result['ZonePrivateIpAddressCount'] = self.zone_private_ip_address_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossRegionBandwidth') is not None:
            self.cross_region_bandwidth = m.get('CrossRegionBandwidth')

        if m.get('EndpointBusinessStatus') is not None:
            self.endpoint_business_status = m.get('EndpointBusinessStatus')

        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')

        if m.get('EndpointDomain') is not None:
            self.endpoint_domain = m.get('EndpointDomain')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        if m.get('EndpointStatus') is not None:
            self.endpoint_status = m.get('EndpointStatus')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('Payer') is not None:
            self.payer = m.get('Payer')

        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')

        if m.get('ZonePrivateIpAddressCount') is not None:
            self.zone_private_ip_address_count = m.get('ZonePrivateIpAddressCount')

        return self

