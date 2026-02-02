# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyPlanMaintenanceWindowRequest(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        plan_window_id: str = None,
        plan_window_name: str = None,
        region_id: str = None,
        support_maintenance_action: str = None,
        target_resource: main_models.ModifyPlanMaintenanceWindowRequestTargetResource = None,
        time_period: main_models.ModifyPlanMaintenanceWindowRequestTimePeriod = None,
    ):
        self.enable = enable
        # This parameter is required.
        self.plan_window_id = plan_window_id
        self.plan_window_name = plan_window_name
        # This parameter is required.
        self.region_id = region_id
        self.support_maintenance_action = support_maintenance_action
        self.target_resource = target_resource
        self.time_period = time_period

    def validate(self):
        if self.target_resource:
            self.target_resource.validate()
        if self.time_period:
            self.time_period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.plan_window_id is not None:
            result['PlanWindowId'] = self.plan_window_id

        if self.plan_window_name is not None:
            result['PlanWindowName'] = self.plan_window_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.support_maintenance_action is not None:
            result['SupportMaintenanceAction'] = self.support_maintenance_action

        if self.target_resource is not None:
            result['TargetResource'] = self.target_resource.to_map()

        if self.time_period is not None:
            result['TimePeriod'] = self.time_period.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('PlanWindowId') is not None:
            self.plan_window_id = m.get('PlanWindowId')

        if m.get('PlanWindowName') is not None:
            self.plan_window_name = m.get('PlanWindowName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SupportMaintenanceAction') is not None:
            self.support_maintenance_action = m.get('SupportMaintenanceAction')

        if m.get('TargetResource') is not None:
            temp_model = main_models.ModifyPlanMaintenanceWindowRequestTargetResource()
            self.target_resource = temp_model.from_map(m.get('TargetResource'))

        if m.get('TimePeriod') is not None:
            temp_model = main_models.ModifyPlanMaintenanceWindowRequestTimePeriod()
            self.time_period = temp_model.from_map(m.get('TimePeriod'))

        return self

class ModifyPlanMaintenanceWindowRequestTimePeriod(DaraModel):
    def __init__(
        self,
        period_unit: str = None,
        range_list: List[main_models.ModifyPlanMaintenanceWindowRequestTimePeriodRangeList] = None,
    ):
        self.period_unit = period_unit
        self.range_list = range_list

    def validate(self):
        if self.range_list:
            for v1 in self.range_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        result['RangeList'] = []
        if self.range_list is not None:
            for k1 in self.range_list:
                result['RangeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        self.range_list = []
        if m.get('RangeList') is not None:
            for k1 in m.get('RangeList'):
                temp_model = main_models.ModifyPlanMaintenanceWindowRequestTimePeriodRangeList()
                self.range_list.append(temp_model.from_map(k1))

        return self

class ModifyPlanMaintenanceWindowRequestTimePeriodRangeList(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ModifyPlanMaintenanceWindowRequestTargetResource(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        scope: str = None,
        tags: List[main_models.ModifyPlanMaintenanceWindowRequestTargetResourceTags] = None,
    ):
        self.resource_group_id = resource_group_id
        self.scope = scope
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scope is not None:
            result['Scope'] = self.scope

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ModifyPlanMaintenanceWindowRequestTargetResourceTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ModifyPlanMaintenanceWindowRequestTargetResourceTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

