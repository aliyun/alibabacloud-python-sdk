# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateBrowserInstanceGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        app_package_type: str = None,
        auth_notification_enabled: bool = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        browser_config_shrink: str = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        cloud_browser_name: str = None,
        image_id: str = None,
        instance_type: str = None,
        max_amount: int = None,
        network_shrink: str = None,
        node_pool_shrink: str = None,
        os_type: str = None,
        period: int = None,
        period_unit: str = None,
        policy_shrink: str = None,
        promotion_id: str = None,
        security_policy_shrink: str = None,
        storage_policy_shrink: str = None,
        sub_pay_type: str = None,
        tag_shrink: str = None,
        timers_shrink: str = None,
        user_group_ids: List[str] = None,
        user_info_shrink: str = None,
        users_shrink: str = None,
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
        self.browser_config_shrink = browser_config_shrink
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
        self.network_shrink = network_shrink
        # The node pool configuration.
        # You do not need to specify this parameter.
        self.node_pool_shrink = node_pool_shrink
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
        self.policy_shrink = policy_shrink
        # The promotion identifier, which is used to specify the promotional offer applied to the order.
        # 
        # Applicability and specific discounts are subject to the promotion rules. You do not need to specify this parameter if no promotional offer is applied.
        self.promotion_id = promotion_id
        # The connection security policy of the browser group.
        self.security_policy_shrink = security_policy_shrink
        # The user data storage configuration of the browser group.
        self.storage_policy_shrink = storage_policy_shrink
        # The billing sub-type.
        # 
        # **You must explicitly set this parameter to mau, which indicates billing by monthly active users (MAUs).** Omitting this parameter does not enable MAU billing.
        self.sub_pay_type = sub_pay_type
        # This parameter is not supported and does not need to be specified.
        self.tag_shrink = tag_shrink
        # This parameter is not supported and does not need to be specified.
        self.timers_shrink = timers_shrink
        # The list of authorized user group IDs. You can specify up to 10 IDs. The user groups must belong to the current account and match the account type of the office network.
        # **Limits:** This parameter cannot be specified together with a non-empty Users parameter.
        self.user_group_ids = user_group_ids
        # The authorized user account information. The information must match the user and office network types.
        self.user_info_shrink = user_info_shrink
        # The list of authorized users. You can specify up to 200 users. The users must be created in advance and match the account type.
        # 
        # **Limit:** This parameter cannot be specified together with a non-empty UserGroupIds parameter.
        self.users_shrink = users_shrink

    def validate(self):
        pass

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

        if self.browser_config_shrink is not None:
            result['BrowserConfig'] = self.browser_config_shrink

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

        if self.network_shrink is not None:
            result['Network'] = self.network_shrink

        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.policy_shrink is not None:
            result['Policy'] = self.policy_shrink

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.security_policy_shrink is not None:
            result['SecurityPolicy'] = self.security_policy_shrink

        if self.storage_policy_shrink is not None:
            result['StoragePolicy'] = self.storage_policy_shrink

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        if self.timers_shrink is not None:
            result['Timers'] = self.timers_shrink

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        if self.users_shrink is not None:
            result['Users'] = self.users_shrink

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
            self.browser_config_shrink = m.get('BrowserConfig')

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
            self.network_shrink = m.get('Network')

        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('Policy') is not None:
            self.policy_shrink = m.get('Policy')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('SecurityPolicy') is not None:
            self.security_policy_shrink = m.get('SecurityPolicy')

        if m.get('StoragePolicy') is not None:
            self.storage_policy_shrink = m.get('StoragePolicy')

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        if m.get('Timers') is not None:
            self.timers_shrink = m.get('Timers')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        if m.get('Users') is not None:
            self.users_shrink = m.get('Users')

        return self

