# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityGroupConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeSecurityGroupConfigurationResponseBodyItems = None,
        request_id: str = None,
    ):
        # Details about the ECS security groups.
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
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeSecurityGroupConfigurationResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSecurityGroupConfigurationResponseBodyItems(DaraModel):
    def __init__(
        self,
        rds_ecs_security_group_rel: List[main_models.DescribeSecurityGroupConfigurationResponseBodyItemsRdsEcsSecurityGroupRel] = None,
    ):
        self.rds_ecs_security_group_rel = rds_ecs_security_group_rel

    def validate(self):
        if self.rds_ecs_security_group_rel:
            for v1 in self.rds_ecs_security_group_rel:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RdsEcsSecurityGroupRel'] = []
        if self.rds_ecs_security_group_rel is not None:
            for k1 in self.rds_ecs_security_group_rel:
                result['RdsEcsSecurityGroupRel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rds_ecs_security_group_rel = []
        if m.get('RdsEcsSecurityGroupRel') is not None:
            for k1 in m.get('RdsEcsSecurityGroupRel'):
                temp_model = main_models.DescribeSecurityGroupConfigurationResponseBodyItemsRdsEcsSecurityGroupRel()
                self.rds_ecs_security_group_rel.append(temp_model.from_map(k1))

        return self

class DescribeSecurityGroupConfigurationResponseBodyItemsRdsEcsSecurityGroupRel(DaraModel):
    def __init__(
        self,
        net_type: str = None,
        region_id: str = None,
        security_group_id: str = None,
    ):
        # The network type of the ECS security group. Valid values:
        # 
        # *   **vpc**
        # *   **classic**
        self.net_type = net_type
        # The region ID of the ECS security group.
        self.region_id = region_id
        # The ID of the ECS security group.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

