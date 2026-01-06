# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMaterializedViewRecommendRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        description: str = None,
        min_rewrite_query_count: int = None,
        min_rewrite_query_pattern: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scan_queries_range: int = None,
        scheduling_day: str = None,
        scheduling_policy: str = None,
        slow_query_threshold: int = None,
        specified_time: str = None,
        task_name: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The description of the recommendation task.
        self.description = description
        # Pattern匹配的最少慢查询个数
        self.min_rewrite_query_count = min_rewrite_query_count
        # 最小可加速的Pattern数量
        self.min_rewrite_query_pattern = min_rewrite_query_pattern
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The time range for scanning data. Unit: days. Default value: 3.
        self.scan_queries_range = scan_queries_range
        # This parameter is valid only when SchedulingPolicy is set to weekly. Valid values:
        # 
        # *   Monday
        # *   Tuesday
        # *   Wednesday
        # *   Thursday
        # *   Friday
        # *   Saturday
        # *   Sunday
        # 
        # Separate multiple days with commas (,).
        self.scheduling_day = scheduling_day
        # The scheduling policy of the recommendation task. Valid values:
        # 
        # daily
        # 
        # weekly
        # 
        # This parameter is required.
        self.scheduling_policy = scheduling_policy
        # 慢查询阈值
        self.slow_query_threshold = slow_query_threshold
        # The execution time of the recommendation task. Specify the time in the HH:MM:SS format.
        # 
        # This parameter is required.
        self.specified_time = specified_time
        # The name of the recommendation task.
        # 
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.min_rewrite_query_count is not None:
            result['MinRewriteQueryCount'] = self.min_rewrite_query_count

        if self.min_rewrite_query_pattern is not None:
            result['MinRewriteQueryPattern'] = self.min_rewrite_query_pattern

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scan_queries_range is not None:
            result['ScanQueriesRange'] = self.scan_queries_range

        if self.scheduling_day is not None:
            result['SchedulingDay'] = self.scheduling_day

        if self.scheduling_policy is not None:
            result['SchedulingPolicy'] = self.scheduling_policy

        if self.slow_query_threshold is not None:
            result['SlowQueryThreshold'] = self.slow_query_threshold

        if self.specified_time is not None:
            result['SpecifiedTime'] = self.specified_time

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MinRewriteQueryCount') is not None:
            self.min_rewrite_query_count = m.get('MinRewriteQueryCount')

        if m.get('MinRewriteQueryPattern') is not None:
            self.min_rewrite_query_pattern = m.get('MinRewriteQueryPattern')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScanQueriesRange') is not None:
            self.scan_queries_range = m.get('ScanQueriesRange')

        if m.get('SchedulingDay') is not None:
            self.scheduling_day = m.get('SchedulingDay')

        if m.get('SchedulingPolicy') is not None:
            self.scheduling_policy = m.get('SchedulingPolicy')

        if m.get('SlowQueryThreshold') is not None:
            self.slow_query_threshold = m.get('SlowQueryThreshold')

        if m.get('SpecifiedTime') is not None:
            self.specified_time = m.get('SpecifiedTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

