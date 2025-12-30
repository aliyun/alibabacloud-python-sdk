# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeResolverEndpointResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        id: str = None,
        ip_configs: List[main_models.DescribeResolverEndpointResponseBodyIpConfigs] = None,
        name: str = None,
        request_id: str = None,
        security_group_id: str = None,
        status: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_region_id: str = None,
        vpc_region_name: str = None,
    ):
        # The time when the endpoint was created.
        self.create_time = create_time
        # The time when the endpoint was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The endpoint ID. This ID uniquely identifies the endpoint.
        self.id = id
        # The configurations of the source IP addresses for outbound traffic.
        self.ip_configs = ip_configs
        # The name of the endpoint.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The ID of the security group. The security group rules are applied to the outbound virtual private cloud (VPC).
        self.security_group_id = security_group_id
        # The state of the endpoint. Valid values:
        # 
        # *   SUCCESS: The endpoint works as expected.
        # *   INIT: The endpoint is being created.
        # *   FAILED: The endpoint failed to be created.
        # *   CHANGE_INIT: The endpoint is being modified.
        # *   CHANGE_FAILED: The endpoint failed to be modified.
        # *   EXCEPTION: The endpoint encountered an exception.
        self.status = status
        # The time when the endpoint was updated.
        self.update_time = update_time
        # The time when the endpoint was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The ID of the outbound VPC. All outbound Domain Name System (DNS) requests of the resolver are forwarded by this VPC.
        self.vpc_id = vpc_id
        # The name of the outbound VPC.
        self.vpc_name = vpc_name
        # The region ID of the outbound VPC.
        self.vpc_region_id = vpc_region_id
        # The name of the region where the outbound VPC resides.
        self.vpc_region_name = vpc_region_name

    def validate(self):
        if self.ip_configs:
            for v1 in self.ip_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.id is not None:
            result['Id'] = self.id

        result['IpConfigs'] = []
        if self.ip_configs is not None:
            for k1 in self.ip_configs:
                result['IpConfigs'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id

        if self.vpc_region_name is not None:
            result['VpcRegionName'] = self.vpc_region_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.ip_configs = []
        if m.get('IpConfigs') is not None:
            for k1 in m.get('IpConfigs'):
                temp_model = main_models.DescribeResolverEndpointResponseBodyIpConfigs()
                self.ip_configs.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')

        if m.get('VpcRegionName') is not None:
            self.vpc_region_name = m.get('VpcRegionName')

        return self

class DescribeResolverEndpointResponseBodyIpConfigs(DaraModel):
    def __init__(
        self,
        az_id: str = None,
        cidr_block: str = None,
        ip: str = None,
        v_switch_id: str = None,
    ):
        # The ID of the zone to which the vSwitch belongs.
        self.az_id = az_id
        # The IPv4 CIDR block of the vSwitch.
        self.cidr_block = cidr_block
        # The source IP address of outbound traffic. The IP address must be within the specified CIDR block. If this parameter is left empty, the system automatically allocates an IP address.
        self.ip = ip
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.az_id is not None:
            result['AzId'] = self.az_id

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AzId') is not None:
            self.az_id = m.get('AzId')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

