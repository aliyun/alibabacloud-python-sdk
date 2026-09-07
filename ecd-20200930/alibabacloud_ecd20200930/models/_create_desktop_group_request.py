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
        # The users of all shared cloud computer categories.
        self.all_classify_users = all_classify_users
        # Specifies whether to allow automatic creation of cloud computers within subscription shared cloud computers. This parameter takes effect and is required only when ChargeType is set to PrePaid.
        self.allow_auto_setup = allow_auto_setup
        # The number of reserved cloud computers allowed in pay-as-you-go shared cloud computers. This parameter takes effect and is required only when ChargeType is set to PostPaid. Valid values:
        self.allow_buffer_count = allow_buffer_count
        # Specifies whether automatic payment is enabled for the subscription order.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the subscription shared cloud computer.
        self.auto_renew = auto_renew
        # The number of concurrent sessions allowed per cloud computer in multi-session shared cloud computers.
        self.bind_amount = bind_amount
        # The cloud computer template ID.
        self.bundle_id = bundle_id
        # - For subscription shared cloud computers: the initial number of cloud computers to create. Valid values: 0 to 200.
        self.buy_desktops_count = buy_desktops_count
        # The billing method of the cloud computer.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The type of the shared cloud computer.
        self.classify = classify
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The remarks.
        self.comments = comments
        # The maximum duration that a session can remain in the connected state. The session is automatically disconnected when this duration is reached. Unit: milliseconds. Valid values: 900000 (15 minutes) to 345600000 (4 days).
        self.connect_duration = connect_duration
        # The data cloud disk type.
        self.data_disk_category = data_disk_category
        # The performance level of the ESSD. Default value: PL0.
        self.data_disk_per_level = data_disk_per_level
        # The size of the attached data cloud disk. Unit: GB. Valid values: 0 to 16380. The value must be a multiple of 20.
        self.data_disk_size = data_disk_size
        # The default number of cloud computers to create when you create multiple shared cloud computers. Default value: 1.
        self.default_init_desktop_count = default_init_desktop_count
        # The system language.
        self.default_language = default_language
        # The retention period before cloud computers in the cloud computer pool are automatically deleted.
        self.delete_duration = delete_duration
        # The name of the shared cloud computer. The name can be up to 30 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. The name can contain Chinese characters, letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        self.desktop_group_name = desktop_group_name
        # The cloud computer specification. You can call [DescribeDesktopTypes](~~DescribeDesktopTypes~~) to query the specification IDs supported by cloud computers.
        self.desktop_type = desktop_type
        # The directory ID.
        self.directory_id = directory_id
        # The list of user IDs for the shared cloud computer.
        self.end_user_ids = end_user_ids
        # Creates a static pool. This parameter is required when the `SessionType` parameter is set to `MultipleSession`. Set the value to `Exclusive`.
        self.exclusive_type = exclusive_type
        # The ID of the NAS file system used for user data roaming.
        self.file_system_id = file_system_id
        # The number of single shared cloud computers to create. This parameter is required only when the `MultiResource` parameter is set to `false`. Valid values: 1 to 5. Default value: 1.
        self.group_amount = group_amount
        # The version of the shared cloud computer.
        self.group_version = group_version
        # The custom hostname of the cloud computer. Only Settings for cloud computers that run the Windows operating system in AD office networks are supported.
        self.hostname = hostname
        # The maximum idle duration after a user session is established. If no keyboard or mouse activity occurs within this duration, the session is disconnected. Unit: milliseconds. Valid values: 360000 (6 minutes) to 3600000 (60 minutes).
        # 
        # 30 seconds before this duration is reached, the end user in the session receives a prompt to save document data. The end user must save document data promptly to avoid data loss.
        # 
        # > Applicable only to cloud computers with an image version of 1.0.2 or later.
        self.idle_disconnect_duration = idle_disconnect_duration
        # The image ID.
        self.image_id = image_id
        # The retention period after a session is disconnected. Unit: milliseconds. Valid values: 180000 (3 minutes) to 345600000 (4 days). A value of 0 indicates that the session is always retained.
        self.keep_duration = keep_duration
        # The load balancing policy for multi-session shared cloud computers.
        self.load_policy = load_policy
        # The maximum number of pay-as-you-go shared cloud computers. Valid values: 0 to 500.
        self.max_desktops_count = max_desktops_count
        # The maximum number of cloud computers that can be used for automatic creation for subscription shared cloud computers. This parameter takes effect and is required only when ChargeType is set to PrePaid. Default value: 1. Valid values: 0 to the value of MaxDesktopsCount.
        self.min_desktops_count = min_desktops_count
        # Specifies whether the cloud computers are multi-resource shared cloud computers.
        self.multi_resource = multi_resource
        # The ID of the office network to which the shared cloud computer belongs.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The type of the shared cloud computer.
        self.own_type = own_type
        # The subscription duration of the shared cloud computer. This parameter takes effect and is required only when ChargeType is set to PrePaid. The unit is specified by PeriodUnit.
        self.period = period
        # The unit of the subscription billable methods duration.
        self.period_unit = period_unit
        # The ID of the policy associated with the shared cloud computer.
        # 
        # This parameter is required.
        self.policy_group_id = policy_group_id
        # Specifies whether to enable user data roaming.
        self.profile_follow_switch = profile_follow_switch
        # The coupon ID.
        self.promotion_id = promotion_id
        # The session occupancy threshold used as the automatic scaling trigger condition for multi-session shared cloud computers. The session occupancy is calculated by using the following formula:
        # 
        # ```Session occupancy = Number of bound sessions / (Total number of cloud computer resources × Maximum number of sessions supported per cloud computer) × 100%```
        # 
        # When the session occupancy reaches this threshold, new cloud computers are created. When the session occupancy is below this threshold, excess cloud computers are deleted.
        # 
        # > This parameter is not yet available for use.
        self.ratio_threshold = ratio_threshold
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The user ID of the resource ownership in reseller pattern. You do not need to specify this parameter in non-reseller pattern.
        self.reseller_owner_uid = reseller_owner_uid
        # The reset type of the cloud computer.
        self.reset_type = reset_type
        # The scaling policy ID.
        self.scale_strategy_id = scale_strategy_id
        # The session type.
        self.session_type = session_type
        # The ID of the convenience user group.
        self.simple_user_group_id = simple_user_group_id
        # The ID of the automatic snapshot policy.
        self.snapshot_policy_id = snapshot_policy_id
        # The idle shutdown duration. When the cloud computer has been idle for this duration, it is automatically shut down. If a user connects after shutdown, the cloud computer automatically starts. Unit: milliseconds.
        self.stop_duration = stop_duration
        # The system cloud disk type.
        self.system_disk_category = system_disk_category
        # The performance level of the ESSD. Default value: PL0.
        self.system_disk_per_level = system_disk_per_level
        # The system cloud disk size. Unit: GiB.
        self.system_disk_size = system_disk_size
        # The list of tags. A maximum of 20 tags can be specified.
        self.tag = tag
        # The ID of the scheduled task group.
        self.timer_group_id = timer_group_id
        # The name of the user group.
        self.user_group_name = user_group_name
        # The organizational unit (OU) path of the user.
        self.user_ou_path = user_ou_path
        # Specifies whether to enable disk encryption.
        self.volume_encryption_enabled = volume_encryption_enabled
        # The ID of the KMS key used for disk encryption. You can call [ListKeys](https://help.aliyun.com/document_detail/28951.html) to obtain the key ID.
        self.volume_encryption_key = volume_encryption_key
        # The VPC ID of the office network to which the shared cloud computer belongs.
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
        # The tag key. If you specify this parameter, the value cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
        self.key = key
        # The tag value. The value can be an empty string. The tag value can be up to 128 characters in length and cannot start with `acs:`. It cannot contain `http://` or `https://`.
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

