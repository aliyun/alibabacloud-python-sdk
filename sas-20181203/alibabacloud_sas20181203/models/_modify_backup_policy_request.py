# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class ModifyBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        policy: Dict[str, Any] = None,
        policy_region_id: str = None,
        policy_version: str = None,
        uuid_list: List[str] = None,
    ):
        # The ID of the anti-ransomware policy that you want to modify.
        # 
        # This parameter is required.
        self.id = id
        # The name of the anti-ransomware policy that you want to modify.
        # 
        # This parameter is required.
        self.name = name
        # The configurations of the anti-ransomware policy that you want to modify. The value is a JSON string that contains the following fields:
        # 
        # *   **Source**: the directory that you want to protect. If you want to protect all directories, set this field to brackets [].
        # 
        # *   **Include**: the format of the file that you want to protect. Examples: \\*.jpg and \\*.doc.
        # 
        # *   **Exclude**: the directory that you want to exclude from the anti-ransomware policy. You can call the DescribeExcludeSystemPath operation to query all directories and then specify the directory that you want to exclude. Example: /home/user.
        # 
        # *   **Schedule**: the start time and interval of a data backup task. We recommend that you specify a start time that begins during off-peak hours but does not start on the hour.
        # 
        #     *   If you set this field to I|1583216092|P21D, the data backup task starts from 2020-03-03 14:14:52, and the task is executed at an interval of three weeks.
        #     *   If you set this field to I|1583216092|PT24H, the data backup task starts from 2020-03-03 14:14:52, and the task is executed at an interval of 24 hours.
        # 
        # *   **Retention**: the period during which backup data is retained. Unit: day. If you set this field to 7, backup data is retained for a week. If you set this field to 365, backup data is retained for a year. If you set this field to -1, backup data is permanently retained.
        # 
        # *   **SpeedLimiter**: the limit on the network bandwidth for data backup tasks. If you set this field to 12:15:15360|6:12:5120, the maximum bandwidth for a data backup task is 15 Mbit/s from 12:00 to 15:00 and 5 Mbit/s from 06:00 to 12:00.
        # 
        # If you back up data on an Elastic Compute Service (ECS) instance that is connected over an internal network, we recommend that you leave this field empty. If this field is left empty, the bandwidth for data backup tasks is unlimited.
        # 
        # This parameter is required.
        self.policy = policy
        # The region ID of the server to which the anti-ransomware policy is applied.
        # 
        # You can call the [DescribeSupportRegion](~~DescribeSupportRegion~~) operation to query the regions in which the anti-ransomware feature is supported.
        self.policy_region_id = policy_region_id
        # The version of the anti-ransomware policy. You can call the [DescribeBackupPolicies](~~DescribeBackupPolicies~~) operation to query the versions of anti-ransomware policies.
        # 
        # *   **1.0.0**
        # *   **2.0.0**
        self.policy_version = policy_version
        # The UUIDs of the servers to which the anti-ransomware policy is applied.
        # 
        # This parameter is required.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.policy_region_id is not None:
            result['PolicyRegionId'] = self.policy_region_id

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PolicyRegionId') is not None:
            self.policy_region_id = m.get('PolicyRegionId')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

