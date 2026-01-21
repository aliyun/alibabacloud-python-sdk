# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_privatelink20200415 import models as main_models
from darabonba.model import DaraModel

class ListVpcEndpointConnectionsResponseBody(DaraModel):
    def __init__(
        self,
        connections: List[main_models.ListVpcEndpointConnectionsResponseBodyConnections] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The endpoint connections.
        self.connections = connections
        # The number of entries returned on each page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next requests are performed.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.connections:
            for v1 in self.connections:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Connections'] = []
        if self.connections is not None:
            for k1 in self.connections:
                result['Connections'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k1 in m.get('Connections'):
                temp_model = main_models.ListVpcEndpointConnectionsResponseBodyConnections()
                self.connections.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListVpcEndpointConnectionsResponseBodyConnections(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        connection_status: str = None,
        endpoint_id: str = None,
        endpoint_owner_id: int = None,
        endpoint_region_id: str = None,
        endpoint_vpc_id: str = None,
        modified_time: str = None,
        resource_group_id: str = None,
        resource_owner: bool = None,
        service_id: str = None,
        service_region_id: str = None,
        traffic_control_mode: str = None,
        zones: List[main_models.ListVpcEndpointConnectionsResponseBodyConnectionsZones] = None,
    ):
        # The bandwidth of the endpoint connection. Valid values: **1024 to 10240**. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The state of the endpoint connection. Valid values:
        # 
        # *   **Pending**: The connection is being modified.
        # *   **Connecting**: The connection is being established.
        # *   **Connected**: The connection is established.
        # *   **Disconnecting**: The endpoint is being disconnected from the endpoint service.
        # *   **Disconnected**: The endpoint is disconnected from the endpoint service.
        # *   **Deleting**: The connection is being deleted.
        # *   **ServiceDeleted**: The corresponding endpoint service has been deleted.
        self.connection_status = connection_status
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The ID of the Alibaba Cloud account to which the endpoint belongs.
        self.endpoint_owner_id = endpoint_owner_id
        self.endpoint_region_id = endpoint_region_id
        # The ID of the virtual private cloud (VPC) to which the endpoint belongs.
        self.endpoint_vpc_id = endpoint_vpc_id
        # The time when the endpoint connection was modified.
        self.modified_time = modified_time
        # The ID of the resource group to which the endpoint belongs.
        self.resource_group_id = resource_group_id
        # Indicates whether the endpoint and the endpoint service belong to the same Alibaba Cloud account. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.resource_owner = resource_owner
        # The endpoint service ID.
        self.service_id = service_id
        self.service_region_id = service_region_id
        self.traffic_control_mode = traffic_control_mode
        # The zones.
        self.zones = zones

    def validate(self):
        if self.zones:
            for v1 in self.zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_owner_id is not None:
            result['EndpointOwnerId'] = self.endpoint_owner_id

        if self.endpoint_region_id is not None:
            result['EndpointRegionId'] = self.endpoint_region_id

        if self.endpoint_vpc_id is not None:
            result['EndpointVpcId'] = self.endpoint_vpc_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        if self.traffic_control_mode is not None:
            result['TrafficControlMode'] = self.traffic_control_mode

        result['Zones'] = []
        if self.zones is not None:
            for k1 in self.zones:
                result['Zones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointOwnerId') is not None:
            self.endpoint_owner_id = m.get('EndpointOwnerId')

        if m.get('EndpointRegionId') is not None:
            self.endpoint_region_id = m.get('EndpointRegionId')

        if m.get('EndpointVpcId') is not None:
            self.endpoint_vpc_id = m.get('EndpointVpcId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('TrafficControlMode') is not None:
            self.traffic_control_mode = m.get('TrafficControlMode')

        self.zones = []
        if m.get('Zones') is not None:
            for k1 in m.get('Zones'):
                temp_model = main_models.ListVpcEndpointConnectionsResponseBodyConnectionsZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class ListVpcEndpointConnectionsResponseBodyConnectionsZones(DaraModel):
    def __init__(
        self,
        eni_id: str = None,
        replaced_eni_id: str = None,
        replaced_resource_id: str = None,
        resource_id: str = None,
        v_switch_id: str = None,
        zone_domain: str = None,
        zone_id: str = None,
        zone_status: str = None,
    ):
        # The endpoint ENI ID.
        self.eni_id = eni_id
        # The ID of the replaced endpoint ENI in smooth migration scenarios.
        self.replaced_eni_id = replaced_eni_id
        # The ID of the replaced service resource in smooth migration scenarios.
        self.replaced_resource_id = replaced_resource_id
        # The service resource ID.
        self.resource_id = resource_id
        # The ID of the vSwitch to which the endpoint belongs.
        self.v_switch_id = v_switch_id
        # The domain name of the zone.
        self.zone_domain = zone_domain
        # The zone ID.
        self.zone_id = zone_id
        # The state of the zone. Valid values:
        # 
        # *   **Creating**: The zone is being created.
        # *   **Wait**: The zone is to be connected.
        # *   **Connected**: The zone is connected.
        # *   **Deleting**: The zone is being deleted.
        # *   **Disconnecting**: The zone is being disconnected.
        # *   **Disconnected**: The zone is disconnected.
        # *   **Connecting**: The zone is being connected.
        # *   **Migrating**: The zone is being migrated.
        # *   **Migrated**: The zone is migrated.
        self.zone_status = zone_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eni_id is not None:
            result['EniId'] = self.eni_id

        if self.replaced_eni_id is not None:
            result['ReplacedEniId'] = self.replaced_eni_id

        if self.replaced_resource_id is not None:
            result['ReplacedResourceId'] = self.replaced_resource_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_domain is not None:
            result['ZoneDomain'] = self.zone_domain

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_status is not None:
            result['ZoneStatus'] = self.zone_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')

        if m.get('ReplacedEniId') is not None:
            self.replaced_eni_id = m.get('ReplacedEniId')

        if m.get('ReplacedResourceId') is not None:
            self.replaced_resource_id = m.get('ReplacedResourceId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneDomain') is not None:
            self.zone_domain = m.get('ZoneDomain')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneStatus') is not None:
            self.zone_status = m.get('ZoneStatus')

        return self

