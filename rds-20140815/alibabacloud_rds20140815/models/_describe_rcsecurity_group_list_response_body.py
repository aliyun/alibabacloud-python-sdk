# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCSecurityGroupListResponseBody(DaraModel):
    def __init__(
        self,
        rcsecurity_groups: List[main_models.DescribeRCSecurityGroupListResponseBodyRCSecurityGroups] = None,
        request_id: str = None,
    ):
        # The basic information about the security groups.
        self.rcsecurity_groups = rcsecurity_groups
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.rcsecurity_groups:
            for v1 in self.rcsecurity_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RCSecurityGroups'] = []
        if self.rcsecurity_groups is not None:
            for k1 in self.rcsecurity_groups:
                result['RCSecurityGroups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rcsecurity_groups = []
        if m.get('RCSecurityGroups') is not None:
            for k1 in m.get('RCSecurityGroups'):
                temp_model = main_models.DescribeRCSecurityGroupListResponseBodyRCSecurityGroups()
                self.rcsecurity_groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRCSecurityGroupListResponseBodyRCSecurityGroups(DaraModel):
    def __init__(
        self,
        available_instance_amount: int = None,
        creation_time: str = None,
        description: str = None,
        instance_count: int = None,
        security_group_id: str = None,
        security_group_type: str = None,
        vpc_id: str = None,
    ):
        # The number of instances that can be added to the security group.
        self.available_instance_amount = available_instance_amount
        # The time when the security group was created. The time follows the ISO 8601 standard and is in the `yyyy-MM-ddThh:mmZ` format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the security group.
        self.description = description
        # The number of instances that are added to the security group.
        # 
        # This parameter is required.
        self.instance_count = instance_count
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The type of the security group. Valid values:
        # 
        # *   **normal**: a normal security group.
        # *   **enterprise**: an advanced security group.
        self.security_group_type = security_group_type
        # The ID of the VPC to which the security group belongs.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_instance_amount is not None:
            result['AvailableInstanceAmount'] = self.available_instance_amount

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_type is not None:
            result['SecurityGroupType'] = self.security_group_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableInstanceAmount') is not None:
            self.available_instance_amount = m.get('AvailableInstanceAmount')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupType') is not None:
            self.security_group_type = m.get('SecurityGroupType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

