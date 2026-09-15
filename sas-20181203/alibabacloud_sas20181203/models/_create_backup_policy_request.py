# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class CreateBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        policy: Dict[str, Any] = None,
        policy_region_id: str = None,
        policy_version: str = None,
        select_type: str = None,
        server_type: str = None,
        uuid_list: List[str] = None,
    ):
        # The name of the protection policy to create. Set this parameter to the desired policy name.
        # 
        # This parameter is required.
        self.name = name
        # - **IsDefault**: The type of the protection policy to create. Valid values:
        #     - **1**: Recommended policy.
        #     - **0**: Custom policy.
        # - **Include**: The file types to protect. To protect all file types, set this parameter to [].
        # - **Source**: The server folders to protect. To protect all folders, set this parameter to [].
        # - **ExcludeSystemPath**: Specifies whether to exclude specified folders. Set this parameter to **true** to exclude folders. If you do not want to exclude folders, you do not need to set this parameter.
        # - **Exclude**: The specified protection folder addresses. If you do not want to specify protection folder addresses, set this parameter to [].
        # - **Schedule**: The time and interval at which the data backup task is scheduled to run. Specify a non-peak hour that is not on the hour. Examples:
        #     - Example 1: I|1583216092|P21D indicates that the data backup starts at 2020-03-03 14:14:52 and the backup policy runs at an interval of 3 weeks.
        #     - Example 2: I|1583216092|PT24H indicates that the data backup starts at 2020-03-03 14:14:52 and the backup policy runs at an interval of 24 hours.
        # - **Retention**: The retention period of backup data, in days. The value 7 indicates 1 week, 365 indicates 1 year, and -1 indicates permanent retention.
        # - **SpeedLimiter**: The network bandwidth throttling for backup. For example, 0:24:30720 indicates that the network bandwidth throttling for backup is 30 MB/s from 00:00 to 24:00.
        # - **UseVss**: Specifies whether to enable the Volume Shadow Copy Service (VSS) feature for Windows. Valid values:
        #     - **true**: Enabled.
        #     - **false**: Not enabled.
        # 
        # > The VSS (Windows) feature applies only to Windows systems. After this feature is enabled, the issue of individual file backup failures due to process occupation is effectively reduced. We recommend that you enable this feature. After this feature is enabled, file backup for exFAT and FAT32 disk formats is not supported.
        # 
        # This parameter is required.
        self.policy = policy
        # The region ID of the non-Alibaba Cloud server.
        # 
        # > Call the [DescribeSupportRegion](~~DescribeSupportRegion~~) operation to query the regions supported by the anti-ransomware feature, and then select the supported region closest to the region where your non-Alibaba Cloud server resides.
        self.policy_region_id = policy_region_id
        # The version of the protection policy. Set the value to **2.0.0**.
        # 
        # This parameter is required.
        self.policy_version = policy_version
        # The method used to cover assets. Valid values:
        # - **ALL_MACHINE**: All assets.
        # > To cover all assets of this type, set this parameter to **ALL_MACHINE**. In this case, **UuidList** is invalid. Only one policy that covers all assets can exist for each server type.
        self.select_type = select_type
        # The server type. Valid values:
        # - **ALIYUN**: Alibaba Cloud server.
        # - **OUT_CLOUD**: Non-Alibaba Cloud server.
        # - **TRIPARTITE**: Simple application server.
        self.server_type = server_type
        # The UUIDs of the servers to protect.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.policy is not None:
            result['Policy'] = self.policy

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
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

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

