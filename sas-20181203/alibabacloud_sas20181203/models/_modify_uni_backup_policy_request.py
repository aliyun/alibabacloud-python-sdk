# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ModifyUniBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        full_plan: Dict[str, Any] = None,
        inc_plan: Dict[str, Any] = None,
        policy_id: int = None,
        policy_name: str = None,
        policy_status: str = None,
        retention: int = None,
        speed_limiter: int = None,
    ):
        # The name of the database account.
        self.account_name = account_name
        # The password of the database account.
        self.account_password = account_password
        # The policy for full backup. The value of this parameter is a JSON string that contains the following fields:
        # 
        # *   **start**: the start time of a backup task
        # *   **interval**: the interval of backup tasks
        # *   **type**: the unit of the interval
        # *   **days**: the days of a week on which a backup task is performed
        self.full_plan = full_plan
        # The policy for incremental backup. The value of this parameter is a JSON string that contains the following fields:
        # 
        # *   **start**: the start time of a backup task
        # *   **interval**: the interval of backup tasks
        # *   **type**: the unit of the interval
        # *   **days**: the days of a week on which a backup task is performed
        self.inc_plan = inc_plan
        # The ID of the anti-ransomware policy.
        # 
        # > You can call the [DescribeUniBackupPolicies](~~DescribeUniBackupPolicies~~) operation to query the IDs of anti-ransomware policies.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The name of the anti-ransomware policy.
        self.policy_name = policy_name
        # The status of the anti-ransomware policy. Valid values:
        # 
        # *   **enabled**
        # *   **disabled**
        self.policy_status = policy_status
        # The retention period of the backup snapshot.
        self.retention = retention
        # The maximum network bandwidth that is allowed during data backup. Unit: bytes.
        self.speed_limiter = speed_limiter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.full_plan is not None:
            result['FullPlan'] = self.full_plan

        if self.inc_plan is not None:
            result['IncPlan'] = self.inc_plan

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.speed_limiter is not None:
            result['SpeedLimiter'] = self.speed_limiter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('FullPlan') is not None:
            self.full_plan = m.get('FullPlan')

        if m.get('IncPlan') is not None:
            self.inc_plan = m.get('IncPlan')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('SpeedLimiter') is not None:
            self.speed_limiter = m.get('SpeedLimiter')

        return self

