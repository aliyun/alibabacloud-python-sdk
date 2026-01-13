# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateActionPlanShrinkRequest(DaraModel):
    def __init__(
        self,
        action_plan_name: str = None,
        allocation_spec: str = None,
        app_id: str = None,
        desired_capacity: float = None,
        interval_minutes: int = None,
        level: str = None,
        prolog_script: str = None,
        regions_shrink: str = None,
        resource_type: str = None,
        resources_shrink: str = None,
        script: str = None,
    ):
        # The name of the execution plan.
        self.action_plan_name = action_plan_name
        # The type of the resource.
        # 
        # *   Standard
        # *   Dedicated: You must enable a whitelist for use.
        # *   Economic: You must enable a whitelist for use.
        self.allocation_spec = allocation_spec
        # The ID of the application.
        self.app_id = app_id
        # The expected scale of resources for the execution plan. If the ResourceType parameter is set to VcpuCapacity, the execution plan is expected to have 10000 vCPUs.
        self.desired_capacity = desired_capacity
        self.interval_minutes = interval_minutes
        # The computing power level. This value is valid only when the resource type is Economic. The following disk categories are supported:
        # 
        # *   General
        # *   Performance
        # 
        # Default value: General
        self.level = level
        # The pre-processing script. Base64 encoding is required.
        self.prolog_script = prolog_script
        # The list of resource configurations in the region where the execution plan runs.
        self.regions_shrink = regions_shrink
        # Target resource type: the capacity of vCPUs or the number of execution nodes. Valid values:
        # 
        # *   VCpuCapacity
        # *   ExecutorCapacity
        self.resource_type = resource_type
        # The list of resource configurations of the execution plan runtime environment. You can configure 1 to 10 resources.
        self.resources_shrink = resources_shrink
        # The running-job script. Base64 encoding is required.
        self.script = script

    def validate(self):
        pass

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

        if self.regions_shrink is not None:
            result['Regions'] = self.regions_shrink

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resources_shrink is not None:
            result['Resources'] = self.resources_shrink

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

        if m.get('Regions') is not None:
            self.regions_shrink = m.get('Regions')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Resources') is not None:
            self.resources_shrink = m.get('Resources')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        return self

