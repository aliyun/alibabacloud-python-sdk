# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class CreateDesktopsRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        app_rule_id: str = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        bundle_id: str = None,
        bundle_models: List[main_models.CreateDesktopsRequestBundleModels] = None,
        channel_cookie: str = None,
        charge_type: str = None,
        desktop_attachment: main_models.CreateDesktopsRequestDesktopAttachment = None,
        desktop_member_ip: str = None,
        desktop_name: str = None,
        desktop_name_suffix: bool = None,
        desktop_timers: List[main_models.CreateDesktopsRequestDesktopTimers] = None,
        directory_id: str = None,
        end_user_id: List[str] = None,
        extend_info: str = None,
        group_id: str = None,
        hostname: str = None,
        month_desktop_setting: main_models.CreateDesktopsRequestMonthDesktopSetting = None,
        office_site_id: str = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        promotion_id: str = None,
        qos_rule_id: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
        resource_group_id: str = None,
        saving_plan_id: str = None,
        snapshot_policy_id: str = None,
        subnet_id: str = None,
        tag: List[main_models.CreateDesktopsRequestTag] = None,
        timer_group_id: str = None,
        user_assign_mode: str = None,
        user_commands: List[main_models.CreateDesktopsRequestUserCommands] = None,
        user_name: str = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
        vpc_id: str = None,
    ):
        # The number of cloud computers that you want to create. Valid values: 1 to 300. Default value: 1.
        self.amount = amount
        self.app_rule_id = app_rule_id
        # Specifies whether to enable automatic payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. This parameter takes effect only when the ChargeType parameter is set to PrePaid.
        self.auto_renew = auto_renew
        # The ID of the cloud computer template.
        self.bundle_id = bundle_id
        # The cloud computer templates.
        self.bundle_models = bundle_models
        self.channel_cookie = channel_cookie
        # The billing method of the cloud computers.
        # 
        # Default value: PostPaid. Valid values:
        # 
        # *   Postpaid: pay-as-you-go
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   PrePaid: subscription
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.charge_type = charge_type
        # The input parameters used when no templates are used.
        self.desktop_attachment = desktop_attachment
        # The private IP address of the cloud computer.
        self.desktop_member_ip = desktop_member_ip
        # The name of the cloud computer. The name must meet the following requirements:
        # 
        # *   The name must be 1 to 64 characters in length.
        # *   The name must start with a letter but cannot start with `http://` or `https://`.
        # *   The name can only contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        self.desktop_name = desktop_name
        # Specifies whether to automatically add suffixes to the names of cloud computers when you create multiple cloud computers at the same time.
        # 
        # Default value: true. Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   False
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.desktop_name_suffix = desktop_name_suffix
        # The details of the scheduled task on cloud computers.
        self.desktop_timers = desktop_timers
        # >  This parameter is not publicly available.
        self.directory_id = directory_id
        # The IDs of the end users to which you want to assign the cloud computers. You can specify 1 to 100 IDs.
        self.end_user_id = end_user_id
        self.extend_info = extend_info
        # The ID of the cloud computer pool.
        self.group_id = group_id
        # The custom hostnames of the cloud computers. This parameter is valid only if the office network is an AD office network and the operating system type of the cloud computers is Windows.
        # 
        # The hostnames must meet the following requirements:
        # 
        # *   The hostnames must be 2 to 15 characters in length.
        # *   The hostnames can contain only letters, digits, and hyphens (-). The hostnames cannot start or end with a hyphen (-), contain consecutive hyphens (-), or contain only digits.
        # 
        # When you create multiple cloud computers, you can use the `name_prefix[begin_number,bits]name_suffix` naming format to name the cloud computers. For example, if you set the value of the Hostname parameter to ecd-[1,4]-test, the hostname of the first cloud computer is ecd-0001-test, the hostname of the second cloud computer is ecd-0002-test, and so on.
        # 
        # *   `name_prefix`: the prefix of the hostname.
        # *   `[begin_number,bits]`: the sequential number in the hostname. The `begin_number` value is the starting digit. Valid values of begin_number: 0 to 999999. Default value: 0. The `bits` value is the number of digits. Valid values: 1 to 6. Default value: 6.
        # *   `name_suffix`: the suffix of the hostname.
        self.hostname = hostname
        # > This parameter is not publicly available.
        self.month_desktop_setting = month_desktop_setting
        # The office network ID.
        self.office_site_id = office_site_id
        # The subscription duration of the cloud desktop that you want to create. The unit is specified by the `PeriodUnit` parameter. This parameter takes effect and is required only when the `ChargeType` parameter is set to `PrePaid`.
        # 
        # *   Valid values if the `PeriodUnit` parameter is set to `Month`:
        # 
        #     *   1
        #     *   2
        #     *   3
        #     *   6
        # 
        # *   Valid values if the `PeriodUnit` parameter is set to `Year`:
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
        self.policy_group_id = policy_group_id
        # The ID of the sales promotion.
        self.promotion_id = promotion_id
        self.qos_rule_id = qos_rule_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.reseller_owner_uid = reseller_owner_uid
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the saving plan.
        self.saving_plan_id = saving_plan_id
        # The ID of the auto-snapshot policy.
        self.snapshot_policy_id = snapshot_policy_id
        self.subnet_id = subnet_id
        # The tags that you want to add to the cloud desktop.
        self.tag = tag
        # The ID of the timer group.
        self.timer_group_id = timer_group_id
        # How the cloud computers are assigned.
        # 
        # >  If you do not specify the `EndUserId` parameter, the cloud computers are not assigned to end users after the cloud computers are created.
        # 
        # Default value: ALL. Valid values:
        # 
        # *   ALL: If you specify the EndUserId parameter, the cloud computers are assigned to all specified end users after the cloud computers are created.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   PER_USER: If you specify the EndUserId parameter, the cloud computers are evenly assigned to the specified end users after the cloud computers are created.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     In this case, you must make sure that the value of the Amount parameter can be divided by the N value of the EndUserId.N parameter that you specify.
        # 
        #     <!-- -->
        self.user_assign_mode = user_assign_mode
        # Details about the custom command scripts.
        self.user_commands = user_commands
        # >  This parameter is not publicly available.
        self.user_name = user_name
        # Specifies whether to enable disk encryption.
        self.volume_encryption_enabled = volume_encryption_enabled
        # The ID of the Key Management Service (KMS) key that you want to use when disk encryption is enabled. You can call the [ListKeys](https://help.aliyun.com/document_detail/28951.html) operation to obtain a list of KMS keys.
        self.volume_encryption_key = volume_encryption_key
        # >  This parameter is not publicly available.
        self.vpc_id = vpc_id

    def validate(self):
        if self.bundle_models:
            for v1 in self.bundle_models:
                 if v1:
                    v1.validate()
        if self.desktop_attachment:
            self.desktop_attachment.validate()
        if self.desktop_timers:
            for v1 in self.desktop_timers:
                 if v1:
                    v1.validate()
        if self.month_desktop_setting:
            self.month_desktop_setting.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.user_commands:
            for v1 in self.user_commands:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.app_rule_id is not None:
            result['AppRuleId'] = self.app_rule_id

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        result['BundleModels'] = []
        if self.bundle_models is not None:
            for k1 in self.bundle_models:
                result['BundleModels'].append(k1.to_map() if k1 else None)

        if self.channel_cookie is not None:
            result['ChannelCookie'] = self.channel_cookie

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.desktop_attachment is not None:
            result['DesktopAttachment'] = self.desktop_attachment.to_map()

        if self.desktop_member_ip is not None:
            result['DesktopMemberIp'] = self.desktop_member_ip

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_name_suffix is not None:
            result['DesktopNameSuffix'] = self.desktop_name_suffix

        result['DesktopTimers'] = []
        if self.desktop_timers is not None:
            for k1 in self.desktop_timers:
                result['DesktopTimers'].append(k1.to_map() if k1 else None)

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.month_desktop_setting is not None:
            result['MonthDesktopSetting'] = self.month_desktop_setting.to_map()

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.qos_rule_id is not None:
            result['QosRuleId'] = self.qos_rule_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.saving_plan_id is not None:
            result['SavingPlanId'] = self.saving_plan_id

        if self.snapshot_policy_id is not None:
            result['SnapshotPolicyId'] = self.snapshot_policy_id

        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.timer_group_id is not None:
            result['TimerGroupId'] = self.timer_group_id

        if self.user_assign_mode is not None:
            result['UserAssignMode'] = self.user_assign_mode

        result['UserCommands'] = []
        if self.user_commands is not None:
            for k1 in self.user_commands:
                result['UserCommands'].append(k1.to_map() if k1 else None)

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled

        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AppRuleId') is not None:
            self.app_rule_id = m.get('AppRuleId')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        self.bundle_models = []
        if m.get('BundleModels') is not None:
            for k1 in m.get('BundleModels'):
                temp_model = main_models.CreateDesktopsRequestBundleModels()
                self.bundle_models.append(temp_model.from_map(k1))

        if m.get('ChannelCookie') is not None:
            self.channel_cookie = m.get('ChannelCookie')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DesktopAttachment') is not None:
            temp_model = main_models.CreateDesktopsRequestDesktopAttachment()
            self.desktop_attachment = temp_model.from_map(m.get('DesktopAttachment'))

        if m.get('DesktopMemberIp') is not None:
            self.desktop_member_ip = m.get('DesktopMemberIp')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopNameSuffix') is not None:
            self.desktop_name_suffix = m.get('DesktopNameSuffix')

        self.desktop_timers = []
        if m.get('DesktopTimers') is not None:
            for k1 in m.get('DesktopTimers'):
                temp_model = main_models.CreateDesktopsRequestDesktopTimers()
                self.desktop_timers.append(temp_model.from_map(k1))

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('MonthDesktopSetting') is not None:
            temp_model = main_models.CreateDesktopsRequestMonthDesktopSetting()
            self.month_desktop_setting = temp_model.from_map(m.get('MonthDesktopSetting'))

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('QosRuleId') is not None:
            self.qos_rule_id = m.get('QosRuleId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SavingPlanId') is not None:
            self.saving_plan_id = m.get('SavingPlanId')

        if m.get('SnapshotPolicyId') is not None:
            self.snapshot_policy_id = m.get('SnapshotPolicyId')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDesktopsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TimerGroupId') is not None:
            self.timer_group_id = m.get('TimerGroupId')

        if m.get('UserAssignMode') is not None:
            self.user_assign_mode = m.get('UserAssignMode')

        self.user_commands = []
        if m.get('UserCommands') is not None:
            for k1 in m.get('UserCommands'):
                temp_model = main_models.CreateDesktopsRequestUserCommands()
                self.user_commands.append(temp_model.from_map(k1))

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')

        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateDesktopsRequestUserCommands(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_encoding: str = None,
        content_type: str = None,
    ):
        # The command content.
        self.content = content
        # The encoding mode of the command content.
        # 
        # Valid values:
        # 
        # *   Base64: encodes the command content in Base64.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   PlainText: does not encode the command content.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.content_encoding = content_encoding
        # The language type of the command.
        # 
        # Valid values:
        # 
        # *   RunPowerShellScript: PowerShell commands (applicable to Windows cloud computers).
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   RunShellScript: shell commands (applicable to Linux cloud computers).
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   RunBatScript: batch commands (applicable to Windows cloud computers).
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.content_type = content_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        return self

class CreateDesktopsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. You can specify 1 to 20 keys for a tag.
        self.key = key
        # The value of the tag. You can specify 1 to 20 values for a tag.
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

class CreateDesktopsRequestMonthDesktopSetting(DaraModel):
    def __init__(
        self,
        buyer_id: int = None,
        desktop_id: str = None,
        use_duration: int = None,
    ):
        # > This parameter is not publicly available.
        self.buyer_id = buyer_id
        # > This parameter is not publicly available.
        self.desktop_id = desktop_id
        # > This parameter is not publicly available.
        self.use_duration = use_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.use_duration is not None:
            result['UseDuration'] = self.use_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('UseDuration') is not None:
            self.use_duration = m.get('UseDuration')

        return self

class CreateDesktopsRequestDesktopTimers(DaraModel):
    def __init__(
        self,
        allow_client_setting: bool = None,
        cron_expression: str = None,
        enforce: bool = None,
        interval: int = None,
        operation_type: str = None,
        reset_type: str = None,
        timer_type: str = None,
    ):
        # Specifies whether to allow the end user to configure the scheduled task.
        self.allow_client_setting = allow_client_setting
        # The cron expression for the scheduled task.
        # 
        # >  The time must be in UTC. For example, for 24:00 (UTC+8), you must set the value to 0 0 16 ? \\* 1,2,3,4,5,6,7
        self.cron_expression = cron_expression
        # Specifies whether to forcibly execute the scheduled task.
        # 
        # Valid values:
        # 
        # *   true: forcibly executes the scheduled task regardless of the status and connection of the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false: does not forcibly execute the scheduled task.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enforce = enforce
        # The interval at which cloud computers are created. Unit: minutes.
        self.interval = interval
        # The operations that scheduled tasks support. This parameter is valid only when TimerType is set to NoConnect.
        # 
        # Valid values:
        # 
        # *   Hibernate: hibernates the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Shutdown: stops the cloud computers.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.operation_type = operation_type
        # The reset type of the cloud computers.
        # 
        # Valid values:
        # 
        # *   RESET_TYPE_SYSTEM: resets the system disks.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   RESET_TYPE_BOTH: resets the system disks and data disks.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.reset_type = reset_type
        # The type of the scheduled task.
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_client_setting is not None:
            result['AllowClientSetting'] = self.allow_client_setting

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.enforce is not None:
            result['Enforce'] = self.enforce

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.reset_type is not None:
            result['ResetType'] = self.reset_type

        if self.timer_type is not None:
            result['TimerType'] = self.timer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowClientSetting') is not None:
            self.allow_client_setting = m.get('AllowClientSetting')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Enforce') is not None:
            self.enforce = m.get('Enforce')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        return self

class CreateDesktopsRequestDesktopAttachment(DaraModel):
    def __init__(
        self,
        data_disk_category: str = None,
        data_disk_per_level: str = None,
        data_disk_size: int = None,
        default_language: str = None,
        desktop_type: str = None,
        image_id: str = None,
        system_disk_category: str = None,
        system_disk_per_level: str = None,
        system_disk_size: int = None,
    ):
        # The category of the data disk. Valid values:
        # 
        # *   cloud_auto: SSD
        # *   cloud_essd: ESSD
        self.data_disk_category = data_disk_category
        # The performance level of the data disk. Valid values:
        # 
        # - PL0 (default)
        # - PL1
        self.data_disk_per_level = data_disk_per_level
        # The size of the data disk. Unit: GiB.
        self.data_disk_size = data_disk_size
        # The default display language:
        # 
        # - zh-CN: Simplified Chinese
        # - zh-HK: Traditional Chinese
        # - en-US: English
        # - ja-JP: Japanese
        self.default_language = default_language
        # The desktop type. You can call the [DescribeDesktopTypes](~~DescribeDesktopTypes~~) operation to query the IDs of supported desktop types.
        self.desktop_type = desktop_type
        # The ID of the image.
        self.image_id = image_id
        # The category of the system disk. Valid values:
        # 
        # *   cloud_auto: SSD
        # *   cloud_essd: ESSD
        self.system_disk_category = system_disk_category
        # The performance level of the system disk. Valid values:
        # 
        # - PL0 (default)
        # - PL1
        self.system_disk_per_level = system_disk_per_level
        # The size of the system disk. Unit: GiB.
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category

        if self.data_disk_per_level is not None:
            result['DataDiskPerLevel'] = self.data_disk_per_level

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.default_language is not None:
            result['DefaultLanguage'] = self.default_language

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_per_level is not None:
            result['SystemDiskPerLevel'] = self.system_disk_per_level

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')

        if m.get('DataDiskPerLevel') is not None:
            self.data_disk_per_level = m.get('DataDiskPerLevel')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('DefaultLanguage') is not None:
            self.default_language = m.get('DefaultLanguage')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskPerLevel') is not None:
            self.system_disk_per_level = m.get('SystemDiskPerLevel')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

class CreateDesktopsRequestBundleModels(DaraModel):
    def __init__(
        self,
        amount: int = None,
        bundle_id: str = None,
        desktop_name: str = None,
        end_user_ids: List[str] = None,
        hostname: str = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
    ):
        # The number of cloud computers that you want to create. Valid values: 1 to 300. Default value: null.
        self.amount = amount
        # The ID of a cloud computer template.
        self.bundle_id = bundle_id
        # The name of the cloud computer. The name must meet the following requirements:
        # 
        # *   The name must be 1 to 64 characters in length.
        # *   The name must start with a letter but cannot start with `http://` or `https://`.
        # *   The name can only contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        self.desktop_name = desktop_name
        # The IDs of the end users to whom the cloud computer are assigned.
        self.end_user_ids = end_user_ids
        # The custom hostnames of the cloud computers. This parameter is valid only if the office network is an AD office network and the operating system type of the cloud computers is Windows.
        # 
        # The hostnames must meet the following requirements:
        # 
        # *   The hostnames must be 2 to 15 characters in length.
        # *   The hostnames can contain only letters, digits, and hyphens (-). The hostnames cannot start or end with a hyphen (-), contain consecutive hyphens (-), or contain only digits.
        # 
        # When you create multiple cloud computers, you can use the `name_prefix[begin_number,bits]name_suffix` naming format to name the cloud computers. For example, if you set the value of the Hostname parameter to ecd-[1,4]-test, the hostname of the first cloud computer is ecd-0001-test, the hostname of the second cloud computer is ecd-0002-test, and so on.
        # 
        # *   `name_prefix`: the prefix of the hostname.
        # *   `[begin_number,bits]`: the sequential number in the hostname. The `begin_number` value is the starting digit. Valid values of begin_number: 0 to 999999. Default value: 0. The `bits` value is the number of digits. Valid values: 1 to 6. Default value: 6.
        # *   `name_suffix`: the suffix of the hostname.
        self.hostname = hostname
        # Specifies whether to enable disk encryption.
        self.volume_encryption_enabled = volume_encryption_enabled
        # The ID of the Key Management Service (KMS) key that is used when disk encryption is enabled. You can call the [ListKeys](https://help.aliyun.com/document_detail/28951.html) operation to query the list of KMS keys.
        self.volume_encryption_key = volume_encryption_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled

        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')

        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')

        return self

