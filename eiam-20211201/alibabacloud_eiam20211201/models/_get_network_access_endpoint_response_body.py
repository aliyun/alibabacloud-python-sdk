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
        # The network access endpoint information.
        self.network_access_endpoint = network_access_endpoint
        # The request ID.
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
        backup_vpc_endpoint: main_models.GetNetworkAccessEndpointResponseBodyNetworkAccessEndpointBackupVpcEndpoint = None,
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
        self.backup_vpc_endpoint = backup_vpc_endpoint
        # The time when the network access endpoint was created. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The private egress IP address range of the dedicated network access endpoint. This parameter is returned only when NetworkEndpointType is set to private.
        self.egress_private_ip_addresses = egress_private_ip_addresses
        # The public egress IP address range of the shared network access endpoint. This parameter is returned only when NetworkEndpointType is set to shared.
        self.egress_public_ip_addresses = egress_public_ip_addresses
        # The instance ID.
        self.instance_id = instance_id
        # The ID of the dedicated network access endpoint.
        self.network_access_endpoint_id = network_access_endpoint_id
        # The name of the dedicated network access endpoint.
        self.network_access_endpoint_name = network_access_endpoint_name
        # The type of the network access endpoint. Valid values:
        # 
        # - shared: Shared network access endpoint.
        # - private: Dedicated network access endpoint.
        self.network_access_endpoint_type = network_access_endpoint_type
        # The ID of the security group used by the dedicated network access endpoint.
        self.security_group_id = security_group_id
        # The status of the network access endpoint. Valid values:
        # 
        # - pending: Pending initialization.
        # - creating: Being created.
        # - running: Running.
        # - deleting: Being deleted.
        self.status = status
        # The time when the dedicated network access endpoint was last updated. The value is a UNIX timestamp in milliseconds.
        self.update_time = update_time
        # The list of vSwitches to which the dedicated network access endpoint is connected.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC to which the dedicated network access endpoint is connected.
        self.vpc_id = vpc_id
        # The region of the VPC to which the dedicated network access endpoint is connected.
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
        if m.get('BackupVpcEndpoint') is not None:
            temp_model = main_models.GetNetworkAccessEndpointResponseBodyNetworkAccessEndpointBackupVpcEndpoint()
            self.backup_vpc_endpoint = temp_model.from_map(m.get('BackupVpcEndpoint'))

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

class GetNetworkAccessEndpointResponseBodyNetworkAccessEndpointBackupVpcEndpoint(DaraModel):
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

