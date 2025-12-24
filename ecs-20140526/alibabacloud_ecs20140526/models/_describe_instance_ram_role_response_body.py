# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceRamRoleResponseBody(DaraModel):
    def __init__(
        self,
        instance_ram_role_sets: main_models.DescribeInstanceRamRoleResponseBodyInstanceRamRoleSets = None,
        region_id: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The IDs of the ECS instances and the names of the corresponding instance RAM roles.
        self.instance_ram_role_sets = instance_ram_role_sets
        # The region ID of the ECS instances.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The number of ECS instances returned.
        self.total_count = total_count

    def validate(self):
        if self.instance_ram_role_sets:
            self.instance_ram_role_sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ram_role_sets is not None:
            result['InstanceRamRoleSets'] = self.instance_ram_role_sets.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceRamRoleSets') is not None:
            temp_model = main_models.DescribeInstanceRamRoleResponseBodyInstanceRamRoleSets()
            self.instance_ram_role_sets = temp_model.from_map(m.get('InstanceRamRoleSets'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceRamRoleResponseBodyInstanceRamRoleSets(DaraModel):
    def __init__(
        self,
        instance_ram_role_set: List[main_models.DescribeInstanceRamRoleResponseBodyInstanceRamRoleSetsInstanceRamRoleSet] = None,
    ):
        self.instance_ram_role_set = instance_ram_role_set

    def validate(self):
        if self.instance_ram_role_set:
            for v1 in self.instance_ram_role_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceRamRoleSet'] = []
        if self.instance_ram_role_set is not None:
            for k1 in self.instance_ram_role_set:
                result['InstanceRamRoleSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_ram_role_set = []
        if m.get('InstanceRamRoleSet') is not None:
            for k1 in m.get('InstanceRamRoleSet'):
                temp_model = main_models.DescribeInstanceRamRoleResponseBodyInstanceRamRoleSetsInstanceRamRoleSet()
                self.instance_ram_role_set.append(temp_model.from_map(k1))

        return self

class DescribeInstanceRamRoleResponseBodyInstanceRamRoleSetsInstanceRamRoleSet(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        ram_role_name: str = None,
    ):
        # The ID of the instance
        self.instance_id = instance_id
        # The name of the instance RAM role.
        self.ram_role_name = ram_role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        return self

