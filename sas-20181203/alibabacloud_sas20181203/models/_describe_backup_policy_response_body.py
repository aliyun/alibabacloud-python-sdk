# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        backup_policy_detail: main_models.DescribeBackupPolicyResponseBodyBackupPolicyDetail = None,
        request_id: str = None,
    ):
        # The details of the anti-ransomware policy.
        self.backup_policy_detail = backup_policy_detail
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.backup_policy_detail:
            self.backup_policy_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_policy_detail is not None:
            result['BackupPolicyDetail'] = self.backup_policy_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPolicyDetail') is not None:
            temp_model = main_models.DescribeBackupPolicyResponseBodyBackupPolicyDetail()
            self.backup_policy_detail = temp_model.from_map(m.get('BackupPolicyDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackupPolicyResponseBodyBackupPolicyDetail(DaraModel):
    def __init__(
        self,
        client_status: str = None,
        id: int = None,
        name: str = None,
        policy: str = None,
        policy_version: str = None,
        region_id: str = None,
        status: str = None,
        uuid_list: List[str] = None,
    ):
        # The status of the anti-ransomware agent. Valid values:
        # 
        # *   **running**: normal
        # *   **exception**: abnormal
        self.client_status = client_status
        # The ID of the anti-ransomware policy.
        self.id = id
        # The name of the anti-ransomware policy.
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
        self.policy = policy
        # The version of the anti-ransomware policy.
        # 
        # *   **1.0.0**
        # *   **2.0.0**
        self.policy_version = policy_version
        # The ID of the region in which backup data is stored.
        self.region_id = region_id
        # The status of the anti-ransomware policy. Valid values:
        # 
        # *   **enabled**: The anti-ransomware policy is manually enabled.
        # *   **disabled**: The anti-ransomware policy is manually disabled. After an anti-ransomware policy is disabled, the data backup task that is running based on the policy stops.
        # *   **closed**: The anti-ransomware policy automatically stops because the anti-ransomware capacity is insufficient.
        self.status = status
        # An array consisting of the UUIDs of the servers to which the anti-ransomware policy is applied.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_status is not None:
            result['ClientStatus'] = self.client_status

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientStatus') is not None:
            self.client_status = m.get('ClientStatus')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

