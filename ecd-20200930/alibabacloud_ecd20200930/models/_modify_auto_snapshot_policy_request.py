# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAutoSnapshotPolicyRequest(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        disk_type: str = None,
        policy_id: str = None,
        policy_name: str = None,
        region_id: str = None,
        retention_days: int = None,
    ):
        # The cron expression.
        self.cron_expression = cron_expression
        # The type of cloud disk for which the automatic snapshot policy creates snapshots.
        self.disk_type = disk_type
        # The ID of the automatic snapshot policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The name of the automatic snapshot policy. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. The name can contain digits, colons (:), underscores (_), or hyphens (-). Default value: empty.
        self.policy_name = policy_name
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The retention period of automatic snapshots. Unit: days. Valid values: 1 to 180.
        self.retention_days = retention_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

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

        return self

