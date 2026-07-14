# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class CreateDesktopsShrinkRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        app_rule_id: str = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        bundle_id: str = None,
        bundle_models: List[main_models.CreateDesktopsShrinkRequestBundleModels] = None,
        channel_cookie: str = None,
        charge_type: str = None,
        desktop_attachment_shrink: str = None,
        desktop_member_ip: str = None,
        desktop_name: str = None,
        desktop_name_suffix: bool = None,
        desktop_timers: List[main_models.CreateDesktopsShrinkRequestDesktopTimers] = None,
        directory_id: str = None,
        end_user_id: List[str] = None,
        extend_info: str = None,
        group_id: str = None,
        hostname: str = None,
        month_desktop_setting: main_models.CreateDesktopsShrinkRequestMonthDesktopSetting = None,
        office_site_id: str = None,
        ou_path: str = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        promotion_id: str = None,
        purchase_options_shrink: str = None,
        qos_rule_id: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
        resource_group_id: str = None,
        saving_plan_id: str = None,
        snapshot_policy_id: str = None,
        sub_pay_type: str = None,
        subnet_id: str = None,
        tag: List[main_models.CreateDesktopsShrinkRequestTag] = None,
        timer_group_id: str = None,
        user_assign_mode: str = None,
        user_commands: List[main_models.CreateDesktopsShrinkRequestUserCommands] = None,
        user_name: str = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
        vpc_id: str = None,
    ):
        # The number of cloud desktops to create. Valid values: 1 to 300. Default value: 1.
        self.amount = amount
        # The application control policy ID.
        self.app_rule_id = app_rule_id
        # Specifies whether to enable automatic payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. This parameter takes effect only when `ChargeType` is set to `PrePaid`.
        self.auto_renew = auto_renew
        # The cloud desktop template ID. If no template ID is specified, you can create a cloud desktop by specifying the required fields.
        self.bundle_id = bundle_id
        # The list of cloud desktop templates.
        self.bundle_models = bundle_models
        # > This field is not available for use.
        self.channel_cookie = channel_cookie
        # The billing method of the cloud desktop.
        self.charge_type = charge_type
        # The parameters for creating a cloud desktop without a template. This parameter is invalid when the BundleId parameter is specified.
        self.desktop_attachment_shrink = desktop_attachment_shrink
        # The private IP address of the cloud desktop.
        self.desktop_member_ip = desktop_member_ip
        # The cloud desktop name. The naming rules are as follows:
        # 
        # - The name can be up to 64 characters in length.
        # - The name must start with a letter or a Chinese character and cannot start with `http://` or `https://`.
        # - The name can contain Chinese characters, letters, digits, colons (:), underscores (_), periods (.), or hyphens (-).
        self.desktop_name = desktop_name
        # Specifies whether to automatically append a suffix to the cloud desktop name when you create multiple cloud desktops in a batch.
        self.desktop_name_suffix = desktop_name_suffix
        # The scheduled task details of the cloud desktop. This parameter is being deprecated. Use the TimerGroupId parameter instead.
        self.desktop_timers = desktop_timers
        # > This parameter is not available for use.
        self.directory_id = directory_id
        # The list of authorized user IDs to add to the cloud desktops. You can specify 1 to 100 user IDs.
        self.end_user_id = end_user_id
        # The extended information in JSON string format. This parameter is available only for internal customers.
        self.extend_info = extend_info
        # The cloud desktop pool ID.
        self.group_id = group_id
        # The custom hostname of the cloud desktop. Settings for this parameter are supported only for cloud desktops that run the Windows operating system in an AD office network.
        # 
        # The naming rules for the hostname are as follows:
        # 
        # - The hostname must be 2 to 15 characters in length.
        # - The hostname can contain uppercase letters, lowercase letters, digits, or hyphens (-). It cannot start or end with a hyphen, contain consecutive hyphens, or consist of only digits.
        # 
        # When you create multiple cloud desktops, you can use the `name_prefix[begin_number,bits]name_suffix` format to uniformly name the cloud desktops. For example, if you set Hostname to ecd-[1,4]-test, the hostname of the first cloud desktop is ecd-0001-test, the hostname of the second cloud desktop is ecd-0002-test, and so on.
        # 
        # - `name_prefix`: the prefix of the hostname.
        # - `[begin_number,bits]`: the sequential number in the hostname. `begin_number` is the starting number. Valid values: 0 to 999999. Default value: 0. `bits` is the number of digits. Valid values: 1 to 6. Default value: 6.
        # - `name_suffix`: the suffix of the hostname.
        self.hostname = hostname
        # The purchase parameters for the monthly hourly package.
        self.month_desktop_setting = month_desktop_setting
        # The office network ID.
        self.office_site_id = office_site_id
        # The OU path. If specified, the cloud desktop is added to the corresponding organizational unit (OU) in Active Directory (AD).
        self.ou_path = ou_path
        # The subscription duration of the resource. The unit is specified by `PeriodUnit`. This parameter takes effect and is required only when `ChargeType` is set to `PrePaid`.
        # 
        # - If `PeriodUnit` is set to `Month`, valid values of this parameter:
        # 
        #      - 1
        #     -  2
        #     - 3
        #     - 6
        # 
        # - If `PeriodUnit` is set to `Year`, valid values of this parameter:
        # 
        #     - 1
        #     - 2
        #     - 3
        #     - 4
        #     - 5
        self.period = period
        # The unit of the subscription duration.
        self.period_unit = period_unit
        # The policy ID.
        self.policy_group_id = policy_group_id
        # The promotion ID.
        self.promotion_id = promotion_id
        # The additional parameters for a specific purchase type.
        self.purchase_options_shrink = purchase_options_shrink
        # The public network rate limiting rule ID.
        self.qos_rule_id = qos_rule_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The user ID for resource ownership in reseller pattern. This parameter is not required in non-reseller pattern.
        self.reseller_owner_uid = reseller_owner_uid
        # The WUYING resource group ID.
        self.resource_group_id = resource_group_id
        # > This field is not available for use.
        self.saving_plan_id = saving_plan_id
        # The WUYING automatic snapshot policy ID.
        self.snapshot_policy_id = snapshot_policy_id
        self.sub_pay_type = sub_pay_type
        # The subnet ID.
        self.subnet_id = subnet_id
        # The tags.
        self.tag = tag
        # The scheduled task group ID.
        self.timer_group_id = timer_group_id
        # The cloud desktop assignment mode.
        # 
        # > If `EndUserId` is not specified, the created cloud desktops are not assigned to any user.
        self.user_assign_mode = user_assign_mode
        # The custom command script data.
        self.user_commands = user_commands
        # > This parameter is not available for use.
        self.user_name = user_name
        # Specifies whether to enable cloud disk encryption.
        self.volume_encryption_enabled = volume_encryption_enabled
        # The ID of the Key Management Service (KMS) key used for cloud disk encryption. You can call [ListKeys](https://help.aliyun.com/document_detail/28951.html) to obtain the key ID.
        self.volume_encryption_key = volume_encryption_key
        # > This parameter is not available for use.
        self.vpc_id = vpc_id

    def validate(self):
        if self.bundle_models:
            for v1 in self.bundle_models:
                 if v1:
                    v1.validate()
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

        if self.desktop_attachment_shrink is not None:
            result['DesktopAttachment'] = self.desktop_attachment_shrink

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

        if self.ou_path is not None:
            result['OuPath'] = self.ou_path

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.purchase_options_shrink is not None:
            result['PurchaseOptions'] = self.purchase_options_shrink

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

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

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
                temp_model = main_models.CreateDesktopsShrinkRequestBundleModels()
                self.bundle_models.append(temp_model.from_map(k1))

        if m.get('ChannelCookie') is not None:
            self.channel_cookie = m.get('ChannelCookie')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DesktopAttachment') is not None:
            self.desktop_attachment_shrink = m.get('DesktopAttachment')

        if m.get('DesktopMemberIp') is not None:
            self.desktop_member_ip = m.get('DesktopMemberIp')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopNameSuffix') is not None:
            self.desktop_name_suffix = m.get('DesktopNameSuffix')

        self.desktop_timers = []
        if m.get('DesktopTimers') is not None:
            for k1 in m.get('DesktopTimers'):
                temp_model = main_models.CreateDesktopsShrinkRequestDesktopTimers()
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
            temp_model = main_models.CreateDesktopsShrinkRequestMonthDesktopSetting()
            self.month_desktop_setting = temp_model.from_map(m.get('MonthDesktopSetting'))

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OuPath') is not None:
            self.ou_path = m.get('OuPath')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('PurchaseOptions') is not None:
            self.purchase_options_shrink = m.get('PurchaseOptions')

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

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDesktopsShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TimerGroupId') is not None:
            self.timer_group_id = m.get('TimerGroupId')

        if m.get('UserAssignMode') is not None:
            self.user_assign_mode = m.get('UserAssignMode')

        self.user_commands = []
        if m.get('UserCommands') is not None:
            for k1 in m.get('UserCommands'):
                temp_model = main_models.CreateDesktopsShrinkRequestUserCommands()
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

class CreateDesktopsShrinkRequestUserCommands(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_encoding: str = None,
        content_type: str = None,
    ):
        # The command content.
        self.content = content
        # The encoding method of the command content (CommandContent).
        self.content_encoding = content_encoding
        # The language type of the command.
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

class CreateDesktopsShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify 1 to 20 tag keys.
        self.key = key
        # The tag value. You can specify 1 to 20 tag values.
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

class CreateDesktopsShrinkRequestMonthDesktopSetting(DaraModel):
    def __init__(
        self,
        buyer_id: int = None,
        desktop_id: str = None,
        use_duration: int = None,
    ):
        # > This field is not available for use.
        self.buyer_id = buyer_id
        # > This field is not available for use.
        self.desktop_id = desktop_id
        # The package option when purchasing a monthly hourly package. Valid values: 120, 250, and 360.
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

class CreateDesktopsShrinkRequestDesktopTimers(DaraModel):
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
        # Specifies whether to allow end users to configure scheduled tasks.
        self.allow_client_setting = allow_client_setting
        # The cron expression of the scheduled task.
        # 
        # >Notice: Specify the time in UTC. For example, to schedule a task at 00:00 (UTC+8) every day, set the value to 0 0 16 ? * 1,2,3,4,5,6,7.</notice>
        self.cron_expression = cron_expression
        # Specifies whether to forcefully execute the task.
        self.enforce = enforce
        # The time interval, in minutes.
        self.interval = interval
        # The operation type of the scheduled task. Currently, only the disconnection scheduled task is supported.
        self.operation_type = operation_type
        # The reset type of the cloud desktop.
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

class CreateDesktopsShrinkRequestBundleModels(DaraModel):
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
        # The number of cloud desktops to create. Valid values: 1 to 300. Default value: 0.
        self.amount = amount
        # The cloud desktop template ID.
        self.bundle_id = bundle_id
        # The cloud desktop name. The naming rules are as follows:
        # 
        # - The name can be up to 64 characters in length.
        # - The name must start with a letter or a Chinese character and cannot start with `http://` or `https://`.
        # - The name can contain Chinese characters, letters, digits, colons (:), underscores (_), periods (.), or hyphens (-).
        self.desktop_name = desktop_name
        # The list of users to whom the cloud desktops are assigned.
        self.end_user_ids = end_user_ids
        # The custom hostname of the cloud desktop. Settings for this parameter are supported only for cloud desktops that run the Windows operating system in an AD office network.
        # 
        # The naming rules for the hostname are as follows:
        # 
        # - The hostname must be 2 to 15 characters in length.
        # - The hostname can contain uppercase letters, lowercase letters, digits, or hyphens (-). It cannot start or end with a hyphen, contain consecutive hyphens, or consist of only digits.
        # 
        # When you create multiple cloud desktops, you can use the `name_prefix[begin_number,bits]name_suffix` format to uniformly name the cloud desktops. For example, if you set Hostname to ecd-[1,4]-test, the hostname of the first cloud desktop is ecd-0001-test, the hostname of the second cloud desktop is ecd-0002-test, and so on.
        # 
        # - `name_prefix`: the prefix of the hostname.
        # - `[begin_number,bits]`: the sequential number in the hostname. `begin_number` is the starting number. Valid values: 0 to 999999. Default value: 0. `bits` is the number of digits. Valid values: 1 to 6. Default value: 6.
        # - `name_suffix`: the suffix of the hostname.
        self.hostname = hostname
        # Specifies whether to enable cloud disk encryption.
        self.volume_encryption_enabled = volume_encryption_enabled
        # The ID of the Key Management Service (KMS) key used for cloud disk encryption. You can call [ListKeys](https://help.aliyun.com/document_detail/28951.html) to obtain the key ID.
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

