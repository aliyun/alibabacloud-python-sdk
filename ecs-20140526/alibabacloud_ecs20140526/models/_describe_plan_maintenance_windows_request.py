# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribePlanMaintenanceWindowsRequest(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        max_results: int = None,
        next_token: str = None,
        plan_window_id: str = None,
        plan_window_name: str = None,
        region_id: str = None,
        target_resource_group_id: str = None,
        target_resource_tags: main_models.DescribePlanMaintenanceWindowsRequestTargetResourceTags = None,
    ):
        self.enable = enable
        self.max_results = max_results
        self.next_token = next_token
        self.plan_window_id = plan_window_id
        self.plan_window_name = plan_window_name
        # This parameter is required.
        self.region_id = region_id
        self.target_resource_group_id = target_resource_group_id
        self.target_resource_tags = target_resource_tags

    def validate(self):
        if self.target_resource_tags:
            self.target_resource_tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.plan_window_id is not None:
            result['PlanWindowId'] = self.plan_window_id

        if self.plan_window_name is not None:
            result['PlanWindowName'] = self.plan_window_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_resource_group_id is not None:
            result['TargetResourceGroupId'] = self.target_resource_group_id

        if self.target_resource_tags is not None:
            result['TargetResourceTags'] = self.target_resource_tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PlanWindowId') is not None:
            self.plan_window_id = m.get('PlanWindowId')

        if m.get('PlanWindowName') is not None:
            self.plan_window_name = m.get('PlanWindowName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetResourceGroupId') is not None:
            self.target_resource_group_id = m.get('TargetResourceGroupId')

        if m.get('TargetResourceTags') is not None:
            temp_model = main_models.DescribePlanMaintenanceWindowsRequestTargetResourceTags()
            self.target_resource_tags = temp_model.from_map(m.get('TargetResourceTags'))

        return self

class DescribePlanMaintenanceWindowsRequestTargetResourceTags(DaraModel):
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

