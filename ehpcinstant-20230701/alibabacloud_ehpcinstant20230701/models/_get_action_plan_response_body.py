# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class GetActionPlanResponseBody(DaraModel):
    def __init__(
        self,
        action_plan_id: str = None,
        action_plan_name: str = None,
        allocation_spec: str = None,
        app_id: str = None,
        create_time: str = None,
        desired_capacity: float = None,
        interval_minutes: int = None,
        level: str = None,
        prolog_script: str = None,
        regions: List[main_models.GetActionPlanResponseBodyRegions] = None,
        request_id: str = None,
        resource_type: str = None,
        resources: List[main_models.GetActionPlanResponseBodyResources] = None,
        status: str = None,
        total_capacity: float = None,
        update_time: str = None,
    ):
        # ID of the execution plan.
        self.action_plan_id = action_plan_id
        # Name of the execution plan.
        self.action_plan_name = action_plan_name
        # Resource type.
        self.allocation_spec = allocation_spec
        # ID of the application.
        self.app_id = app_id
        # Time when the execution plan was created.
        self.create_time = create_time
        # Target resource size for the execution plan. If ResourceType is VCpuCapacity, this value represents the target vCPU count.
        self.desired_capacity = desired_capacity
        self.interval_minutes = interval_minutes
        # Computing power level.
        self.level = level
        # Prologue script. Must be Base64-encoded.
        self.prolog_script = prolog_script
        # List of region-specific resource configurations for the execution plan\\"s runtime environment.
        self.regions = regions
        # ID of the request.
        self.request_id = request_id
        # Type of target resource for the execution plan. Valid values are:
        # 
        # - VCpuCapacity: vCPU capacity
        # 
        # - ExecutorCapacity: number of executor nodes
        self.resource_type = resource_type
        # List of resource configurations for the execution plan\\"s runtime environment.
        self.resources = resources
        # Status of the execution plan. Valid values are:
        # 
        # - Active: The execution plan is active and dynamically manages Instant jobs.
        # 
        # - Inactive: The execution plan is inactive and no longer manages Instant jobs.
        # 
        # - Deleting: The execution plan is being deleted. You cannot modify parameters during this state.
        self.status = status
        # Current resource size managed by the execution plan.
        self.total_capacity = total_capacity
        # Last time the execution plan was modified.
        self.update_time = update_time

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
        if self.action_plan_id is not None:
            result['ActionPlanId'] = self.action_plan_id

        if self.action_plan_name is not None:
            result['ActionPlanName'] = self.action_plan_name

        if self.allocation_spec is not None:
            result['AllocationSpec'] = self.allocation_spec

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPlanId') is not None:
            self.action_plan_id = m.get('ActionPlanId')

        if m.get('ActionPlanName') is not None:
            self.action_plan_name = m.get('ActionPlanName')

        if m.get('AllocationSpec') is not None:
            self.allocation_spec = m.get('AllocationSpec')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

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
                temp_model = main_models.GetActionPlanResponseBodyRegions()
                self.regions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.GetActionPlanResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetActionPlanResponseBodyResources(DaraModel):
    def __init__(
        self,
        cores: float = None,
        memory: float = None,
    ):
        # Number of CPUs in the runtime environment.
        self.cores = cores
        # Memory size in the runtime environment, in GiB.
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

class GetActionPlanResponseBodyRegions(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        security_group_ids: List[str] = None,
        v_switch_ids: List[str] = None,
    ):
        # ID of the region.
        self.region_id = region_id
        # List of security groups available to the execution plan in this region.
        self.security_group_ids = security_group_ids
        # List of vSwitches available to the execution plan in this region.
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

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

