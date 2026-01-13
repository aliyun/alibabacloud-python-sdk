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
        # The ID of the execution plan.
        self.action_plan_id = action_plan_id
        # The name of the execution plan.
        self.action_plan_name = action_plan_name
        # The type of the resource.
        self.allocation_spec = allocation_spec
        # The ID of the application.
        self.app_id = app_id
        # The time when the execution plan was created.
        self.create_time = create_time
        # The expected scale of resources for the execution plan. If the ResourceType parameter is set to VcpuCapacity, the execution plan is expected to have 10000 vCPUs.
        self.desired_capacity = desired_capacity
        self.interval_minutes = interval_minutes
        # The computing power level.
        self.level = level
        # The pre-processing script. Base64 encoding is required.
        self.prolog_script = prolog_script
        # The list of resource configurations in the region where the execution plan runs.
        self.regions = regions
        # The request ID.
        self.request_id = request_id
        # Target resource type: the capacity of vCPUs or the number of execution nodes. Valid values:
        # 
        # *   VCpuCapacity
        # *   ExecutorCapacity
        self.resource_type = resource_type
        # The list of resource configurations of the execution plan runtime environment.
        self.resources = resources
        # The status of the execution plan. The possible values are as follows:
        # 
        # *   Active Instant tasks are dynamically managed only when the execution plan is in the Active state.
        # *   Inactive Instant tasks are no longer managed by execution plans in the Inactive state.
        # *   Deleting You cannot modify the parameters of an execution plan in this state.
        self.status = status
        # The size of the resources currently managed by the execution plan.
        self.total_capacity = total_capacity
        # The time when the execution plan was last modified.
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
        # The number of CPUs in the running environment.
        self.cores = cores
        # The memory size of the running environment. Unit: GiB.
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
        # The region ID of the instance.
        self.region_id = region_id
        # The list of security groups available for the execution plan in the region.
        self.security_group_ids = security_group_ids
        # The list of VSwitches available for the execution plan in the region.
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

