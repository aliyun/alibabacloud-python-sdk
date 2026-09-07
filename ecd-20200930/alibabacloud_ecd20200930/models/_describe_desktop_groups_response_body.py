# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDesktopGroupsResponseBody(DaraModel):
    def __init__(
        self,
        desktop_groups: List[main_models.DescribeDesktopGroupsResponseBodyDesktopGroups] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of shared cloud computers.
        self.desktop_groups = desktop_groups
        # The token for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.desktop_groups:
            for v1 in self.desktop_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DesktopGroups'] = []
        if self.desktop_groups is not None:
            for k1 in self.desktop_groups:
                result['DesktopGroups'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktop_groups = []
        if m.get('DesktopGroups') is not None:
            for k1 in m.get('DesktopGroups'):
                temp_model = main_models.DescribeDesktopGroupsResponseBodyDesktopGroups()
                self.desktop_groups.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDesktopGroupsResponseBodyDesktopGroups(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        bind_amount: int = None,
        buy_desktops_count: int = None,
        comments: str = None,
        connect_duration: int = None,
        count_per_status: List[main_models.DescribeDesktopGroupsResponseBodyDesktopGroupsCountPerStatus] = None,
        cpu: int = None,
        create_time: str = None,
        creator: str = None,
        data_disk_category: str = None,
        data_disk_size: str = None,
        desktop_count: int = None,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
        desktop_type: str = None,
        end_user_count: int = None,
        entra_domain_name: str = None,
        env_id: str = None,
        env_type: str = None,
        expired_time: str = None,
        expired_times: List[str] = None,
        gpu_count: float = None,
        gpu_driver_version: str = None,
        gpu_spec: str = None,
        idle_disconnect_duration: int = None,
        image_id: str = None,
        is_ldap: bool = None,
        keep_duration: int = None,
        load_policy: int = None,
        max_desktops_count: int = None,
        memory: int = None,
        min_desktops_count: int = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_type: str = None,
        org_id: str = None,
        os_type: str = None,
        own_bundle_id: str = None,
        own_bundle_name: str = None,
        own_type: int = None,
        pay_type: str = None,
        policy_group_id: str = None,
        policy_group_id_list: List[str] = None,
        policy_group_name: str = None,
        policy_group_name_list: List[str] = None,
        protocol_type: str = None,
        qos_rule_id: str = None,
        ratio_threshold: float = None,
        reset_type: int = None,
        simple_user_group_id: str = None,
        status: int = None,
        stop_duration: int = None,
        subnet_id: str = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
        tags: List[main_models.DescribeDesktopGroupsResponseBodyDesktopGroupsTags] = None,
        user_group_name: str = None,
        user_ou_path: str = None,
        version: int = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
    ):
        # The account type.
        self.account_type = account_type
        # The number of concurrent sessions allowed per cloud computer in a multi-session shared cloud computer group with multiple instances.
        self.bind_amount = bind_amount
        # This parameter applies only to subscription shared cloud computers and indicates the initial number of cloud computers purchased. Valid values: 0 to 200.
        self.buy_desktops_count = buy_desktops_count
        # The remarks.
        self.comments = comments
        # The maximum duration that a session can remain in the connected state. The session is automatically disconnected when this duration is reached. Unit: milliseconds.
        self.connect_duration = connect_duration
        # The list of cloud computer counts by status.
        self.count_per_status = count_per_status
        # The number of vCPUs.
        self.cpu = cpu
        # The creation time.
        # 
        # The time is displayed in UTC in the ISO 8601 standard format: yyyy-MM-ddTHH:mm:ssZ.
        self.create_time = create_time
        # The Alibaba Cloud account ID of the creator.
        self.creator = creator
        # The user disk type.
        self.data_disk_category = data_disk_category
        # The user disk capacity. Unit: GiB.
        self.data_disk_size = data_disk_size
        # The number of cloud computers that have been created.
        self.desktop_count = desktop_count
        # The ID of the shared cloud computer.
        self.desktop_group_id = desktop_group_id
        # The name of the shared cloud computer.
        self.desktop_group_name = desktop_group_name
        # The cloud computer specification. You can call [DescribeDesktopTypes](https://help.aliyun.com/document_detail/188882.html) to query the specification IDs supported by Wuying Cloud Computer.
        self.desktop_type = desktop_type
        # The number of authorized users for the shared cloud computer.
        self.end_user_count = end_user_count
        # The domain name of Microsoft Entra ID.
        self.entra_domain_name = entra_domain_name
        # The environment ID. This parameter is not publicly available.
        self.env_id = env_id
        # The environment type. This parameter is not publicly available.
        self.env_type = env_type
        # The expiration time of the subscription shared cloud computer.
        # 
        # The time follows the ISO 8601 standard in UTC: yyyy-MM-ddTHH:mm:ssZ.
        self.expired_time = expired_time
        # The list of expiration times.
        self.expired_times = expired_times
        # The number of GPU cores.
        self.gpu_count = gpu_count
        # The GPU driver version.
        self.gpu_driver_version = gpu_driver_version
        # The GPU memory.
        self.gpu_spec = gpu_spec
        # The maximum idle duration after a user session is established. If no keyboard or mouse operations are performed within this duration, the session is disconnected. Unit: milliseconds.
        self.idle_disconnect_duration = idle_disconnect_duration
        # The image ID.
        self.image_id = image_id
        # Indicates whether the directory is an LDAP directory.
        self.is_ldap = is_ldap
        # The retention period after a session is disconnected. Unit: milliseconds. Valid values: 180000 (3 minutes) to 345600000 (4 days). A value of 0 indicates that the session is always retained.
        self.keep_duration = keep_duration
        # The load balancing policy for multi-session shared cloud computers with multiple instances.
        self.load_policy = load_policy
        # - For pay-as-you-go shared cloud computers, this parameter indicates the maximum number of cloud computers that can be created.
        self.max_desktops_count = max_desktops_count
        # The memory size. Unit: MiB.
        self.memory = memory
        # - For pay-as-you-go shared cloud computers, this parameter indicates the minimum number of cloud computers that can be created.
        self.min_desktops_count = min_desktops_count
        # The name of the office network to which the shared cloud computer belongs.
        self.office_site_id = office_site_id
        # The ID of the office network to which the shared cloud computers belong.
        self.office_site_name = office_site_name
        # The account system type of the office network.
        self.office_site_type = office_site_type
        # The organization ID of the team.
        self.org_id = org_id
        # The operating system type.
        self.os_type = os_type
        # The cloud computer template ID.
        self.own_bundle_id = own_bundle_id
        # The name of the cloud computer template.
        self.own_bundle_name = own_bundle_name
        # The type of the shared cloud computer.
        self.own_type = own_type
        # The billing method.
        self.pay_type = pay_type
        # The ID of the policy associated with the shared cloud computer.
        self.policy_group_id = policy_group_id
        # The list of cloud computer policy IDs.
        self.policy_group_id_list = policy_group_id_list
        # The policy name associated with the shared cloud computer.
        self.policy_group_name = policy_group_name
        # The list of cloud computer policy names.
        self.policy_group_name_list = policy_group_name_list
        # The protocol type.
        self.protocol_type = protocol_type
        # The ID of the QoS rule.
        self.qos_rule_id = qos_rule_id
        # The session occupancy threshold used as the auto scaling trigger condition for multi-session shared cloud computers. The session occupancy is calculated by using the following formula:
        # 
        # ```Session occupancy = Number of bound sessions / (Total number of cloud computers × Maximum number of sessions supported by each cloud computer) × 100%```
        # 
        # When the session occupancy reaches this threshold, new cloud computers are created. When the session occupancy is below this threshold, excess cloud computers are deleted.
        self.ratio_threshold = ratio_threshold
        # The reset type of the shared cloud computer.
        self.reset_type = reset_type
        # The convenience user group ID.
        self.simple_user_group_id = simple_user_group_id
        # The status of the shared cloud computer.
        self.status = status
        # The idle shutdown duration. When the cloud computer has been idle for this duration, it is automatically shut down. If a user connects after shutdown, the cloud computer automatically starts. Unit: milliseconds.
        self.stop_duration = stop_duration
        # The subnet ID.
        self.subnet_id = subnet_id
        # The system cloud disk type.
        self.system_disk_category = system_disk_category
        # The system cloud disk capacity. Unit: GiB.
        self.system_disk_size = system_disk_size
        # The list of tags.
        self.tags = tags
        # The user group name.
        self.user_group_name = user_group_name
        # The organizational unit (OU) path of the user.
        self.user_ou_path = user_ou_path
        # The version number of the shared cloud computer.
        self.version = version
        # Indicates whether encryption is enabled.
        self.volume_encryption_enabled = volume_encryption_enabled
        # The ID of the KMS key used for disk encryption.
        self.volume_encryption_key = volume_encryption_key

    def validate(self):
        if self.count_per_status:
            for v1 in self.count_per_status:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.bind_amount is not None:
            result['BindAmount'] = self.bind_amount

        if self.buy_desktops_count is not None:
            result['BuyDesktopsCount'] = self.buy_desktops_count

        if self.comments is not None:
            result['Comments'] = self.comments

        if self.connect_duration is not None:
            result['ConnectDuration'] = self.connect_duration

        result['CountPerStatus'] = []
        if self.count_per_status is not None:
            for k1 in self.count_per_status:
                result['CountPerStatus'].append(k1.to_map() if k1 else None)

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.desktop_count is not None:
            result['DesktopCount'] = self.desktop_count

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.end_user_count is not None:
            result['EndUserCount'] = self.end_user_count

        if self.entra_domain_name is not None:
            result['EntraDomainName'] = self.entra_domain_name

        if self.env_id is not None:
            result['EnvId'] = self.env_id

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.expired_times is not None:
            result['ExpiredTimes'] = self.expired_times

        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count

        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version

        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec

        if self.idle_disconnect_duration is not None:
            result['IdleDisconnectDuration'] = self.idle_disconnect_duration

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.is_ldap is not None:
            result['IsLdap'] = self.is_ldap

        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration

        if self.load_policy is not None:
            result['LoadPolicy'] = self.load_policy

        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.own_bundle_id is not None:
            result['OwnBundleId'] = self.own_bundle_id

        if self.own_bundle_name is not None:
            result['OwnBundleName'] = self.own_bundle_name

        if self.own_type is not None:
            result['OwnType'] = self.own_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.policy_group_id_list is not None:
            result['PolicyGroupIdList'] = self.policy_group_id_list

        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name

        if self.policy_group_name_list is not None:
            result['PolicyGroupNameList'] = self.policy_group_name_list

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.qos_rule_id is not None:
            result['QosRuleId'] = self.qos_rule_id

        if self.ratio_threshold is not None:
            result['RatioThreshold'] = self.ratio_threshold

        if self.reset_type is not None:
            result['ResetType'] = self.reset_type

        if self.simple_user_group_id is not None:
            result['SimpleUserGroupId'] = self.simple_user_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.stop_duration is not None:
            result['StopDuration'] = self.stop_duration

        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        if self.user_ou_path is not None:
            result['UserOuPath'] = self.user_ou_path

        if self.version is not None:
            result['Version'] = self.version

        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled

        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('BindAmount') is not None:
            self.bind_amount = m.get('BindAmount')

        if m.get('BuyDesktopsCount') is not None:
            self.buy_desktops_count = m.get('BuyDesktopsCount')

        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('ConnectDuration') is not None:
            self.connect_duration = m.get('ConnectDuration')

        self.count_per_status = []
        if m.get('CountPerStatus') is not None:
            for k1 in m.get('CountPerStatus'):
                temp_model = main_models.DescribeDesktopGroupsResponseBodyDesktopGroupsCountPerStatus()
                self.count_per_status.append(temp_model.from_map(k1))

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('DesktopCount') is not None:
            self.desktop_count = m.get('DesktopCount')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('EndUserCount') is not None:
            self.end_user_count = m.get('EndUserCount')

        if m.get('EntraDomainName') is not None:
            self.entra_domain_name = m.get('EntraDomainName')

        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('ExpiredTimes') is not None:
            self.expired_times = m.get('ExpiredTimes')

        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')

        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')

        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')

        if m.get('IdleDisconnectDuration') is not None:
            self.idle_disconnect_duration = m.get('IdleDisconnectDuration')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('IsLdap') is not None:
            self.is_ldap = m.get('IsLdap')

        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')

        if m.get('LoadPolicy') is not None:
            self.load_policy = m.get('LoadPolicy')

        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OwnBundleId') is not None:
            self.own_bundle_id = m.get('OwnBundleId')

        if m.get('OwnBundleName') is not None:
            self.own_bundle_name = m.get('OwnBundleName')

        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PolicyGroupIdList') is not None:
            self.policy_group_id_list = m.get('PolicyGroupIdList')

        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')

        if m.get('PolicyGroupNameList') is not None:
            self.policy_group_name_list = m.get('PolicyGroupNameList')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('QosRuleId') is not None:
            self.qos_rule_id = m.get('QosRuleId')

        if m.get('RatioThreshold') is not None:
            self.ratio_threshold = m.get('RatioThreshold')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        if m.get('SimpleUserGroupId') is not None:
            self.simple_user_group_id = m.get('SimpleUserGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StopDuration') is not None:
            self.stop_duration = m.get('StopDuration')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeDesktopGroupsResponseBodyDesktopGroupsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        if m.get('UserOuPath') is not None:
            self.user_ou_path = m.get('UserOuPath')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')

        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')

        return self

class DescribeDesktopGroupsResponseBodyDesktopGroupsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeDesktopGroupsResponseBodyDesktopGroupsCountPerStatus(DaraModel):
    def __init__(
        self,
        count: int = None,
        status: str = None,
    ):
        # The number of cloud computers.
        self.count = count
        # The cloud computer status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

