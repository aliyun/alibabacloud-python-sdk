# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class CreateBrowserInstanceGroupRequest(DaraModel):
    def __init__(
        self,
        app_package_type: str = None,
        auth_notification_enabled: bool = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        browser_config: main_models.CreateBrowserInstanceGroupRequestBrowserConfig = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        cloud_browser_name: str = None,
        image_id: str = None,
        instance_type: str = None,
        max_amount: int = None,
        network: main_models.CreateBrowserInstanceGroupRequestNetwork = None,
        node_pool: main_models.CreateBrowserInstanceGroupRequestNodePool = None,
        os_type: str = None,
        period: int = None,
        period_unit: str = None,
        policy: main_models.CreateBrowserInstanceGroupRequestPolicy = None,
        promotion_id: str = None,
        security_policy: main_models.CreateBrowserInstanceGroupRequestSecurityPolicy = None,
        storage_policy: main_models.CreateBrowserInstanceGroupRequestStoragePolicy = None,
        sub_pay_type: str = None,
        tag: List[main_models.CreateBrowserInstanceGroupRequestTag] = None,
        timers: List[main_models.CreateBrowserInstanceGroupRequestTimers] = None,
        user_group_ids: List[str] = None,
        user_info: main_models.CreateBrowserInstanceGroupRequestUserInfo = None,
        users: List[main_models.CreateBrowserInstanceGroupRequestUsers] = None,
    ):
        # The package identifier.
        # 
        # You do not need to specify this parameter.
        self.app_package_type = app_package_type
        # Specifies whether to send notification emails for authorization and deauthorization.
        # - `true`: Sends notification emails.
        # - `false`: Does not send notification emails.
        self.auth_notification_enabled = auth_notification_enabled
        # The automatic payment parameter.
        # 
        # You do not need to specify this parameter.
        self.auto_pay = auto_pay
        # The auto-renewal parameter.
        # 
        # You do not need to specify this parameter.
        self.auto_renew = auto_renew
        # The identifier of the business region. This parameter is required.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The browser configuration.
        self.browser_config = browser_config
        # The resource billing method.
        # **For MAU scenarios:** Set this parameter to `AppInstance`, which indicates billing by instance resources.
        self.charge_resource_mode = charge_resource_mode
        # The billing method.
        # 
        # **For MAU scenarios:** Set this parameter to PostPaid, which indicates pay-as-you-go.
        self.charge_type = charge_type
        # The name of the cloud browser group. This parameter cannot be empty. It is used to distinguish different browser groups in business management scenarios.
        # 
        # This parameter is required.
        self.cloud_browser_name = cloud_browser_name
        # The image ID used by the cloud browser. The image must be compatible with the operating system.
        # If this parameter is omitted, the default image available for the account is used. If no default image is available, the creation may fail.
        # **Usage conditions:** When CookiesSync is enabled, explicitly specify an image that supports cookie synchronization.
        self.image_id = image_id
        # The instance type identifier. Select an instance type that matches the target region, operating system, and inventory conditions.
        # If this parameter is omitted, the default instance type is used.
        self.instance_type = instance_type
        # The capacity configuration in MAU billing scenarios.
        self.max_amount = max_amount
        # The configurations for the office network and website access restrictions. The selected office network must belong to the current account and reside in the region specified by BizRegionId.
        self.network = network
        # The node pool configuration.
        # You do not need to specify this parameter.
        self.node_pool = node_pool
        # The operating system type. This parameter is required.
        # Only `Windows` is supported. Other operating systems are not supported.
        self.os_type = os_type
        # The number of billing cycles for the purchase.
        # 
        # You do not need to specify this parameter.
        self.period = period
        # The unit of the billing cycle for the purchase.
        # 
        # You do not need to specify this parameter.
        self.period_unit = period_unit
        # Configures policies for the clipboard, video, watermark, session, and client access.
        self.policy = policy
        # The promotion identifier, which is used to specify the promotional offer applied to the order.
        # 
        # Applicability and specific discounts are subject to the promotion rules. You do not need to specify this parameter if no promotional offer is applied.
        self.promotion_id = promotion_id
        # The connection security policy of the browser group.
        self.security_policy = security_policy
        # The user data storage configuration of the browser group.
        self.storage_policy = storage_policy
        # The billing sub-type.
        # 
        # **You must explicitly set this parameter to mau, which indicates billing by monthly active users (MAUs).** Omitting this parameter does not enable MAU billing.
        self.sub_pay_type = sub_pay_type
        # This parameter is not supported and does not need to be specified.
        self.tag = tag
        # This parameter is not supported and does not need to be specified.
        self.timers = timers
        # The list of authorized user group IDs. You can specify up to 10 IDs. The user groups must belong to the current account and match the account type of the office network.
        # **Limits:** This parameter cannot be specified together with a non-empty Users parameter.
        self.user_group_ids = user_group_ids
        # The authorized user account information. The information must match the user and office network types.
        self.user_info = user_info
        # The list of authorized users. You can specify up to 200 users. The users must be created in advance and match the account type.
        # 
        # **Limit:** This parameter cannot be specified together with a non-empty UserGroupIds parameter.
        self.users = users

    def validate(self):
        if self.browser_config:
            self.browser_config.validate()
        if self.network:
            self.network.validate()
        if self.node_pool:
            self.node_pool.validate()
        if self.policy:
            self.policy.validate()
        if self.security_policy:
            self.security_policy.validate()
        if self.storage_policy:
            self.storage_policy.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.timers:
            for v1 in self.timers:
                 if v1:
                    v1.validate()
        if self.user_info:
            self.user_info.validate()
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_package_type is not None:
            result['AppPackageType'] = self.app_package_type

        if self.auth_notification_enabled is not None:
            result['AuthNotificationEnabled'] = self.auth_notification_enabled

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.browser_config is not None:
            result['BrowserConfig'] = self.browser_config.to_map()

        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cloud_browser_name is not None:
            result['CloudBrowserName'] = self.cloud_browser_name

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.max_amount is not None:
            result['MaxAmount'] = self.max_amount

        if self.network is not None:
            result['Network'] = self.network.to_map()

        if self.node_pool is not None:
            result['NodePool'] = self.node_pool.to_map()

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.security_policy is not None:
            result['SecurityPolicy'] = self.security_policy.to_map()

        if self.storage_policy is not None:
            result['StoragePolicy'] = self.storage_policy.to_map()

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        result['Timers'] = []
        if self.timers is not None:
            for k1 in self.timers:
                result['Timers'].append(k1.to_map() if k1 else None)

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppPackageType') is not None:
            self.app_package_type = m.get('AppPackageType')

        if m.get('AuthNotificationEnabled') is not None:
            self.auth_notification_enabled = m.get('AuthNotificationEnabled')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('BrowserConfig') is not None:
            temp_model = main_models.CreateBrowserInstanceGroupRequestBrowserConfig()
            self.browser_config = temp_model.from_map(m.get('BrowserConfig'))

        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CloudBrowserName') is not None:
            self.cloud_browser_name = m.get('CloudBrowserName')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxAmount') is not None:
            self.max_amount = m.get('MaxAmount')

        if m.get('Network') is not None:
            temp_model = main_models.CreateBrowserInstanceGroupRequestNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('NodePool') is not None:
            temp_model = main_models.CreateBrowserInstanceGroupRequestNodePool()
            self.node_pool = temp_model.from_map(m.get('NodePool'))

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('Policy') is not None:
            temp_model = main_models.CreateBrowserInstanceGroupRequestPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('SecurityPolicy') is not None:
            temp_model = main_models.CreateBrowserInstanceGroupRequestSecurityPolicy()
            self.security_policy = temp_model.from_map(m.get('SecurityPolicy'))

        if m.get('StoragePolicy') is not None:
            temp_model = main_models.CreateBrowserInstanceGroupRequestStoragePolicy()
            self.storage_policy = temp_model.from_map(m.get('StoragePolicy'))

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateBrowserInstanceGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        self.timers = []
        if m.get('Timers') is not None:
            for k1 in m.get('Timers'):
                temp_model = main_models.CreateBrowserInstanceGroupRequestTimers()
                self.timers.append(temp_model.from_map(k1))

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserInfo') is not None:
            temp_model = main_models.CreateBrowserInstanceGroupRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.CreateBrowserInstanceGroupRequestUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class CreateBrowserInstanceGroupRequestUsers(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
    ):
        # The identity of the authorized user for authorization.
        self.end_user_id = end_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        return self

class CreateBrowserInstanceGroupRequestUserInfo(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The account type of the authorized user.
        # - `simple`: Convenience account.
        # - `ad`: AD domain account.
        # The account type must match the account types of the user and the office network.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateBrowserInstanceGroupRequestTimers(DaraModel):
    def __init__(
        self,
        interval: int = None,
        timer_type: str = None,
    ):
        # This parameter is not supported and does not need to be specified.
        self.interval = interval
        # This parameter is not supported and does not need to be specified.
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interval is not None:
            result['Interval'] = self.interval

        if self.timer_type is not None:
            result['TimerType'] = self.timer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        return self

class CreateBrowserInstanceGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is not supported and does not need to be specified.
        self.key = key
        # This parameter is not supported and does not need to be specified.
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

class CreateBrowserInstanceGroupRequestStoragePolicy(DaraModel):
    def __init__(
        self,
        user_profile: main_models.CreateBrowserInstanceGroupRequestStoragePolicyUserProfile = None,
    ):
        # The user data roaming configuration, which is used to retain user configuration data.
        self.user_profile = user_profile

    def validate(self):
        if self.user_profile:
            self.user_profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_profile is not None:
            result['UserProfile'] = self.user_profile.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserProfile') is not None:
            temp_model = main_models.CreateBrowserInstanceGroupRequestStoragePolicyUserProfile()
            self.user_profile = temp_model.from_map(m.get('UserProfile'))

        return self

class CreateBrowserInstanceGroupRequestStoragePolicyUserProfile(DaraModel):
    def __init__(
        self,
        user_profile_size: int = None,
        user_profile_switch: bool = None,
    ):
        # The size of the user data roaming disk, in GB.
        self.user_profile_size = user_profile_size
        # Specifies whether to enable user data roaming.
        # - `true`: Enables user data roaming.
        # - `false`: Disables user data roaming.
        # In Windows scenarios, if this parameter is explicitly specified, the specified value is used. If this parameter is omitted, the user roaming configuration of the current account is used.
        self.user_profile_switch = user_profile_switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_profile_size is not None:
            result['UserProfileSize'] = self.user_profile_size

        if self.user_profile_switch is not None:
            result['UserProfileSwitch'] = self.user_profile_switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserProfileSize') is not None:
            self.user_profile_size = m.get('UserProfileSize')

        if m.get('UserProfileSwitch') is not None:
            self.user_profile_switch = m.get('UserProfileSwitch')

        return self

class CreateBrowserInstanceGroupRequestSecurityPolicy(DaraModel):
    def __init__(
        self,
        skip_user_auth_check: bool = None,
    ):
        # Specifies whether to skip the user authorization check when connecting to the application.
        # - `true`: Skips the check.
        # - `false`: Performs the check.
        # If SecurityPolicy is configured but this field is omitted, the user authorization check is performed.
        # **Note:** This field cannot be used to skip OpenAPI authentication and RAM permission verification.
        self.skip_user_auth_check = skip_user_auth_check

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skip_user_auth_check is not None:
            result['SkipUserAuthCheck'] = self.skip_user_auth_check

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkipUserAuthCheck') is not None:
            self.skip_user_auth_check = m.get('SkipUserAuthCheck')

        return self

class CreateBrowserInstanceGroupRequestPolicy(DaraModel):
    def __init__(
        self,
        app_content_protection: str = None,
        authorize_access_policy_rules: List[main_models.CreateBrowserInstanceGroupRequestPolicyAuthorizeAccessPolicyRules] = None,
        client_types: List[main_models.CreateBrowserInstanceGroupRequestPolicyClientTypes] = None,
        clipboard_policy: main_models.CreateBrowserInstanceGroupRequestPolicyClipboardPolicy = None,
        disconnect_keep_session: str = None,
        disconnect_keep_session_time: int = None,
        file_manager: str = None,
        html_5file_transfer: str = None,
        multi_screen: str = None,
        no_operation_disconnect: str = None,
        no_operation_disconnect_time: int = None,
        policy_version: str = None,
        video_policy: main_models.CreateBrowserInstanceGroupRequestPolicyVideoPolicy = None,
        watermark_policy: main_models.CreateBrowserInstanceGroupRequestPolicyWatermarkPolicy = None,
    ):
        # The screen capture prevention switch.
        # 
        # - on: Enables screen capture prevention.
        # - off: Disables screen capture prevention.
        self.app_content_protection = app_content_protection
        # The client access IP address whitelist, which is used to restrict the source IP addresses of clients that can access the cloud browser.
        self.authorize_access_policy_rules = authorize_access_policy_rules
        # The client access control list.
        self.client_types = client_types
        # Specifies the clipboard transfer direction, content types, and size limits. read indicates transfer from the local PC to the cloud browser, and write indicates transfer from the cloud browser to the local PC.
        self.clipboard_policy = clipboard_policy
        # Specifies the data retention policy for sessions after disconnection.
        # 
        # - `customTime`: Retains the session according to the data retention policy. Custom duration through `DisconnectKeepSessionTime` is not supported.
        # - `persistent`: The session is not subject to automatic release based on disconnection duration.
        # 
        # **Note:** `persistent` is still subject to authorization and other release policies.
        self.disconnect_keep_session = disconnect_keep_session
        # This parameter is not supported and does not need to be specified.
        self.disconnect_keep_session_time = disconnect_keep_session_time
        # Specifies whether to enable the file manager floating button.
        # 
        # - `on`: Enabled.
        # - `off`: Disabled.
        # 
        # **Default value:** `off`.
        self.file_manager = file_manager
        # Specifies the file transfer policy for the web client.
        # 
        # - `off`: Prohibits file transfer.
        # - `upload`: Allows upload only.
        # - `download`: Allows download only.
        # - `full`: Allows both upload and download.
        # 
        # Configure this parameter in conjunction with the clipboard policy.
        self.html_5file_transfer = html_5file_transfer
        # Specifies whether to enable the dual-screen mode for the cloud browser.
        self.multi_screen = multi_screen
        # Specifies whether to enable automatic disconnection on inactivity. The value is not case-sensitive.
        # 
        # - `on`: Enabled.
        # - `off`: Disabled.
        # 
        # When enabled, use `NoOperationDisconnectTime` to set the idle timeout.
        self.no_operation_disconnect = no_operation_disconnect
        # Specifies the idle timeout in seconds before automatic disconnection is triggered.
        # 
        # **Prerequisite:** When `NoOperationDisconnect` is enabled, you must specify a value greater than 0.
        self.no_operation_disconnect_time = no_operation_disconnect_time
        # Specifies the policy version. The value is not case-sensitive.
        # 
        # - `DEFAULT`: Legacy policy.
        # - `CENTER`: Centralized policy.
        # 
        # **Default value:** `DEFAULT`. The effective policy version is subject to the policy configuration available for the account.
        self.policy_version = policy_version
        # Specifies the video display policy for the browser session.
        self.video_policy = video_policy
        # The watermark display configuration for browser sessions.
        self.watermark_policy = watermark_policy

    def validate(self):
        if self.authorize_access_policy_rules:
            for v1 in self.authorize_access_policy_rules:
                 if v1:
                    v1.validate()
        if self.client_types:
            for v1 in self.client_types:
                 if v1:
                    v1.validate()
        if self.clipboard_policy:
            self.clipboard_policy.validate()
        if self.video_policy:
            self.video_policy.validate()
        if self.watermark_policy:
            self.watermark_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_content_protection is not None:
            result['AppContentProtection'] = self.app_content_protection

        result['AuthorizeAccessPolicyRules'] = []
        if self.authorize_access_policy_rules is not None:
            for k1 in self.authorize_access_policy_rules:
                result['AuthorizeAccessPolicyRules'].append(k1.to_map() if k1 else None)

        result['ClientTypes'] = []
        if self.client_types is not None:
            for k1 in self.client_types:
                result['ClientTypes'].append(k1.to_map() if k1 else None)

        if self.clipboard_policy is not None:
            result['ClipboardPolicy'] = self.clipboard_policy.to_map()

        if self.disconnect_keep_session is not None:
            result['DisconnectKeepSession'] = self.disconnect_keep_session

        if self.disconnect_keep_session_time is not None:
            result['DisconnectKeepSessionTime'] = self.disconnect_keep_session_time

        if self.file_manager is not None:
            result['FileManager'] = self.file_manager

        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer

        if self.multi_screen is not None:
            result['MultiScreen'] = self.multi_screen

        if self.no_operation_disconnect is not None:
            result['NoOperationDisconnect'] = self.no_operation_disconnect

        if self.no_operation_disconnect_time is not None:
            result['NoOperationDisconnectTime'] = self.no_operation_disconnect_time

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        if self.video_policy is not None:
            result['VideoPolicy'] = self.video_policy.to_map()

        if self.watermark_policy is not None:
            result['WatermarkPolicy'] = self.watermark_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppContentProtection') is not None:
            self.app_content_protection = m.get('AppContentProtection')

        self.authorize_access_policy_rules = []
        if m.get('AuthorizeAccessPolicyRules') is not None:
            for k1 in m.get('AuthorizeAccessPolicyRules'):
                temp_model = main_models.CreateBrowserInstanceGroupRequestPolicyAuthorizeAccessPolicyRules()
                self.authorize_access_policy_rules.append(temp_model.from_map(k1))

        self.client_types = []
        if m.get('ClientTypes') is not None:
            for k1 in m.get('ClientTypes'):
                temp_model = main_models.CreateBrowserInstanceGroupRequestPolicyClientTypes()
                self.client_types.append(temp_model.from_map(k1))

        if m.get('ClipboardPolicy') is not None:
            temp_model = main_models.CreateBrowserInstanceGroupRequestPolicyClipboardPolicy()
            self.clipboard_policy = temp_model.from_map(m.get('ClipboardPolicy'))

        if m.get('DisconnectKeepSession') is not None:
            self.disconnect_keep_session = m.get('DisconnectKeepSession')

        if m.get('DisconnectKeepSessionTime') is not None:
            self.disconnect_keep_session_time = m.get('DisconnectKeepSessionTime')

        if m.get('FileManager') is not None:
            self.file_manager = m.get('FileManager')

        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')

        if m.get('MultiScreen') is not None:
            self.multi_screen = m.get('MultiScreen')

        if m.get('NoOperationDisconnect') is not None:
            self.no_operation_disconnect = m.get('NoOperationDisconnect')

        if m.get('NoOperationDisconnectTime') is not None:
            self.no_operation_disconnect_time = m.get('NoOperationDisconnectTime')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        if m.get('VideoPolicy') is not None:
            temp_model = main_models.CreateBrowserInstanceGroupRequestPolicyVideoPolicy()
            self.video_policy = temp_model.from_map(m.get('VideoPolicy'))

        if m.get('WatermarkPolicy') is not None:
            temp_model = main_models.CreateBrowserInstanceGroupRequestPolicyWatermarkPolicy()
            self.watermark_policy = temp_model.from_map(m.get('WatermarkPolicy'))

        return self

class CreateBrowserInstanceGroupRequestPolicyWatermarkPolicy(DaraModel):
    def __init__(
        self,
        watermark_switch: str = None,
        watermark_types: List[str] = None,
    ):
        # The watermark switch. The value is case-insensitive.
        # - `ON`: Enables the watermark.
        # - `OFF`: Disables the watermark.
        # The watermark content type list is not used when the watermark is disabled.
        self.watermark_switch = watermark_switch
        # The list of watermark content types.
        # - `EndUserId`: The user identifier.
        # - `InstanceGroupId`: The delivery group identifier.
        # - `ClientTime`: The current time of the client.
        # Use the watermark types supported by the browser and the client.
        self.watermark_types = watermark_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.watermark_switch is not None:
            result['WatermarkSwitch'] = self.watermark_switch

        if self.watermark_types is not None:
            result['WatermarkTypes'] = self.watermark_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatermarkSwitch') is not None:
            self.watermark_switch = m.get('WatermarkSwitch')

        if m.get('WatermarkTypes') is not None:
            self.watermark_types = m.get('WatermarkTypes')

        return self

class CreateBrowserInstanceGroupRequestPolicyVideoPolicy(DaraModel):
    def __init__(
        self,
        frame_rate: int = None,
    ):
        # Specifies the frame rate for the browser session.
        self.frame_rate = frame_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')

        return self

class CreateBrowserInstanceGroupRequestPolicyClipboardPolicy(DaraModel):
    def __init__(
        self,
        clipboard: str = None,
        clipboard_read_limit: int = None,
        clipboard_scope: str = None,
        clipboard_size_unit: str = None,
        clipboard_write_limit: int = None,
        file_clipboard: str = None,
        rich_text_clipboard: str = None,
        rich_text_clipboard_limit: int = None,
        rich_text_clipboard_read_limit: int = None,
        rich_text_clipboard_read_size_unit: str = None,
        rich_text_clipboard_size_unit: str = None,
        rich_text_clipboard_write_limit: int = None,
        rich_text_clipboard_write_size_unit: str = None,
        text_clipboard: str = None,
        text_clipboard_read_limit: int = None,
        text_clipboard_read_size_unit: str = None,
        text_clipboard_write_limit: int = None,
        text_clipboard_write_size_unit: str = None,
    ):
        # Specifies the clipboard transfer direction. The value is not case-sensitive.
        # 
        # - `off`: Prohibits bidirectional transfer.
        # - `read`: Allows copy and paste from the local PC to the cloud browser.
        # - `write`: Allows copy and paste from the cloud browser to the local PC.
        # - `readwrite`: Allows bidirectional copy and paste.
        self.clipboard = clipboard
        # Specifies the clipboard size limit for inbound transfer (from the local PC to the cloud browser).
        # 
        # **Value range:** 1 to 102400. The unit is specified by ClipboardSizeUnit.
        # 
        # This value range does not change with unit conversion.
        self.clipboard_read_limit = clipboard_read_limit
        # Specifies the clipboard control granularity.
        # 
        # - `global`: Unified control.
        # - `grained`: Separate control for text, rich text, and files.
        self.clipboard_scope = clipboard_scope
        # Specifies the clipboard size unit.
        # 
        # - `B`: Bytes.
        # - `KB`: 1024 bytes.
        self.clipboard_size_unit = clipboard_size_unit
        # Specifies the clipboard size limit for outbound transfer (from the cloud browser to the local PC).
        # 
        # **Value range:** 1 to 102400. The unit is specified by ClipboardSizeUnit.
        # 
        # This value range does not change with unit conversion.
        self.clipboard_write_limit = clipboard_write_limit
        # Specifies the clipboard transfer direction. The value is not case-sensitive.
        # 
        # - `off`: Prohibits bidirectional transfer.
        # - `read`: Allows copy and paste from the local PC to the cloud browser.
        # - `write`: Allows copy and paste from the cloud browser to the local PC.
        # - `readwrite`: Allows bidirectional copy and paste.
        self.file_clipboard = file_clipboard
        # Specifies the clipboard transfer direction. The value is not case-sensitive.
        # 
        # - `off`: Prohibits bidirectional transfer.
        # - `read`: Allows copy and paste from the local PC to the cloud browser.
        # - `write`: Allows copy and paste from the cloud browser to the local PC.
        # - `readwrite`: Allows bidirectional copy and paste.
        self.rich_text_clipboard = rich_text_clipboard
        # Specifies the clipboard size limit for rich text.
        # 
        # **Value range:** 1 to 204800. The unit is specified by RichTextClipboardSizeUnit.
        # 
        # This value range does not change with unit conversion.
        self.rich_text_clipboard_limit = rich_text_clipboard_limit
        # Specifies the clipboard size limit for inbound transfer (from the local PC to the cloud browser).
        # 
        # **Value range:** 1 to 204800. The unit is specified by RichTextClipboardReadSizeUnit.
        # 
        # This value range does not change with unit conversion.
        self.rich_text_clipboard_read_limit = rich_text_clipboard_read_limit
        # Specifies the clipboard size unit.
        # 
        # - `B`: Bytes.
        # - `KB`: 1024 bytes.
        # 
        # **Default value:** `KB`.
        self.rich_text_clipboard_read_size_unit = rich_text_clipboard_read_size_unit
        # Specifies the clipboard size unit.
        # 
        # - `B`: Bytes.
        # - `KB`: 1024 bytes.
        self.rich_text_clipboard_size_unit = rich_text_clipboard_size_unit
        # Specifies the clipboard size limit for outbound transfer (from the cloud browser to the local PC).
        # 
        # **Value range:** 1 to 204800. The unit is specified by RichTextClipboardWriteSizeUnit.
        # 
        # This value range does not change with unit conversion.
        self.rich_text_clipboard_write_limit = rich_text_clipboard_write_limit
        # Specifies the clipboard size unit.
        # 
        # - `B`: Bytes.
        # - `KB`: 1024 bytes.
        # 
        # **Default value:** `KB`.
        self.rich_text_clipboard_write_size_unit = rich_text_clipboard_write_size_unit
        # Specifies the clipboard transfer direction. The value is not case-sensitive.
        # 
        # - `off`: Prohibits bidirectional transfer.
        # - `read`: Allows copy and paste from the local PC to the cloud browser.
        # - `write`: Allows copy and paste from the cloud browser to the local PC.
        # - `readwrite`: Allows bidirectional copy and paste.
        self.text_clipboard = text_clipboard
        # Specifies the clipboard size limit for inbound transfer (from the local PC to the cloud browser).
        # 
        # **Value range:** 1 to 102400. The unit is specified by TextClipboardReadSizeUnit.
        # 
        # This value range does not change with unit conversion.
        self.text_clipboard_read_limit = text_clipboard_read_limit
        # Specifies the clipboard size unit.
        # 
        # - `B`: Bytes.
        # - `KB`: 1024 bytes.
        # 
        # **Default value:** `KB`.
        self.text_clipboard_read_size_unit = text_clipboard_read_size_unit
        # Specifies the clipboard size limit for outbound transfer (from the cloud browser to the local PC).
        # 
        # **Value range:** 1 to 102400. The unit is specified by TextClipboardWriteSizeUnit.
        # 
        # This value range does not change with unit conversion.
        self.text_clipboard_write_limit = text_clipboard_write_limit
        # Specifies the clipboard size unit.
        # 
        # - `B`: Bytes.
        # - `KB`: 1024 bytes.
        # 
        # **Default value:** `KB`.
        self.text_clipboard_write_size_unit = text_clipboard_write_size_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard

        if self.clipboard_read_limit is not None:
            result['ClipboardReadLimit'] = self.clipboard_read_limit

        if self.clipboard_scope is not None:
            result['ClipboardScope'] = self.clipboard_scope

        if self.clipboard_size_unit is not None:
            result['ClipboardSizeUnit'] = self.clipboard_size_unit

        if self.clipboard_write_limit is not None:
            result['ClipboardWriteLimit'] = self.clipboard_write_limit

        if self.file_clipboard is not None:
            result['FileClipboard'] = self.file_clipboard

        if self.rich_text_clipboard is not None:
            result['RichTextClipboard'] = self.rich_text_clipboard

        if self.rich_text_clipboard_limit is not None:
            result['RichTextClipboardLimit'] = self.rich_text_clipboard_limit

        if self.rich_text_clipboard_read_limit is not None:
            result['RichTextClipboardReadLimit'] = self.rich_text_clipboard_read_limit

        if self.rich_text_clipboard_read_size_unit is not None:
            result['RichTextClipboardReadSizeUnit'] = self.rich_text_clipboard_read_size_unit

        if self.rich_text_clipboard_size_unit is not None:
            result['RichTextClipboardSizeUnit'] = self.rich_text_clipboard_size_unit

        if self.rich_text_clipboard_write_limit is not None:
            result['RichTextClipboardWriteLimit'] = self.rich_text_clipboard_write_limit

        if self.rich_text_clipboard_write_size_unit is not None:
            result['RichTextClipboardWriteSizeUnit'] = self.rich_text_clipboard_write_size_unit

        if self.text_clipboard is not None:
            result['TextClipboard'] = self.text_clipboard

        if self.text_clipboard_read_limit is not None:
            result['TextClipboardReadLimit'] = self.text_clipboard_read_limit

        if self.text_clipboard_read_size_unit is not None:
            result['TextClipboardReadSizeUnit'] = self.text_clipboard_read_size_unit

        if self.text_clipboard_write_limit is not None:
            result['TextClipboardWriteLimit'] = self.text_clipboard_write_limit

        if self.text_clipboard_write_size_unit is not None:
            result['TextClipboardWriteSizeUnit'] = self.text_clipboard_write_size_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')

        if m.get('ClipboardReadLimit') is not None:
            self.clipboard_read_limit = m.get('ClipboardReadLimit')

        if m.get('ClipboardScope') is not None:
            self.clipboard_scope = m.get('ClipboardScope')

        if m.get('ClipboardSizeUnit') is not None:
            self.clipboard_size_unit = m.get('ClipboardSizeUnit')

        if m.get('ClipboardWriteLimit') is not None:
            self.clipboard_write_limit = m.get('ClipboardWriteLimit')

        if m.get('FileClipboard') is not None:
            self.file_clipboard = m.get('FileClipboard')

        if m.get('RichTextClipboard') is not None:
            self.rich_text_clipboard = m.get('RichTextClipboard')

        if m.get('RichTextClipboardLimit') is not None:
            self.rich_text_clipboard_limit = m.get('RichTextClipboardLimit')

        if m.get('RichTextClipboardReadLimit') is not None:
            self.rich_text_clipboard_read_limit = m.get('RichTextClipboardReadLimit')

        if m.get('RichTextClipboardReadSizeUnit') is not None:
            self.rich_text_clipboard_read_size_unit = m.get('RichTextClipboardReadSizeUnit')

        if m.get('RichTextClipboardSizeUnit') is not None:
            self.rich_text_clipboard_size_unit = m.get('RichTextClipboardSizeUnit')

        if m.get('RichTextClipboardWriteLimit') is not None:
            self.rich_text_clipboard_write_limit = m.get('RichTextClipboardWriteLimit')

        if m.get('RichTextClipboardWriteSizeUnit') is not None:
            self.rich_text_clipboard_write_size_unit = m.get('RichTextClipboardWriteSizeUnit')

        if m.get('TextClipboard') is not None:
            self.text_clipboard = m.get('TextClipboard')

        if m.get('TextClipboardReadLimit') is not None:
            self.text_clipboard_read_limit = m.get('TextClipboardReadLimit')

        if m.get('TextClipboardReadSizeUnit') is not None:
            self.text_clipboard_read_size_unit = m.get('TextClipboardReadSizeUnit')

        if m.get('TextClipboardWriteLimit') is not None:
            self.text_clipboard_write_limit = m.get('TextClipboardWriteLimit')

        if m.get('TextClipboardWriteSizeUnit') is not None:
            self.text_clipboard_write_size_unit = m.get('TextClipboardWriteSizeUnit')

        return self

class CreateBrowserInstanceGroupRequestPolicyClientTypes(DaraModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        # The type of the client for which you want to configure an access policy.
        # 
        # - windows: Windows client.
        # - macos: macOS client.
        # - html5: Web client.
        # - android: Android client.
        # - ios: iOS client.
        self.client_type = client_type
        # The access policy switch for the client type.
        # 
        # - on: Allows access from this type of client.
        # - off: Denies access from this type of client.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class CreateBrowserInstanceGroupRequestPolicyAuthorizeAccessPolicyRules(DaraModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
    ):
        # The source CIDR block of the client that is allowed to access the cloud browser. Use the CIDR format.
        self.cidr_ip = cidr_ip
        # The description of the client access IP address whitelist rule.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

class CreateBrowserInstanceGroupRequestNodePool(DaraModel):
    def __init__(
        self,
        node_amount: int = None,
        node_instance_type: str = None,
        strategy_type: str = None,
    ):
        # The number of nodes.
        # You do not need to specify this parameter.
        self.node_amount = node_amount
        # The identity of the node specifications.
        # 
        # You do not need to specify this parameter.
        self.node_instance_type = node_instance_type
        # The node scaling policy.
        # You do not need to specify this parameter.
        self.strategy_type = strategy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount

        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type

        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')

        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')

        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')

        return self

class CreateBrowserInstanceGroupRequestNetwork(DaraModel):
    def __init__(
        self,
        access_restriction: str = None,
        office_site_id: str = None,
        restricted_urls: List[main_models.CreateBrowserInstanceGroupRequestNetworkRestrictedURLs] = None,
        restricted_urls_file_path: str = None,
        v_switch_ids: List[str] = None,
    ):
        # The website access restriction mode.
        # 
        # - ALLOW_ALL: Allows access to all domain names.
        # - ALLOW_LIST: Allows access only to websites in the whitelist.
        self.access_restriction = access_restriction
        # The identifier of the created office network. The office network must belong to the current account and reside in the target region specified by BizRegionId. You can view the office network ID on the Network & Storage > Office Networks page in the Elastic Desktop Service Enterprise Edition console, or call the DescribeOfficeSites operation of Elastic Desktop Service Enterprise Edition to query the ID.
        self.office_site_id = office_site_id
        # The list of websites that are allowed for access. This parameter is used in ALLOW_LIST mode.
        # 
        # **Limits:**
        # 
        # - You can specify up to 20 URLs directly. To specify more than 20 URLs, use RestrictedURLsFilePath to import them from a file.
        # - This parameter cannot be specified together with RestrictedURLsFilePath.
        # - The URLs in the list cannot be duplicated.
        self.restricted_urls = restricted_urls
        # The path of the uploaded website whitelist file. This parameter is used in ALLOW_LIST mode.
        # 
        # If you need to specify more than 20 URLs, import them from a file. By default, you can configure up to 1,000 URLs.
        # 
        # This parameter cannot be specified together with RestrictedURLs.
        self.restricted_urls_file_path = restricted_urls_file_path
        # The list of vSwitch identifiers.
        # 
        # **Usage condition:** This parameter is required only when you use a custom office network. Do not specify this parameter for other types of office networks.
        # 
        # Select vSwitches that match the target business region and the custom office network.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.restricted_urls:
            for v1 in self.restricted_urls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_restriction is not None:
            result['AccessRestriction'] = self.access_restriction

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        result['RestrictedURLs'] = []
        if self.restricted_urls is not None:
            for k1 in self.restricted_urls:
                result['RestrictedURLs'].append(k1.to_map() if k1 else None)

        if self.restricted_urls_file_path is not None:
            result['RestrictedURLsFilePath'] = self.restricted_urls_file_path

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRestriction') is not None:
            self.access_restriction = m.get('AccessRestriction')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        self.restricted_urls = []
        if m.get('RestrictedURLs') is not None:
            for k1 in m.get('RestrictedURLs'):
                temp_model = main_models.CreateBrowserInstanceGroupRequestNetworkRestrictedURLs()
                self.restricted_urls.append(temp_model.from_map(k1))

        if m.get('RestrictedURLsFilePath') is not None:
            self.restricted_urls_file_path = m.get('RestrictedURLsFilePath')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

class CreateBrowserInstanceGroupRequestNetworkRestrictedURLs(DaraModel):
    def __init__(
        self,
        url: str = None,
    ):
        # The URL of the website that is allowed for access.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

class CreateBrowserInstanceGroupRequestBrowserConfig(DaraModel):
    def __init__(
        self,
        bookmarks: List[main_models.CreateBrowserInstanceGroupRequestBrowserConfigBookmarks] = None,
        bookmarks_file_path: str = None,
        browser_param: str = None,
        cookies_sync: bool = None,
        homepage: str = None,
    ):
        # The list of browser bookmarks.
        # **Limits:** This parameter cannot be specified together with a non-empty BookmarksFilePath parameter, and bookmark URLs cannot be duplicated.
        self.bookmarks = bookmarks
        # The path of the uploaded bookmark file. This parameter cannot be specified together with a non-empty Bookmarks parameter.
        # **File format:** A CSV file without a header. Specify the following four columns in order:
        # 1. Bookmark name.
        # 2. URL.
        # 3. Folder.
        # 4. Root directory type: `bookmark_bar` indicates the bookmarks bar, and `other` indicates other bookmarks.
        # **Limits:**
        # - Fields are separated by commas. Field content cannot contain commas or line breaks, and quote escaping is not supported.
        # - The file path must belong to the upload directory specified for the current account and cannot contain `..`.
        self.bookmarks_file_path = bookmarks_file_path
        # The browser startup parameters. For example, --incognito indicates that an incognito window is used.
        self.browser_param = browser_param
        # Specifies whether to synchronize cookies.
        self.cookies_sync = cookies_sync
        # The homepage URL opened when the browser starts. The URL must conform to the URI syntax.
        self.homepage = homepage

    def validate(self):
        if self.bookmarks:
            for v1 in self.bookmarks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bookmarks'] = []
        if self.bookmarks is not None:
            for k1 in self.bookmarks:
                result['Bookmarks'].append(k1.to_map() if k1 else None)

        if self.bookmarks_file_path is not None:
            result['BookmarksFilePath'] = self.bookmarks_file_path

        if self.browser_param is not None:
            result['BrowserParam'] = self.browser_param

        if self.cookies_sync is not None:
            result['CookiesSync'] = self.cookies_sync

        if self.homepage is not None:
            result['Homepage'] = self.homepage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bookmarks = []
        if m.get('Bookmarks') is not None:
            for k1 in m.get('Bookmarks'):
                temp_model = main_models.CreateBrowserInstanceGroupRequestBrowserConfigBookmarks()
                self.bookmarks.append(temp_model.from_map(k1))

        if m.get('BookmarksFilePath') is not None:
            self.bookmarks_file_path = m.get('BookmarksFilePath')

        if m.get('BrowserParam') is not None:
            self.browser_param = m.get('BrowserParam')

        if m.get('CookiesSync') is not None:
            self.cookies_sync = m.get('CookiesSync')

        if m.get('Homepage') is not None:
            self.homepage = m.get('Homepage')

        return self

class CreateBrowserInstanceGroupRequestBrowserConfigBookmarks(DaraModel):
    def __init__(
        self,
        bookmark_folder: str = None,
        bookmark_name: str = None,
        bookmark_url: str = None,
    ):
        # The folder where the bookmark is located. The length cannot exceed 64 characters after leading and trailing spaces are removed.
        self.bookmark_folder = bookmark_folder
        # The bookmark name. This parameter is required and cannot be empty when you create a bookmark. The length cannot exceed 64 characters after leading and trailing spaces are removed.
        # 
        # This parameter is required.
        self.bookmark_name = bookmark_name
        # The URL of the bookmark. This parameter is required when you create a bookmark. The length cannot exceed 1024 characters after leading and trailing spaces are removed.
        # 
        # This parameter is required.
        self.bookmark_url = bookmark_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bookmark_folder is not None:
            result['BookmarkFolder'] = self.bookmark_folder

        if self.bookmark_name is not None:
            result['BookmarkName'] = self.bookmark_name

        if self.bookmark_url is not None:
            result['BookmarkURL'] = self.bookmark_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BookmarkFolder') is not None:
            self.bookmark_folder = m.get('BookmarkFolder')

        if m.get('BookmarkName') is not None:
            self.bookmark_name = m.get('BookmarkName')

        if m.get('BookmarkURL') is not None:
            self.bookmark_url = m.get('BookmarkURL')

        return self

