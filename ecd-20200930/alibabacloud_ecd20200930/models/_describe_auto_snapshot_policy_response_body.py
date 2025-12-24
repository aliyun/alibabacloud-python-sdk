# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoSnapshotPolicyResponseBody(DaraModel):
    def __init__(
        self,
        auto_snapshot_policies: List[main_models.DescribeAutoSnapshotPolicyResponseBodyAutoSnapshotPolicies] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details of the queried automatic snapshot policies.
        self.auto_snapshot_policies = auto_snapshot_policies
        # The token that is used to start the next query. If this parameter is empty, all results haven been returned.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.auto_snapshot_policies:
            for v1 in self.auto_snapshot_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoSnapshotPolicies'] = []
        if self.auto_snapshot_policies is not None:
            for k1 in self.auto_snapshot_policies:
                result['AutoSnapshotPolicies'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_snapshot_policies = []
        if m.get('AutoSnapshotPolicies') is not None:
            for k1 in m.get('AutoSnapshotPolicies'):
                temp_model = main_models.DescribeAutoSnapshotPolicyResponseBodyAutoSnapshotPolicies()
                self.auto_snapshot_policies.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAutoSnapshotPolicyResponseBodyAutoSnapshotPolicies(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        cron_expression: str = None,
        desktop_num: int = None,
        disk_type: str = None,
        policy_id: str = None,
        policy_name: str = None,
        region_id: str = None,
        retention_days: str = None,
        status: str = None,
        time_points: str = None,
    ):
        # The time when the automatic snapshot policy was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-mm-ddthh:mm:ssz` format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The cron expression that specifies when Elastic Desktop Service creates snapshots on the cloud computers.
        self.cron_expression = cron_expression
        # The number of cloud computers to which the automatic snapshot policy is applied.
        self.desktop_num = desktop_num
        self.disk_type = disk_type
        # The ID of the automatic snapshot policy.
        self.policy_id = policy_id
        # The name of the automatic snapshot policy.
        self.policy_name = policy_name
        # The ID of the region to which the automatic snapshot policy belongs.
        self.region_id = region_id
        # The retention period of the automatic snapshots. Unit: days. Valid values: 1 to 180.
        self.retention_days = retention_days
        # The status of the automatic snapshot policy.
        # 
        # Valid values:
        # 
        # *   Expire: The automatic snapshot policy cannot be used because you have overdue payments in your account.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Normal: The automatic snapshot policy is normal.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status
        # The points in time at which the auto snapshots were created.
        # 
        # The parameter values are a JSON array. Example: `["0", "1", ... "23"]`. A maximum of 24 points in time are returned. The points in time are separated with commas (,).
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.desktop_num is not None:
            result['DesktopNum'] = self.desktop_num

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        if self.status is not None:
            result['Status'] = self.status

        if self.time_points is not None:
            result['TimePoints'] = self.time_points

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('DesktopNum') is not None:
            self.desktop_num = m.get('DesktopNum')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')

        return self

