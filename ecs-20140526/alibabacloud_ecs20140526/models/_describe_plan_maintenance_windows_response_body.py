# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribePlanMaintenanceWindowsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        plan_maintenance_window_list: List[main_models.DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.plan_maintenance_window_list = plan_maintenance_window_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.plan_maintenance_window_list:
            for v1 in self.plan_maintenance_window_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PlanMaintenanceWindowList'] = []
        if self.plan_maintenance_window_list is not None:
            for k1 in self.plan_maintenance_window_list:
                result['PlanMaintenanceWindowList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.plan_maintenance_window_list = []
        if m.get('PlanMaintenanceWindowList') is not None:
            for k1 in m.get('PlanMaintenanceWindowList'):
                temp_model = main_models.DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowList()
                self.plan_maintenance_window_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        enable: bool = None,
        modified_time: str = None,
        plan_window_id: str = None,
        plan_window_name: str = None,
        support_maintenance_action: str = None,
        target_resource: main_models.DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowListTargetResource = None,
        time_period: main_models.DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowListTimePeriod = None,
    ):
        self.create_time = create_time
        self.enable = enable
        self.modified_time = modified_time
        self.plan_window_id = plan_window_id
        self.plan_window_name = plan_window_name
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.plan_window_id is not None:
            result['PlanWindowId'] = self.plan_window_id

        if self.plan_window_name is not None:
            result['PlanWindowName'] = self.plan_window_name

        if self.support_maintenance_action is not None:
            result['SupportMaintenanceAction'] = self.support_maintenance_action

        if self.target_resource is not None:
            result['TargetResource'] = self.target_resource.to_map()

        if self.time_period is not None:
            result['TimePeriod'] = self.time_period.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('PlanWindowId') is not None:
            self.plan_window_id = m.get('PlanWindowId')

        if m.get('PlanWindowName') is not None:
            self.plan_window_name = m.get('PlanWindowName')

        if m.get('SupportMaintenanceAction') is not None:
            self.support_maintenance_action = m.get('SupportMaintenanceAction')

        if m.get('TargetResource') is not None:
            temp_model = main_models.DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowListTargetResource()
            self.target_resource = temp_model.from_map(m.get('TargetResource'))

        if m.get('TimePeriod') is not None:
            temp_model = main_models.DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowListTimePeriod()
            self.time_period = temp_model.from_map(m.get('TimePeriod'))

        return self

class DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowListTimePeriod(DaraModel):
    def __init__(
        self,
        period_unit: str = None,
        range_list: List[main_models.DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowListTimePeriodRangeList] = None,
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
                temp_model = main_models.DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowListTimePeriodRangeList()
                self.range_list.append(temp_model.from_map(k1))

        return self

class DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowListTimePeriodRangeList(DaraModel):
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

class DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowListTargetResource(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        scope: str = None,
        tags: List[main_models.DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowListTargetResourceTags] = None,
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
                temp_model = main_models.DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowListTargetResourceTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribePlanMaintenanceWindowsResponseBodyPlanMaintenanceWindowListTargetResourceTags(DaraModel):
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

