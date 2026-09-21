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
        # The plan identifier.
        # 
        # Do not specify this parameter.
        self.app_package_type = app_package_type
        # Specifies whether to send authorization and deauthorization notification emails.
        # 
        # - `true`: Sends the notification.
        # - `false`: Does not send the notification.
        self.auth_notification_enabled = auth_notification_enabled
        # The automatic payment parameter.
        # 
        # Do not specify this parameter.
        self.auto_pay = auto_pay
        # The auto-renewal parameter.
        # 
        # Do not specify this parameter.
        self.auto_renew = auto_renew
        # The business region ID. This parameter is required.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The browser configuration.
        self.browser_config_shrink = browser_config_shrink
        # The resource billing mode.
        # 
        # **For MAU scenarios:** Set this parameter to `AppInstance` to bill by instance resource.
        self.charge_resource_mode = charge_resource_mode
        # The billing type.
        # 
        # **For MAU scenarios:** Set this parameter to `PostPaid`, which indicates pay-as-you-go billing.
        self.charge_type = charge_type
        # The name of the cloud browser group. This parameter cannot be empty. The name is used to distinguish different browser groups in business management scenarios.
        # 
        # This parameter is required.
        self.cloud_browser_name = cloud_browser_name
        # The image identifier used by the cloud browser. The image must be compatible with the operating system.
        # 
        # If this parameter is omitted, the default image available for the account is used. If no default image is available, the creation may fail.
        # 
        # **Usage condition:** When `CookiesSync` is enabled, explicitly specify an image that supports cookie synchronization.
        self.image_id = image_id
        # The instance type identifier. Select an instance type that matches the target region, operating system, and inventory conditions.
        # 
        # If this parameter is omitted, the default instance type is used.
        self.instance_type = instance_type
        # The capacity configuration for the MAU billing scenario.
        self.max_amount = max_amount
        # The office network and website access restriction configurations. The selected office network must belong to the current account and be located in the region specified by `BizRegionId`.
        self.network_shrink = network_shrink
        # The node pool configuration.
        # 
        # You do not need to specify this parameter.
        self.node_pool_shrink = node_pool_shrink
        # The operating system type. This parameter is required.
        # 
        # Only `Windows` is supported. Other operating systems are not supported.
        self.os_type = os_type
        # The number of subscription periods.
        # 
        # Do not specify this parameter.
        self.period = period
        # The unit of the subscription period.
        # 
        # Do not specify this parameter.
        self.period_unit = period_unit
        # The clipboard, video, watermark, session, and client access policy configurations.
        self.policy_shrink = policy_shrink
        # The promotion ID. Specifies the promotional campaign to apply to the order.
        # 
        # Whether the promotion is applicable depends on the campaign rules. Do not specify this parameter if no promotional campaign is used.
        self.promotion_id = promotion_id
        # The connection security policy for the browser group.
        self.security_policy_shrink = security_policy_shrink
        # The user data storage configuration for the browser group.
        self.storage_policy_shrink = storage_policy_shrink
        # The billing subtype.
        # 
        # **Set this parameter to `mau` explicitly, which indicates billing by monthly active users.** Omitting this field does not enable MAU billing.
        self.sub_pay_type = sub_pay_type
        # Not supported. You do not need to specify this parameter.
        self.tag_shrink = tag_shrink
        # Not supported. You do not need to specify this parameter.
        self.timers_shrink = timers_shrink
        # The list of authorized user group identifiers. A maximum of 10 items are supported. The user groups must belong to the current account and match the workspace network account type.
        # 
        # **Limit:** Cannot be specified together with a non-empty `Users`.
        self.user_group_ids = user_group_ids
        # The authorized user account information. The value must match the user and workspace network type.
        self.user_info_shrink = user_info_shrink
        # The list of authorized users. A maximum of 200 users can be specified. Users must be created in advance and must match the account type.
        # 
        # **Restriction:** This parameter cannot be specified together with a non-empty `UserGroupIds`.
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

