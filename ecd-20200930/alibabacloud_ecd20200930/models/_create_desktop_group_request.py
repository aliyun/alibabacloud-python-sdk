# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class CreateDesktopGroupRequest(DaraModel):
    def __init__(
        self,
        all_classify_users: bool = None,
        allow_auto_setup: int = None,
        allow_buffer_count: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        bind_amount: int = None,
        bundle_id: str = None,
        buy_desktops_count: int = None,
        charge_type: str = None,
        classify: str = None,
        client_token: str = None,
        comments: str = None,
        connect_duration: int = None,
        data_disk_category: str = None,
        data_disk_per_level: str = None,
        data_disk_size: int = None,
        default_init_desktop_count: int = None,
        default_language: str = None,
        delete_duration: int = None,
        desktop_group_name: str = None,
        desktop_type: str = None,
        directory_id: str = None,
        end_user_ids: List[str] = None,
        exclusive_type: str = None,
        file_system_id: str = None,
        group_amount: int = None,
        group_version: int = None,
        hostname: str = None,
        idle_disconnect_duration: int = None,
        image_id: str = None,
        keep_duration: int = None,
        load_policy: int = None,
        max_desktops_count: int = None,
        min_desktops_count: int = None,
        multi_resource: bool = None,
        office_site_id: str = None,
        own_type: int = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        profile_follow_switch: bool = None,
        promotion_id: str = None,
        ratio_threshold: float = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
        reset_type: int = None,
        scale_strategy_id: str = None,
        session_type: str = None,
        simple_user_group_id: str = None,
        snapshot_policy_id: str = None,
        stop_duration: int = None,
        system_disk_category: str = None,
        system_disk_per_level: str = None,
        system_disk_size: int = None,
        tag: List[main_models.CreateDesktopGroupRequestTag] = None,
        timer_group_id: str = None,
        user_group_name: str = None,
        user_ou_path: str = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
        vpc_id: str = None,
    ):
        # The types of the users.
        # 
        # >  This parameter is not publicly available.
        self.all_classify_users = all_classify_users
        # Specifies whether to enable batch-based automatic creation of subscription cloud computers for the shared group. This parameter is required if you set `ChargeType` to `PrePaid`.
        # 
        # Valid values:
        # 
        # *   0: enables batch-based automatic creation of subscription cloud computers.
        # *   1: disables batch-based automatic creation of subscription cloud computers.
        self.allow_auto_setup = allow_auto_setup
        # The maximum number of pay-as-you-go cloud computers that can be reserved in the shared group. This parameter is required if you set `ChargeType` to `PostPaid`. Valid values:
        # 
        # *   0: does not reserve any cloud computers.
        # *   N: reserves N cloud computers (1≤ N ≤ 100).
        # 
        # >  Setting this parameter to 0 means no cloud computers will be reserved in the shared group. In this case, the system must create, start, and assign cloud computers to end users upon request, which can be time-consuming. To improve user experience, we recommend that you reserve a specific number of cloud computers.
        self.allow_buffer_count = allow_buffer_count
        # Specifies whether to automatically complete the payment for subscription orders.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the shared subscription group.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.auto_renew = auto_renew
        # The number of concurrent sessions of the multi-session shared group.
        # 
        # >  This parameter is not publicly available.
        self.bind_amount = bind_amount
        # The ID of the cloud computer template.
        self.bundle_id = bundle_id
        # *   For shared subscription groups, this parameter defines the initial number of cloud computers to be created. Valid values: 0 to 200.
        # *   For shared pay-as-you-go groups, this parameter defines the minimum initial number of cloud computers to be created. Valid values: 0 to `MaxDesktopsCount`. Default value: 1.
        self.buy_desktops_count = buy_desktops_count
        # The billing method of the shared group.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go.
        # *   PrePaid: subscription.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The type of the cloud computers in the shared group.
        # 
        # >  This parameter is not publicly available.
        # 
        # Valid values:
        # 
        # *   teacher: cloud computers designed for teachers.
        # *   student: cloud computers designed for students.
        self.classify = classify
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The remarks of the shared group.
        self.comments = comments
        # The maximum duration for which each session remains connected. The session is automatically disconnected once the specified maximum time limit is reached. Unit: milliseconds. Valid values: 900000 to 345600000. That is, the session can be connected for 15 to 5,760 minutes (4 days).
        self.connect_duration = connect_duration
        # The category of the data disk.
        # 
        # Valid values:
        # 
        # *   cloud_auto: the standard SSD.
        # *   cloud_essd: the ESSD.
        self.data_disk_category = data_disk_category
        # The PL of the data disk of the ESSD category. Default value: PL0.
        # 
        # Valid values:
        # 
        # *   PL1
        # *   PL0
        self.data_disk_per_level = data_disk_per_level
        # The size of the data disk. Unit: GB. Valid values: 0 to 16380. The value must be an integral multiple of 20.
        # 
        # *   A value of 0 means no data disk is attached.
        # *   If the selected plan includes a standard SSD, the data disk size must be at least 20 GB.
        # 
        # Default value: 0.
        self.data_disk_size = data_disk_size
        # The default number of cloud computers that you want to create at the same time in the shared group. Default value: 1.
        self.default_init_desktop_count = default_init_desktop_count
        # The language of the OS.
        # 
        # Valid values:
        # 
        # *   en-US: English.
        # *   zh-HK: Traditional Chinese.
        # *   zh-CN: Simplified Chinese
        # *   ja-JP: Japanese.
        self.default_language = default_language
        self.delete_duration = delete_duration
        # The name of the shared group. The name can be up to 30 characters in length and can contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-). It must start with a letter but cannot start with `http://` or `https://`.
        self.desktop_group_name = desktop_group_name
        # The specifications of the cloud computer. You can call the [DescribeDesktopTypes](~~DescribeDesktopTypes~~) operation to query all the supported specifications.
        self.desktop_type = desktop_type
        # The ID of the directory.
        # 
        # >  This parameter is not publicly available.
        self.directory_id = directory_id
        # The IDs of the end users.
        self.end_user_ids = end_user_ids
        # Specifies whether the shared group is exclusive. You must set this parameter to `Exclusive` when `SessionType` is set to `MultipleSession`.
        self.exclusive_type = exclusive_type
        # The ID of the File Storage NAS (NAS) file system for the user data roaming feature.
        # 
        # >  This parameter is not publicly available.
        self.file_system_id = file_system_id
        # The number of shared groups for the single-cloud computer type. You must specify this parameter if you set `MultiResource` to `false`. Valid values: 1 to 5. Default value: 1.
        self.group_amount = group_amount
        # The version of the shared group.
        self.group_version = group_version
        # The hostname series of the cloud computer. This parameter is supported exclusively when the office network operates on Active Directory (AD) and the cloud computer runs on a Windows operating system.
        # 
        # Naming conventions:
        # 
        # *   A hostname must be 2 to 15 characters in length
        # *   and can contain only letters, digits, and hyphens (-). It cannot start or end with a hyphen (-), contain consecutive hyphens (-), or contain only digits.
        # 
        # If you want to create multiple cloud computers, specify their hostnames in the `name_prefix[begin_number,bits]name_suffix` format. For example, if you set Hostname to ecd-[1,4]-test, the hostnames of the cloud computers will be assigned sequentially as ecd-0001-test, ecd-0002-test, and so on.
        # 
        # *   `name_prefix`: the prefix of the hostname.
        # *   `[begin_number,bits]`: the sequential number in the hostname. The `begin_number` value is the starting number. Valid values of begin_number: 0 to 999999. Default value: 0. The `bits` value is the number of digits. Valid values: 1 to 6. Default value: 6.
        # *   `name_suffix`: the suffix of the hostname.
        self.hostname = hostname
        # The duration after which a session is terminated if no keyboard or mouse activity is detected. When an end user connects to a cloud computer, a session is initiated. If no input from the keyboard or mouse is detected within this specified timeframe, the session is automatically closed. Unit: milliseconds. Valid values: 360000 to 3600000 (6 minutes to 60 minutes)
        # 
        # The system prompts end users to save their data 30 seconds before a session is disconnected. To avoid data loss, end users must save their session data upon receiving the prompt.
        # 
        # >  This parameter is suitable only for cloud computers whose image version is v1.0.2 or later.
        self.idle_disconnect_duration = idle_disconnect_duration
        # The ID of the image.
        self.image_id = image_id
        # The duration for which each session remains active after disconnection. Valid values: 180000 (3 minutes) to 345600000 (4 days). Unit: milliseconds. If you set this parameter to 0, the session is permanently retained after disconnection.
        # 
        # When a session is disconnected, take note of the following items: 1. If the end user does not resume the session within the specified duration, the session will close, and all unsaved data will be cleared. 2. If the end user resumes the session within the specified duration, the session data will remain accessible for continued use.
        self.keep_duration = keep_duration
        # The load balancing policy of the multi-session shared group.
        # 
        # >  This parameter is not publicly available.
        # 
        # Valid values:
        # 
        # *   0: depth-first
        # *   1: breadth first
        self.load_policy = load_policy
        # The maximum number of pay-as-you-go cloud computers that can be automatically provisioned at the same time in the shared group. Valid values: 0 to 500.
        self.max_desktops_count = max_desktops_count
        # The minimum number of subscription cloud computers that can be automatically provisioned at the same time in the shared group. This parameter is required if you set `ChargeType` to `PrePaid`. Default value: 1. Valid values: 0 to `MaxDesktopsCount`.
        self.min_desktops_count = min_desktops_count
        # Specifies whether the shared group is a multi-cloud computer type.
        # 
        # Valid values:
        # 
        # *   true: a multi-cloud computer type.
        # *   false: a single-cloud computer type.
        self.multi_resource = multi_resource
        # The ID of the office network.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The session type of the shared group.
        # 
        # >  This parameter is not publicly available.
        # 
        # Valid values:
        # 
        # *   0: single-session.
        # *   1: multi-session.
        self.own_type = own_type
        # The subscription duration of the shared group. This parameter is required if you set `ChargeType` to `PrePaid`. You must specify the subscription duration unit by using `PeriodUnit`.
        # 
        # *   If you set `PeriodUnit` to `Month`, valid values of this parameter:
        # 
        #     *   1
        #     *   2
        #     *   3
        #     *   6
        # 
        # *   If you set `PeriodUnit` to `Year`, valid values of this parameter:
        # 
        #     *   1
        #     *   2
        #     *   3
        #     *   4
        #     *   5
        self.period = period
        # The unit of the subscription duration.
        self.period_unit = period_unit
        # The ID of the policy.
        # 
        # This parameter is required.
        self.policy_group_id = policy_group_id
        # Specifies whether to enable user data roaming.
        # 
        # >  This parameter is not publicly available.
        self.profile_follow_switch = profile_follow_switch
        # The ID of the coupon.
        self.promotion_id = promotion_id
        # The threshold for the ratio of connected sessions. This parameter defines the condition that activates automatic scaling of cloud computers in a multi-session shared group. The ratio of connected sessions is calculated by using the following formula:
        # 
        # `Ratio of connected sessions = Number of connected sessions/(Total number of cloud computers × Maximum number of sessions allowed for each cloud computer) × 100%`.
        # 
        # If the connected session ratio exceeds the specified threshold, new cloud computers are provisioned. If the ratio falls below the threshold, idle cloud computers are deleted.
        # 
        # >  This parameter is not publicly available.
        self.ratio_threshold = ratio_threshold
        # The ID of the region. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.reseller_owner_uid = reseller_owner_uid
        # The reset option of the shared group.
        # 
        # Valid values:
        # 
        # *   0: Reset is not required.
        # *   1: Only the system disk is reset.
        # *   2: Only the data disk is reset.
        # *   3: Both the system disk and the data disk are reset.
        self.reset_type = reset_type
        # The ID of the scaling policy.
        # 
        # >  This parameter is not publicly available.
        self.scale_strategy_id = scale_strategy_id
        # The type of the session.
        # 
        # Valid values:
        # 
        # *   SingleSession
        # *   MultipleSession
        self.session_type = session_type
        self.simple_user_group_id = simple_user_group_id
        # The ID of the automatic snapshot policy.
        self.snapshot_policy_id = snapshot_policy_id
        # The maximum period of inactivity allowed before a cloud computer is automatically stopped. If the idle duration reaches the specified limit, the system stops the cloud computer. When an end user reconnects to the stopped cloud computer, it automatically restarts. Unit: milliseconds.
        self.stop_duration = stop_duration
        # The category of the system disk.
        # 
        # Valid values:
        # 
        # *   cloud_auto: the standard SSD.
        # *   cloud_essd: the Enterprise SSD (ESSD).
        self.system_disk_category = system_disk_category
        # The performance level (PL) of the system disk of the ESSD category. Default value: PL0.
        # 
        # Valid values:
        # 
        # *   PL1
        # *   PL0
        self.system_disk_per_level = system_disk_per_level
        # The size of the system disk. Unit: GiB.
        # 
        # >  The system disk must be at least as large as the image.
        self.system_disk_size = system_disk_size
        # The tags. You can specify up to 20 tags.
        self.tag = tag
        # The ID of the timer group.
        self.timer_group_id = timer_group_id
        self.user_group_name = user_group_name
        self.user_ou_path = user_ou_path
        # Specifies whether to enable disk encryption.
        self.volume_encryption_enabled = volume_encryption_enabled
        # The ID of the Key Management Service (KMS) key that you want to use when disk encryption is enabled. You can call the [ListKeys](https://help.aliyun.com/document_detail/28951.html) operation to obtain a list of KMS keys.
        self.volume_encryption_key = volume_encryption_key
        # The ID of the virtual private cloud (VPC).
        # 
        # >  This parameter is not publicly available.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_classify_users is not None:
            result['AllClassifyUsers'] = self.all_classify_users

        if self.allow_auto_setup is not None:
            result['AllowAutoSetup'] = self.allow_auto_setup

        if self.allow_buffer_count is not None:
            result['AllowBufferCount'] = self.allow_buffer_count

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.bind_amount is not None:
            result['BindAmount'] = self.bind_amount

        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.buy_desktops_count is not None:
            result['BuyDesktopsCount'] = self.buy_desktops_count

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.classify is not None:
            result['Classify'] = self.classify

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.comments is not None:
            result['Comments'] = self.comments

        if self.connect_duration is not None:
            result['ConnectDuration'] = self.connect_duration

        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category

        if self.data_disk_per_level is not None:
            result['DataDiskPerLevel'] = self.data_disk_per_level

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.default_init_desktop_count is not None:
            result['DefaultInitDesktopCount'] = self.default_init_desktop_count

        if self.default_language is not None:
            result['DefaultLanguage'] = self.default_language

        if self.delete_duration is not None:
            result['DeleteDuration'] = self.delete_duration

        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.exclusive_type is not None:
            result['ExclusiveType'] = self.exclusive_type

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.group_amount is not None:
            result['GroupAmount'] = self.group_amount

        if self.group_version is not None:
            result['GroupVersion'] = self.group_version

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.idle_disconnect_duration is not None:
            result['IdleDisconnectDuration'] = self.idle_disconnect_duration

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration

        if self.load_policy is not None:
            result['LoadPolicy'] = self.load_policy

        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count

        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count

        if self.multi_resource is not None:
            result['MultiResource'] = self.multi_resource

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.own_type is not None:
            result['OwnType'] = self.own_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.profile_follow_switch is not None:
            result['ProfileFollowSwitch'] = self.profile_follow_switch

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.ratio_threshold is not None:
            result['RatioThreshold'] = self.ratio_threshold

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        if self.reset_type is not None:
            result['ResetType'] = self.reset_type

        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id

        if self.session_type is not None:
            result['SessionType'] = self.session_type

        if self.simple_user_group_id is not None:
            result['SimpleUserGroupId'] = self.simple_user_group_id

        if self.snapshot_policy_id is not None:
            result['SnapshotPolicyId'] = self.snapshot_policy_id

        if self.stop_duration is not None:
            result['StopDuration'] = self.stop_duration

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_per_level is not None:
            result['SystemDiskPerLevel'] = self.system_disk_per_level

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.timer_group_id is not None:
            result['TimerGroupId'] = self.timer_group_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        if self.user_ou_path is not None:
            result['UserOuPath'] = self.user_ou_path

        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled

        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllClassifyUsers') is not None:
            self.all_classify_users = m.get('AllClassifyUsers')

        if m.get('AllowAutoSetup') is not None:
            self.allow_auto_setup = m.get('AllowAutoSetup')

        if m.get('AllowBufferCount') is not None:
            self.allow_buffer_count = m.get('AllowBufferCount')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BindAmount') is not None:
            self.bind_amount = m.get('BindAmount')

        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('BuyDesktopsCount') is not None:
            self.buy_desktops_count = m.get('BuyDesktopsCount')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('ConnectDuration') is not None:
            self.connect_duration = m.get('ConnectDuration')

        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')

        if m.get('DataDiskPerLevel') is not None:
            self.data_disk_per_level = m.get('DataDiskPerLevel')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('DefaultInitDesktopCount') is not None:
            self.default_init_desktop_count = m.get('DefaultInitDesktopCount')

        if m.get('DefaultLanguage') is not None:
            self.default_language = m.get('DefaultLanguage')

        if m.get('DeleteDuration') is not None:
            self.delete_duration = m.get('DeleteDuration')

        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('ExclusiveType') is not None:
            self.exclusive_type = m.get('ExclusiveType')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('GroupAmount') is not None:
            self.group_amount = m.get('GroupAmount')

        if m.get('GroupVersion') is not None:
            self.group_version = m.get('GroupVersion')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('IdleDisconnectDuration') is not None:
            self.idle_disconnect_duration = m.get('IdleDisconnectDuration')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')

        if m.get('LoadPolicy') is not None:
            self.load_policy = m.get('LoadPolicy')

        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')

        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')

        if m.get('MultiResource') is not None:
            self.multi_resource = m.get('MultiResource')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('ProfileFollowSwitch') is not None:
            self.profile_follow_switch = m.get('ProfileFollowSwitch')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RatioThreshold') is not None:
            self.ratio_threshold = m.get('RatioThreshold')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')

        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')

        if m.get('SimpleUserGroupId') is not None:
            self.simple_user_group_id = m.get('SimpleUserGroupId')

        if m.get('SnapshotPolicyId') is not None:
            self.snapshot_policy_id = m.get('SnapshotPolicyId')

        if m.get('StopDuration') is not None:
            self.stop_duration = m.get('StopDuration')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskPerLevel') is not None:
            self.system_disk_per_level = m.get('SystemDiskPerLevel')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDesktopGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TimerGroupId') is not None:
            self.timer_group_id = m.get('TimerGroupId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        if m.get('UserOuPath') is not None:
            self.user_ou_path = m.get('UserOuPath')

        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')

        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateDesktopGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You cannot specify an empty string as a tag key. A tag key can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag key cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
        self.key = key
        # The tag value. You can specify an empty string as a tag key. A tag value can be up to 128 characters in length and cannot start with `acs:`. The tag value cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
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

