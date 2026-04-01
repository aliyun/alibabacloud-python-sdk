# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoSnapshotPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        auto_snapshot_policies: main_models.DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPolicies = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.auto_snapshot_policies = auto_snapshot_policies
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of automatic snapshot policies.
        self.total_count = total_count

    def validate(self):
        if self.auto_snapshot_policies:
            self.auto_snapshot_policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policies is not None:
            result['AutoSnapshotPolicies'] = self.auto_snapshot_policies.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicies') is not None:
            temp_model = main_models.DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPolicies()
            self.auto_snapshot_policies = temp_model.from_map(m.get('AutoSnapshotPolicies'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPolicies(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy: List[main_models.DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy] = None,
    ):
        self.auto_snapshot_policy = auto_snapshot_policy

    def validate(self):
        if self.auto_snapshot_policy:
            for v1 in self.auto_snapshot_policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoSnapshotPolicy'] = []
        if self.auto_snapshot_policy is not None:
            for k1 in self.auto_snapshot_policy:
                result['AutoSnapshotPolicy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_snapshot_policy = []
        if m.get('AutoSnapshotPolicy') is not None:
            for k1 in m.get('AutoSnapshotPolicy'):
                temp_model = main_models.DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy()
                self.auto_snapshot_policy.append(temp_model.from_map(k1))

        return self

class DescribeAutoSnapshotPoliciesResponseBodyAutoSnapshotPoliciesAutoSnapshotPolicy(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        auto_snapshot_policy_name: str = None,
        create_time: str = None,
        file_system_nums: int = None,
        file_system_type: str = None,
        region_id: str = None,
        repeat_weekdays: str = None,
        retention_days: int = None,
        status: str = None,
        time_points: str = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.auto_snapshot_policy_name = auto_snapshot_policy_name
        self.create_time = create_time
        self.file_system_nums = file_system_nums
        self.file_system_type = file_system_type
        self.region_id = region_id
        self.repeat_weekdays = repeat_weekdays
        self.retention_days = retention_days
        self.status = status
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id

        if self.auto_snapshot_policy_name is not None:
            result['AutoSnapshotPolicyName'] = self.auto_snapshot_policy_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.file_system_nums is not None:
            result['FileSystemNums'] = self.file_system_nums

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repeat_weekdays is not None:
            result['RepeatWeekdays'] = self.repeat_weekdays

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        if self.status is not None:
            result['Status'] = self.status

        if self.time_points is not None:
            result['TimePoints'] = self.time_points

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')

        if m.get('AutoSnapshotPolicyName') is not None:
            self.auto_snapshot_policy_name = m.get('AutoSnapshotPolicyName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FileSystemNums') is not None:
            self.file_system_nums = m.get('FileSystemNums')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepeatWeekdays') is not None:
            self.repeat_weekdays = m.get('RepeatWeekdays')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')

        return self

