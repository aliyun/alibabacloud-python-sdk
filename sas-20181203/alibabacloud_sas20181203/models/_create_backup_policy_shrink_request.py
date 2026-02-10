# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateBackupPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        policy_shrink: str = None,
        policy_region_id: str = None,
        policy_version: str = None,
        uuid_list: List[str] = None,
    ):
        # The name of the anti-ransomware policy.
        # 
        # This parameter is required.
        self.name = name
        # *   **IsDefault**: the type of the anti-ransomware policy. Valid values:
        # 
        #     *   **1**: recommended policy
        #     *   **0**: custom policy
        # 
        # *   **Include**: the format of the files that you want to protect. If you want to protect the files in all formats, set this field to [].
        # 
        # *   **Source**: the directory that you want to protect. If you want to protect all directories, set this field to [].
        # 
        # *   **ExcludeSystemPath**: specifies whether to exclude a specific directory from the anti-ransomware policy. If you want to exclude a directory, set this field to **true**. If you do not want to exclude a directory, leave this field empty.
        # 
        # *   **Exclude**: the directory that you want to exclude from the anti-ransomware policy. If you do not want to exclude a directory, set this field to [].
        # 
        # *   **Schedule**: the start time and interval of a data backup task. We recommend that you specify a start time that begins during off-peak hours but does not start on the hour. Examples:
        # 
        #     *   If you set this field to I|1583216092|P21D, the data backup task starts from 2020-03-03 14:14:52, and the task is run at an interval of three weeks.
        #     *   If you set this field to I|1583216092|PT24H, the data backup task starts from 2020-03-03 14:14:52, and the task is run at an interval of 24 hours.
        # 
        # *   **Retention**: the period during which backup data is retained. Unit: days. If you set this field to 7, backup data is retained for a week. If you set this field to 365, backup data is retained for a year. If you set this field to -1, backup data is permanently retained.
        # 
        # *   **SpeedLimiter**: the limit on the network bandwidth for data backup tasks. If you set this field to 0:24:30720, the maximum bandwidth for a data backup task is 30 MB/s from 00:00 to 24:00.
        # 
        # *   **UseVss**: specifies whether to enable the VSS feature. The feature is available only for Windows servers. Valid values:
        # 
        #     *   **true**: yes
        #     *   **false**: no
        # 
        # >  The VSS feature is available only if you create the anti-ransomware policy for Windows servers. After you enable the feature, the number of backup failures due to running processes is significantly reduced. We recommend that you enable the VSS feature. After you enable the feature, the data of disks that are in the exFAT and FAT32 formats cannot be backed up.
        # 
        # This parameter is required.
        self.policy_shrink = policy_shrink
        # The region ID of the server that is not deployed on Alibaba Cloud.
        # 
        # >  We recommend that you specify the ID of the supported region that is the nearest to the location of the server. You can call the [DescribeSupportRegion](~~DescribeSupportRegion~~) operation to query the supported regions of the anti-ransomware feature.
        self.policy_region_id = policy_region_id
        # The version of the anti-ransomware policy. Set the value to **2.0.0**.
        # 
        # This parameter is required.
        self.policy_version = policy_version
        # The UUIDs of the servers that you want to protect.
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

