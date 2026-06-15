# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePlanMaintenanceWindowsShrinkRequest(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        max_results: int = None,
        next_token: str = None,
        plan_window_id: str = None,
        plan_window_name: str = None,
        region_id: str = None,
        target_resource_group_id: str = None,
        target_resource_tags_shrink: str = None,
    ):
        # Indicates whether the maintenance window is enabled.
        self.enable = enable
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the last query as the value of NextToken.
        self.next_token = next_token
        # The ID of the maintenance window.
        self.plan_window_id = plan_window_id
        # The name of the maintenance window.
        self.plan_window_name = plan_window_name
        # The ID of the region where the ECS instance is located. You can call the DescribeRegions operation to query the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the maintenance window applies.
        self.target_resource_group_id = target_resource_group_id
        # The tags of the resources to which the maintenance window applies.
        self.target_resource_tags_shrink = target_resource_tags_shrink

    def validate(self):
        pass

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

        if self.target_resource_tags_shrink is not None:
            result['TargetResourceTags'] = self.target_resource_tags_shrink

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
            self.target_resource_tags_shrink = m.get('TargetResourceTags')

        return self

