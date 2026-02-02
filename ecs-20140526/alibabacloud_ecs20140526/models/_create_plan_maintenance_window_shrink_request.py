# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePlanMaintenanceWindowShrinkRequest(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        plan_window_name: str = None,
        region_id: str = None,
        support_maintenance_action: str = None,
        target_resource_shrink: str = None,
        time_period_shrink: str = None,
    ):
        # This parameter is required.
        self.enable = enable
        # This parameter is required.
        self.plan_window_name = plan_window_name
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.support_maintenance_action = support_maintenance_action
        # This parameter is required.
        self.target_resource_shrink = target_resource_shrink
        # This parameter is required.
        self.time_period_shrink = time_period_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.plan_window_name is not None:
            result['PlanWindowName'] = self.plan_window_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.support_maintenance_action is not None:
            result['SupportMaintenanceAction'] = self.support_maintenance_action

        if self.target_resource_shrink is not None:
            result['TargetResource'] = self.target_resource_shrink

        if self.time_period_shrink is not None:
            result['TimePeriod'] = self.time_period_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('PlanWindowName') is not None:
            self.plan_window_name = m.get('PlanWindowName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SupportMaintenanceAction') is not None:
            self.support_maintenance_action = m.get('SupportMaintenanceAction')

        if m.get('TargetResource') is not None:
            self.target_resource_shrink = m.get('TargetResource')

        if m.get('TimePeriod') is not None:
            self.time_period_shrink = m.get('TimePeriod')

        return self

