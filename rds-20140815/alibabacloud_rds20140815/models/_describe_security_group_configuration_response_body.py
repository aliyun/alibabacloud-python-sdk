# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityGroupConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        items: main_models.DescribeSecurityGroupConfigurationResponseBodyItems = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.dbinstance_name = dbinstance_name
        # The information about the ECS security group.
        self.items = items
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeSecurityGroupConfigurationResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSecurityGroupConfigurationResponseBodyItems(DaraModel):
    def __init__(
        self,
        ecs_security_group_relation: List[main_models.DescribeSecurityGroupConfigurationResponseBodyItemsEcsSecurityGroupRelation] = None,
    ):
        self.ecs_security_group_relation = ecs_security_group_relation

    def validate(self):
        if self.ecs_security_group_relation:
            for v1 in self.ecs_security_group_relation:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EcsSecurityGroupRelation'] = []
        if self.ecs_security_group_relation is not None:
            for k1 in self.ecs_security_group_relation:
                result['EcsSecurityGroupRelation'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_security_group_relation = []
        if m.get('EcsSecurityGroupRelation') is not None:
            for k1 in m.get('EcsSecurityGroupRelation'):
                temp_model = main_models.DescribeSecurityGroupConfigurationResponseBodyItemsEcsSecurityGroupRelation()
                self.ecs_security_group_relation.append(temp_model.from_map(k1))

        return self

class DescribeSecurityGroupConfigurationResponseBodyItemsEcsSecurityGroupRelation(DaraModel):
    def __init__(
        self,
        network_type: str = None,
        region_id: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
    ):
        # The network type of the ECS security group. Valid values:
        # 
        # *   **Classic**
        # *   **VPC**
        self.network_type = network_type
        # The region ID.
        self.region_id = region_id
        # The ID of the ECS security group.
        self.security_group_id = security_group_id
        # The security group name.
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

