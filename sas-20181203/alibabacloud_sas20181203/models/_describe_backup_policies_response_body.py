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
        # The details of the mitigation policies.
        self.policies = policies
        # The ID of the request. The ID is a unique identifier that Alibaba Cloud generates for the request and can be used to troubleshoot issues.
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
        select_type: str = None,
        server_type: str = None,
        service_error_count: int = None,
        service_error_uuid_list: List[str] = None,
        status: str = None,
        upgrade_status: str = None,
        uuid_list: List[str] = None,
    ):
        # The number of errors reported by the anti-ransomware client.
        self.client_error_count = client_error_count
        # The list of UUIDs of clients in the **abnormal** state.
        self.client_error_uuid_list = client_error_uuid_list
        # The status of the anti-ransomware client. Valid values:
        # 
        # - **running**: Normal.
        # 
        # - **exception**: Abnormal.
        self.client_status = client_status
        # The number of clients in the Normal state.
        self.health_client_count = health_client_count
        # The list of UUIDs of clients in the **healthy** state.
        self.health_client_uuid_list = health_client_uuid_list
        # The ID of the anti-ransomware mitigation policy.
        self.id = id
        # The most recent time when the anti-ransomware mitigation policy status was updated, in milliseconds.
        self.last_status_sync_time = last_status_sync_time
        # The name of the anti-ransomware mitigation policy.
        self.name = name
        # The content of the anti-ransomware mitigation policy. This parameter is in JSON format. The following fields are included:
        # 
        # - **IsDefault**: The type of the mitigation policy. Valid values:
        #     - **1**: recommended policy
        #     - **0**: custom policy
        # - **Include**: The file types to protect. If all file types are protected, this parameter is set to [].
        # - **Source**: The server folders to protect. If all folders need to be protected, this parameter is set to [].
        # - **ExcludeSystemPath**: Specifies whether to exclude specified folders. To exclude folders, set this parameter to **true**. If you do not want to exclude folders, you do not need to set this parameter.
        # - **Exclude**: The specified protection folder addresses. If no specific protection folder address is set, this parameter is set to [].
        # - **Schedule**: The execution time and interval of the data backup node. Specify a non-peak hour that is not on the hour. Examples:
        #     - Example 1: I|1583216092|P21D indicates that data backup starts at 2020-03-03 14:14:52, and the backup policy executes at an interval of 3 weeks.
        #     - Example 2: I|1583216092|PT24H indicates that data backup starts at 2020-03-03 14:14:52, and the backup policy executes at an interval of 24 hours.
        # - **Retention**: The retention period of backup data, in days. 7 indicates 1 week, 365 indicates 1 year, and -1 indicates permanent retention.
        # - **SpeedLimiter**: The backup network bandwidth throttling. For example, 0:24:30720 indicates that the backup network bandwidth throttling is 30 MB/s from 00:00 to 24:00.
        # - **UseVss**: Specifies whether to enable the VSS (Windows) feature. Valid values:
        #     - **true**: enabled
        #     - **false**: not enabled
        # 
        # > The VSS (Windows) feature is available only for Windows systems. After this feature is enabled, it effectively reduces the issue of individual file backup failures caused by process occupation. Enable this feature. After this feature is enabled, file backup for exFAT and FAT32 disk formats is not supported.
        self.policy = policy
        # The region ID of the backup service selected when the anti-ransomware client is installed on a non-Alibaba Cloud server.
        self.policy_region_id = policy_region_id
        # The version of the mitigation policy. Valid values:
        # 
        # - 1.0.0.
        # - 2.0.0.
        self.policy_version = policy_version
        # The previous status of the anti-ransomware mitigation policy.
        # 
        # - **enabled**: The policy was manually enabled.
        # 
        # - **disabled**: The policy was manually disabled. After the policy is disabled, running backup nodes are stopped.
        # 
        # - **closed**: The anti-ransomware capacity was exceeded, and the system disabled the policy.
        self.pre_status = pre_status
        # The list of UUIDs of servers returned after the search by the MachineRemark request parameter.
        self.remarked_uuid_list = remarked_uuid_list
        # The method used to select covered assets. Valid values:
        # 
        # - **ALL_MACHINE**: All assets.
        # 
        # > If the policy covers **all assets**, this property value is **ALL_MACHINE**.
        self.select_type = select_type
        # The server type. Valid values:
        # 
        # - **OUT_CLOUD**: Non-Alibaba Cloud server.
        # - **ALIYUN**: Alibaba Cloud server.
        # - **TRIPARTITE**: Lightweight application server.
        self.server_type = server_type
        # The number of servers with data backup exceptions.
        self.service_error_count = service_error_count
        # The list of UUIDs of servers with data backup exceptions.
        self.service_error_uuid_list = service_error_uuid_list
        # The status of the anti-ransomware mitigation policy.
        # 
        # - **enabled**: The policy is manually enabled.
        # 
        # - **disabled**: The policy is manually disabled. After the policy is disabled, running backup nodes are stopped.
        # 
        # - **closed**: The anti-ransomware capacity is exceeded, and the system disables the policy.
        self.status = status
        # The upgrade status of the policy. Valid values:
        # 
        # - **NotUpgraded**: Not upgraded.
        # - **Upgrading**: Upgrading.
        # - **UpgradeFailed**: Upgrade failed.
        # - **UpgradeSuccess**: Upgrade succeeded.
        self.upgrade_status = upgrade_status
        # The list of UUIDs of servers protected by the anti-ransomware mitigation policy.
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

        if self.select_type is not None:
            result['SelectType'] = self.select_type

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

        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')

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
        # The number of entries on the current page in a paged query.
        self.count = count
        # The page number of the current page in the returned data.
        self.current_page = current_page
        # The number of backup policies per page in a paged query. Default value: 10, which indicates that each page contains 10 backup policies.
        self.page_size = page_size
        # The total number of backup policies in the returned data.
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

