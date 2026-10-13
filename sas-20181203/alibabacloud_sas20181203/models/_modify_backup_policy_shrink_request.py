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
        select_type: str = None,
        server_type: str = None,
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
        # The content of the policy that you want to modify. The value is a JSON string that contains the following fields:
        # 
        # - **Source**: the server directories to be protected. To protect all directories, set this field to [].
        # - **Include**: the types of files to be protected. Examples: "\\*.jpg" and "\\*.doc".
        # - **Exclude**: the custom directories to be excluded. To exclude the "/home/user" directory, call the DescribeExcludeSystemPath operation to obtain all directories and then add the directories to be excluded. Example: exclude the "/home/user" directory.
        # - **Schedule**: the start time and interval of the data backup task. Specify a time during off-peak hours and avoid exact hours.
        # 
        #     - Example 1: I|1583216092|P21D indicates that the start time is 2020-03-03 14:14:52 and the interval is 3 weeks.
        # 
        #     - Example 2: I|1583216092|PT24H indicates that the start time is 2020-03-03 14:14:52 and the interval is 24 hours.
        # 
        # - **Retention**: the retention period of backup data. Unit: days. A value of 7 indicates 1 week, 365 indicates 1 year, and -1 indicates permanent retention.
        # - **SpeedLimiter**: the bandwidth limit for the backup network. Example: 12:15:15360|6:12:5120 indicates a limit of 15 MB from 12:00 to 15:00 and 5 MB from 06:00 to 12:00.
        # If the cloud server is connected to the internal network, do not limit the backup network bandwidth. To remove the bandwidth limit, set this parameter to an empty string ("").
        # 
        # This parameter is required.
        self.policy_shrink = policy_shrink
        # The region where the server to which the policy applies resides.
        # 
        # You can call the [DescribeSupportRegion](~~DescribeSupportRegion~~) operation to query the regions supported by the anti-ransomware feature.
        self.policy_region_id = policy_region_id
        # The version of the policy. You can call the [DescribeBackupPolicies](~~DescribeBackupPolicies~~) operation to query the version.
        # 
        # - **1.0.0**
        # - **2.0.0**
        self.policy_version = policy_version
        # The method to cover assets. Valid values:
        # - **ALL_MACHINE**: all assets
        # > To cover all assets of this type, set this parameter to **ALL_MACHINE**. In this case, **UuidList** does not take effect. Only one policy that covers all assets can exist for the same server type.
        self.select_type = select_type
        # The server type. Valid values:
        # - **ALIYUN**: Alibaba Cloud server
        # - **OUT_CLOUD**: third-party server
        # - **TRIPARTITE**: simple application server
        self.server_type = server_type
        # The list of UUIDs of the servers protected by the policy.
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

        if self.select_type is not None:
            result['SelectType'] = self.select_type

        if self.server_type is not None:
            result['ServerType'] = self.server_type

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

        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

