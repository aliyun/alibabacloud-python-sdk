# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyBackupPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        policy_shrink: str = None,
        policy_region_id: str = None,
        policy_version: str = None,
        uuid_list: List[str] = None,
    ):
        # The ID of the anti-ransomware mitigation policy to modify.
        # 
        # This parameter is required.
        self.id = id
        # The name of the anti-ransomware mitigation policy to modify.
        # 
        # This parameter is required.
        self.name = name
        # The content of the mitigation policy to modify. The value is a JSON-format string that contains the following fields:
        # 
        # - **Source**: The server folder to protect. To protect all folders, set this field to [].
        # - **Include**: The file types to protect. Examples: "\\*.jpg" and "\\*.doc".
        # - **Exclude**: The custom folders to exclude. For example, exclude the folder "/home/user". Invoke the DescribeExcludeSystemPath operation to obtain all folders, and then add the folders that you want to exclude.
        # - **Schedule**: The start time and interval of the data backup task. Specify a non-hourly time during off-peak hours.
        # 
        #     - Example 1: I|1583216092|P21D indicates that the start time is 2020-03-03 14:14:52 and the interval is 3 weeks.
        # 
        #     - Example 2: I|1583216092|PT24H indicates that the start time is 2020-03-03 14:14:52 and the interval is 24 hours.
        # 
        # - **Retention**: The retention period of backup data. Unit: days. 7 indicates 1 week, 365 indicates 1 year, and -1 indicates permanent retention.
        # - **SpeedLimiter**: The network bandwidth throttling for backup. Example: 12:15:15360|6:12:5120 indicates 15 MB from 12:00 to 15:00 and 5 MB from 6:00 to 12:00.
        # Cloud-hosted servers connect through the internal network. Do not limit the backup network bandwidth. To remove the bandwidth limit, set this parameter to an empty string ("").
        # 
        # This parameter is required.
        self.policy_shrink = policy_shrink
        # The region of the server for which you want to modify the mitigation policy.
        # 
        # You can invoke the [DescribeSupportRegion](~~DescribeSupportRegion~~) operation to query the regions supported by the anti-ransomware feature.
        self.policy_region_id = policy_region_id
        # The version of the mitigation policy. You can invoke the [DescribeBackupPolicies](~~DescribeBackupPolicies~~) operation to query the version.
        # 
        # - **1.0.0**
        # - **2.0.0**
        self.policy_version = policy_version
        # The UUIDs of the servers protected by the mitigation policy.
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

        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink

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
            self.policy_shrink = m.get('Policy')

        if m.get('PolicyRegionId') is not None:
            self.policy_region_id = m.get('PolicyRegionId')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

