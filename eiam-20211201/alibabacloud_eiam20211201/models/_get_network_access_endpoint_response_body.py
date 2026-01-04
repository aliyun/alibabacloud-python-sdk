# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetNetworkAccessEndpointResponseBody(DaraModel):
    def __init__(
        self,
        network_access_endpoint: main_models.GetNetworkAccessEndpointResponseBodyNetworkAccessEndpoint = None,
        request_id: str = None,
    ):
        # Network endpoint information.
        self.network_access_endpoint = network_access_endpoint
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.network_access_endpoint:
            self.network_access_endpoint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_access_endpoint is not None:
            result['NetworkAccessEndpoint'] = self.network_access_endpoint.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkAccessEndpoint') is not None:
            temp_model = main_models.GetNetworkAccessEndpointResponseBodyNetworkAccessEndpoint()
            self.network_access_endpoint = temp_model.from_map(m.get('NetworkAccessEndpoint'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetNetworkAccessEndpointResponseBodyNetworkAccessEndpoint(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        egress_private_ip_addresses: List[str] = None,
        egress_public_ip_addresses: List[str] = None,
        instance_id: str = None,
        network_access_endpoint_id: str = None,
        network_access_endpoint_name: str = None,
        network_access_endpoint_type: str = None,
        security_group_id: str = None,
        status: str = None,
        update_time: int = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        vpc_region_id: str = None,
    ):
        # The time when the baseline was created.
        self.create_time = create_time
        # Public egress ip address range of the dedicated network endpoint
        # This field is returned only when NetworkEndpointType is set to private.
        self.egress_private_ip_addresses = egress_private_ip_addresses
        # Public egress ip address range of the shared network endpoint
        # This field is returned only when networkEndpointType is set to shared.
        self.egress_public_ip_addresses = egress_public_ip_addresses
        # Instance ID.
        self.instance_id = instance_id
        # The unique identifier of the network access endpoint.
        self.network_access_endpoint_id = network_access_endpoint_id
        # Private network endpoint name.
        self.network_access_endpoint_name = network_access_endpoint_name
        # Type of the Network Endpoint
        # Possible values:
        # 
        # shared: Shared network endpoint
        # 
        # private: Dedicated network endpoint
        self.network_access_endpoint_type = network_access_endpoint_type
        # The ID of the destination security group.
        self.security_group_id = security_group_id
        # Status of the Network Endpoint
        # Possible values:
        # 
        # pending: Pending initialization
        # 
        # creating: Being created
        # 
        # running: Running
        # 
        # deleting: Being deleted
        self.status = status
        # The time when the endpoint was updated.
        self.update_time = update_time
        # List of specified vSwitches associated with the dedicated network endpoint connection.
        self.v_switch_ids = v_switch_ids
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The region ID of the outbound virtual private cloud (VPC).
        self.vpc_region_id = vpc_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.egress_private_ip_addresses is not None:
            result['EgressPrivateIpAddresses'] = self.egress_private_ip_addresses

        if self.egress_public_ip_addresses is not None:
            result['EgressPublicIpAddresses'] = self.egress_public_ip_addresses

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id

        if self.network_access_endpoint_name is not None:
            result['NetworkAccessEndpointName'] = self.network_access_endpoint_name

        if self.network_access_endpoint_type is not None:
            result['NetworkAccessEndpointType'] = self.network_access_endpoint_type

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EgressPrivateIpAddresses') is not None:
            self.egress_private_ip_addresses = m.get('EgressPrivateIpAddresses')

        if m.get('EgressPublicIpAddresses') is not None:
            self.egress_public_ip_addresses = m.get('EgressPublicIpAddresses')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('NetworkAccessEndpointName') is not None:
            self.network_access_endpoint_name = m.get('NetworkAccessEndpointName')

        if m.get('NetworkAccessEndpointType') is not None:
            self.network_access_endpoint_type = m.get('NetworkAccessEndpointType')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')

        return self

