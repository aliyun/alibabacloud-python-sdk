# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListNetworkAccessEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        network_access_endpoints: List[main_models.ListNetworkAccessEndpointsResponseBodyNetworkAccessEndpoints] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of network access endpoints.
        self.network_access_endpoints = network_access_endpoints
        # The pagination token returned by this call.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries in the list.
        self.total_count = total_count

    def validate(self):
        if self.network_access_endpoints:
            for v1 in self.network_access_endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkAccessEndpoints'] = []
        if self.network_access_endpoints is not None:
            for k1 in self.network_access_endpoints:
                result['NetworkAccessEndpoints'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_access_endpoints = []
        if m.get('NetworkAccessEndpoints') is not None:
            for k1 in m.get('NetworkAccessEndpoints'):
                temp_model = main_models.ListNetworkAccessEndpointsResponseBodyNetworkAccessEndpoints()
                self.network_access_endpoints.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNetworkAccessEndpointsResponseBodyNetworkAccessEndpoints(DaraModel):
    def __init__(
        self,
        backup_vpc_endpoint: main_models.ListNetworkAccessEndpointsResponseBodyNetworkAccessEndpointsBackupVpcEndpoint = None,
        create_time: int = None,
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
        self.backup_vpc_endpoint = backup_vpc_endpoint
        # The creation time of the network access endpoint. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # The network access endpoint ID.
        self.network_access_endpoint_id = network_access_endpoint_id
        # The network access endpoint name.
        self.network_access_endpoint_name = network_access_endpoint_name
        # The type of the network access endpoint. Valid values:
        # 
        # - shared: Shared network access endpoint.
        # - private: Dedicated network access endpoint.
        self.network_access_endpoint_type = network_access_endpoint_type
        # The security group ID used by the dedicated network access endpoint.
        self.security_group_id = security_group_id
        # The status of the network access endpoint. Valid values:
        #  
        # - pending: Pending initialization.
        # - creating: Being created.
        # - running: Running.
        # - deleting: Being deleted.
        self.status = status
        # The last update time of the network access endpoint. The value is a UNIX timestamp in milliseconds.
        self.update_time = update_time
        # The list of vSwitches for the dedicated network access endpoint.
        self.v_switch_ids = v_switch_ids
        # The VPC ID of the dedicated network access endpoint.
        self.vpc_id = vpc_id
        # The region of the VPC for the dedicated network access endpoint.
        self.vpc_region_id = vpc_region_id

    def validate(self):
        if self.backup_vpc_endpoint:
            self.backup_vpc_endpoint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_vpc_endpoint is not None:
            result['BackupVpcEndpoint'] = self.backup_vpc_endpoint.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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
        if m.get('BackupVpcEndpoint') is not None:
            temp_model = main_models.ListNetworkAccessEndpointsResponseBodyNetworkAccessEndpointsBackupVpcEndpoint()
            self.backup_vpc_endpoint = temp_model.from_map(m.get('BackupVpcEndpoint'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

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

class ListNetworkAccessEndpointsResponseBodyNetworkAccessEndpointsBackupVpcEndpoint(DaraModel):
    def __init__(
        self,
        backup_egress_private_ip_addresses: List[str] = None,
        backup_egress_public_ip_addresses: List[str] = None,
        backup_security_group_id: str = None,
        backup_vswitch_ids: List[str] = None,
        backup_vpc_id: str = None,
        backup_vpc_region_id: str = None,
    ):
        self.backup_egress_private_ip_addresses = backup_egress_private_ip_addresses
        self.backup_egress_public_ip_addresses = backup_egress_public_ip_addresses
        self.backup_security_group_id = backup_security_group_id
        self.backup_vswitch_ids = backup_vswitch_ids
        self.backup_vpc_id = backup_vpc_id
        self.backup_vpc_region_id = backup_vpc_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_egress_private_ip_addresses is not None:
            result['BackupEgressPrivateIpAddresses'] = self.backup_egress_private_ip_addresses

        if self.backup_egress_public_ip_addresses is not None:
            result['BackupEgressPublicIpAddresses'] = self.backup_egress_public_ip_addresses

        if self.backup_security_group_id is not None:
            result['BackupSecurityGroupId'] = self.backup_security_group_id

        if self.backup_vswitch_ids is not None:
            result['BackupVSwitchIds'] = self.backup_vswitch_ids

        if self.backup_vpc_id is not None:
            result['BackupVpcId'] = self.backup_vpc_id

        if self.backup_vpc_region_id is not None:
            result['BackupVpcRegionId'] = self.backup_vpc_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEgressPrivateIpAddresses') is not None:
            self.backup_egress_private_ip_addresses = m.get('BackupEgressPrivateIpAddresses')

        if m.get('BackupEgressPublicIpAddresses') is not None:
            self.backup_egress_public_ip_addresses = m.get('BackupEgressPublicIpAddresses')

        if m.get('BackupSecurityGroupId') is not None:
            self.backup_security_group_id = m.get('BackupSecurityGroupId')

        if m.get('BackupVSwitchIds') is not None:
            self.backup_vswitch_ids = m.get('BackupVSwitchIds')

        if m.get('BackupVpcId') is not None:
            self.backup_vpc_id = m.get('BackupVpcId')

        if m.get('BackupVpcRegionId') is not None:
            self.backup_vpc_region_id = m.get('BackupVpcRegionId')

        return self

