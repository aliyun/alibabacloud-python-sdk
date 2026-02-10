# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeBackupPoliciesResponseBodyPageInfo = None,
        policies: List[main_models.DescribeBackupPoliciesResponseBodyPolicies] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The details of the anti-ransomware policy.
        self.policies = policies
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeBackupPoliciesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.DescribeBackupPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackupPoliciesResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        client_error_count: int = None,
        client_error_uuid_list: List[str] = None,
        client_status: str = None,
        health_client_count: int = None,
        health_client_uuid_list: List[str] = None,
        id: int = None,
        last_status_sync_time: int = None,
        name: str = None,
        policy: str = None,
        policy_region_id: str = None,
        policy_version: str = None,
        pre_status: str = None,
        remarked_uuid_list: List[str] = None,
        server_type: str = None,
        service_error_count: int = None,
        service_error_uuid_list: List[str] = None,
        status: str = None,
        upgrade_status: str = None,
        uuid_list: List[str] = None,
    ):
        # The number of the servers on which the anti-ransomware agent is in an abnormal state.
        self.client_error_count = client_error_count
        # The UUIDs of the servers on which the anti-ransomware agent is in an **abnormal** state.
        self.client_error_uuid_list = client_error_uuid_list
        # The status of the anti-ransomware agent. Valid values:
        # 
        # *   **running**: normal
        # *   **exception**: abnormal
        self.client_status = client_status
        # The number of the servers on which the anti-ransomware agent is in a normal state.
        self.health_client_count = health_client_count
        # The UUIDs of the servers on which the anti-ransomware agent is in a **normal** state.
        self.health_client_uuid_list = health_client_uuid_list
        # The ID of the anti-ransomware policy.
        self.id = id
        # The time when the anti-ransomware policy was last updated. Unit: milliseconds.
        self.last_status_sync_time = last_status_sync_time
        # The name of the anti-ransomware policy.
        self.name = name
        # The configurations of the anti-ransomware policy. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **IsDefault**: the type of the anti-ransomware policy. Valid values:
        # 
        #     *   **1**: recommended policy
        #     *   **0**: custom policy
        # 
        # *   **Include**: the format of the files that are protected. If the value of this field is [], all formats of files are protected.
        # 
        # *   **Source**: the directory that is protected. If the value of this field is [], all directories are protected.
        # 
        # *   **ExcludeSystemPath**: indicates whether a specified directory is excluded from the anti-ransomware policy. If the value of this field is **true**, a directory is excluded. If this field is left empty, no directories are excluded.
        # 
        # *   **Exclude**: the directory that is excluded from the anti-ransomware policy. If the value of this field is [], no directories are excluded.
        # 
        # *   **Schedule**: the start time and interval of a data backup task. We recommend that you specify a start time that begins during off-peak hours but does not start on the hour. Examples:
        # 
        #     *   If the value of this field is I|1583216092|P21D, the data backup task starts from 2020-03-03 14:14:52, and the task is run at an interval of three weeks.
        #     *   If the value of this field is I|1583216092|PT24H, the data backup task starts from 2020-03-03 14:14:52, and the task is run at an interval of 24 hours.
        # 
        # *   **Retention**: the period during which backup data is retained. Unit: days. If the value of this field is 7, backup data is retained for a week. If the value of this field is 365, backup data is retained for a year. If the value of this field is -1, backup data is permanently retained.
        # 
        # *   **SpeedLimiter**: the limit on the network bandwidth for data backup tasks. If the value of this field is 0:24:30720, the maximum bandwidth for a data backup task is 30 MB/s from 00:00 to 24:00.
        # 
        # *   **UseVss**: indicates whether the VSS feature is enabled. The feature is available only for Windows servers. Valid values:
        # 
        #     *   **true**
        #     *   **false**
        # 
        # >  The VSS feature is available only if you create the anti-ransomware policy for Windows servers. After you enable the feature, the number of backup failures due to running processes is significantly reduced. We recommend that you enable the VSS feature. After you enable the feature, the data of disks that are in the exFAT and FAT32 formats cannot be backed up.
        self.policy = policy
        # The ID of the region that you specified for data backup when you installed the anti-ransomware agent for the server not deployed on Alibaba Cloud.
        self.policy_region_id = policy_region_id
        # The version of the anti-ransomware policy. Valid values:
        # 
        # *   1.0.0
        # *   2.0.0
        self.policy_version = policy_version
        # The previous status of the anti-ransomware policy. Valid values:
        # 
        # *   **enabled**: The anti-ransomware policy is manually enabled.
        # *   **disabled**: The anti-ransomware policy is manually disabled. After an anti-ransomware policy is disabled, the data backup task that is running based on the policy stops.
        # *   **closed**: The anti-ransomware policy automatically stops because the anti-ransomware capacity is insufficient.
        self.pre_status = pre_status
        # The UUIDs that are returned based on the value of the MachineRemark request parameter.
        self.remarked_uuid_list = remarked_uuid_list
        # The type of the server. Valid values:
        # 
        # *   **OUT_CLOUD**: server not deployed on Alibaba Cloud
        # *   **ALIYUN**: Elastic Compute Service (ECS) instance
        # *   **TRIPARTITE**: simple application server
        self.server_type = server_type
        # The number of servers on which data backup is exceptional.
        self.service_error_count = service_error_count
        # The UUIDs of the servers on which data backup is exceptional.
        self.service_error_uuid_list = service_error_uuid_list
        # The status of the anti-ransomware policy. Valid values:
        # 
        # *   **enabled**: The anti-ransomware policy is manually enabled.
        # *   **disabled**: The anti-ransomware policy is manually disabled. After an anti-ransomware policy is disabled, the data backup task that is running based on the policy stops.
        # *   **closed**: The anti-ransomware policy automatically stops because the anti-ransomware capacity is insufficient.
        self.status = status
        # The upgrade status of the anti-ransomware policy. Valid values:
        # 
        # *   **NotUpgraded**
        # *   **Upgrading**
        # *   **UpgradeFailed**
        # *   **UpgradeSuccess**
        self.upgrade_status = upgrade_status
        # The UUIDs of the servers to which the anti-ransomware policy is applied.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_error_count is not None:
            result['ClientErrorCount'] = self.client_error_count

        if self.client_error_uuid_list is not None:
            result['ClientErrorUuidList'] = self.client_error_uuid_list

        if self.client_status is not None:
            result['ClientStatus'] = self.client_status

        if self.health_client_count is not None:
            result['HealthClientCount'] = self.health_client_count

        if self.health_client_uuid_list is not None:
            result['HealthClientUuidList'] = self.health_client_uuid_list

        if self.id is not None:
            result['Id'] = self.id

        if self.last_status_sync_time is not None:
            result['LastStatusSyncTime'] = self.last_status_sync_time

        if self.name is not None:
            result['Name'] = self.name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.policy_region_id is not None:
            result['PolicyRegionId'] = self.policy_region_id

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        if self.pre_status is not None:
            result['PreStatus'] = self.pre_status

        if self.remarked_uuid_list is not None:
            result['RemarkedUuidList'] = self.remarked_uuid_list

        if self.server_type is not None:
            result['ServerType'] = self.server_type

        if self.service_error_count is not None:
            result['ServiceErrorCount'] = self.service_error_count

        if self.service_error_uuid_list is not None:
            result['ServiceErrorUuidList'] = self.service_error_uuid_list

        if self.status is not None:
            result['Status'] = self.status

        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientErrorCount') is not None:
            self.client_error_count = m.get('ClientErrorCount')

        if m.get('ClientErrorUuidList') is not None:
            self.client_error_uuid_list = m.get('ClientErrorUuidList')

        if m.get('ClientStatus') is not None:
            self.client_status = m.get('ClientStatus')

        if m.get('HealthClientCount') is not None:
            self.health_client_count = m.get('HealthClientCount')

        if m.get('HealthClientUuidList') is not None:
            self.health_client_uuid_list = m.get('HealthClientUuidList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastStatusSyncTime') is not None:
            self.last_status_sync_time = m.get('LastStatusSyncTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PolicyRegionId') is not None:
            self.policy_region_id = m.get('PolicyRegionId')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        if m.get('PreStatus') is not None:
            self.pre_status = m.get('PreStatus')

        if m.get('RemarkedUuidList') is not None:
            self.remarked_uuid_list = m.get('RemarkedUuidList')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        if m.get('ServiceErrorCount') is not None:
            self.service_error_count = m.get('ServiceErrorCount')

        if m.get('ServiceErrorUuidList') is not None:
            self.service_error_uuid_list = m.get('ServiceErrorUuidList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

class DescribeBackupPoliciesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: 10.
        self.page_size = page_size
        # The total number of anti-ransomware policies returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

