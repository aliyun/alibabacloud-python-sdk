# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class CreateActionPlanRequest(DaraModel):
    def __init__(
        self,
        action_plan_name: str = None,
        allocation_spec: str = None,
        app_id: str = None,
        desired_capacity: float = None,
        interval_minutes: int = None,
        level: str = None,
        prolog_script: str = None,
        regions: List[main_models.CreateActionPlanRequestRegions] = None,
        resource_type: str = None,
        resources: List[main_models.CreateActionPlanRequestResources] = None,
        script: str = None,
    ):
        # The name of the execution plan.
        self.action_plan_name = action_plan_name
        # The resource type.
        # 
        # - Standard: Standard.
        # 
        # - Dedicated: Dedicated. This type is available only to users in the whitelist.
        # 
        # - Economic: Economy. This type is available only to users in the whitelist.
        self.allocation_spec = allocation_spec
        # The application ID.
        self.app_id = app_id
        # The desired size of the resource for the execution plan. For example, if you set ResourceType to VcpuCapacity, this parameter specifies the number of vCPUs that you want to maintain for the execution plan.
        self.desired_capacity = desired_capacity
        self.interval_minutes = interval_minutes
        # The computing power level. This parameter is valid only when you set AllocationSpec to Economic. The following types are supported:
        # 
        # - General: General-purpose.
        # 
        # - Performance: Compute-optimized.
        # 
        # Default value: General
        self.level = level
        # The pre-execution script. The script must be Base64-encoded.
        self.prolog_script = prolog_script
        # A list of regional resource configurations for the runtime environment of the execution plan.
        self.regions = regions
        # The type of resource for the execution target. The value can be the vCPU capacity or the number of executor nodes. Valid values:
        # 
        # - VCpuCapacity: vCPU capacity
        # 
        # - ExecutorCapacity: number of executor nodes
        self.resource_type = resource_type
        # A list of resource configurations for the runtime environment of the execution plan. You can specify 1 to 10 resource configurations.
        self.resources = resources
        # The script to run the job. The script must be Base64-encoded.
        self.script = script

    def validate(self):
        if self.regions:
            for v1 in self.regions:
                 if v1:
                    v1.validate()
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_plan_name is not None:
            result['ActionPlanName'] = self.action_plan_name

        if self.allocation_spec is not None:
            result['AllocationSpec'] = self.allocation_spec

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity

        if self.interval_minutes is not None:
            result['IntervalMinutes'] = self.interval_minutes

        if self.level is not None:
            result['Level'] = self.level

        if self.prolog_script is not None:
            result['PrologScript'] = self.prolog_script

        result['Regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['Regions'].append(k1.to_map() if k1 else None)

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.script is not None:
            result['Script'] = self.script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPlanName') is not None:
            self.action_plan_name = m.get('ActionPlanName')

        if m.get('AllocationSpec') is not None:
            self.allocation_spec = m.get('AllocationSpec')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')

        if m.get('IntervalMinutes') is not None:
            self.interval_minutes = m.get('IntervalMinutes')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('PrologScript') is not None:
            self.prolog_script = m.get('PrologScript')

        self.regions = []
        if m.get('Regions') is not None:
            for k1 in m.get('Regions'):
                temp_model = main_models.CreateActionPlanRequestRegions()
                self.regions.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.CreateActionPlanRequestResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('Script') is not None:
            self.script = m.get('Script')

        return self

class CreateActionPlanRequestResources(DaraModel):
    def __init__(
        self,
        cores: float = None,
        memory: float = None,
    ):
        # The number of vCPUs for the runtime environment.
        self.cores = cores
        # The memory size of the runtime environment. Unit: GiB.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

class CreateActionPlanRequestRegions(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        security_group_id: List[str] = None,
        security_group_ids: List[str] = None,
        v_switch_ids: List[str] = None,
    ):
        # The region ID.
        self.region_id = region_id
        # A list of security groups that are available for the execution plan in the region. You can specify 0 to 5 security groups.
        self.security_group_id = security_group_id
        # A list of security group IDs. You can call the [DescribeSecurityGroups](https://api.aliyun.com/document/Ecs/2014-05-26/DescribeSecurityGroups) operation to query information about available security groups.
        self.security_group_ids = security_group_ids
        # A list of vSwitches that are available for the execution plan in the region. You can specify 0 to 5 vSwitches.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

