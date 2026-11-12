# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreateInspectionTaskRequest(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        dbcluster_list: List[main_models.CreateInspectionTaskRequestDBClusterList] = None,
        region_id: str = None,
        resource_group_id: str = None,
        space_id: str = None,
        task_description: str = None,
    ):
        # The cron expression of the inspection task, which specifies the periodic execution schedule.
        self.cron_expression = cron_expression
        # The list of clusters associated with the inspection task.
        self.dbcluster_list = dbcluster_list
        # The region ID of the task.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the inspection space. This parameter is required. If it is not provided, the API returns InvalidSpaceId.Malformed (HTTP 400).
        self.space_id = space_id
        # The description of the inspection task.
        self.task_description = task_description

    def validate(self):
        if self.dbcluster_list:
            for v1 in self.dbcluster_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        result['DBClusterList'] = []
        if self.dbcluster_list is not None:
            for k1 in self.dbcluster_list:
                result['DBClusterList'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.task_description is not None:
            result['TaskDescription'] = self.task_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        self.dbcluster_list = []
        if m.get('DBClusterList') is not None:
            for k1 in m.get('DBClusterList'):
                temp_model = main_models.CreateInspectionTaskRequestDBClusterList()
                self.dbcluster_list.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('TaskDescription') is not None:
            self.task_description = m.get('TaskDescription')

        return self

class CreateInspectionTaskRequestDBClusterList(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # The ID of the PolarDB cluster to be inspected.
        self.dbcluster_id = dbcluster_id
        # The region ID of the cluster to be inspected.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

