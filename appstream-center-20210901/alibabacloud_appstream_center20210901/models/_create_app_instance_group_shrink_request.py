# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateAppInstanceGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_name: str = None,
        app_package_type: str = None,
        app_policy_id: str = None,
        auth_mode: str = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        charge_resource_mode: str = None,
        charge_type: str = None,
        cluster_id: str = None,
        network_shrink: str = None,
        node_pool_shrink: str = None,
        period: int = None,
        period_unit: str = None,
        pre_open_app_id: str = None,
        product_type: str = None,
        promotion_id: str = None,
        runtime_policy_shrink: str = None,
        security_policy_shrink: str = None,
        session_timeout: int = None,
        storage_policy_shrink: str = None,
        sub_pay_type: str = None,
        user_define_policy_shrink: str = None,
        user_group_ids: List[str] = None,
        user_info_shrink: str = None,
        users: List[str] = None,
        video_policy_shrink: str = None,
    ):
        # The image ID of the application. To obtain the image ID, log on to the [App Streaming console](https://appstreaming.console.aliyun.com/). In the left-side navigation pane, choose **Maintenance** > **Custom Images** or Maintenance > **System Images**.
        # 
        # This parameter is required.
        self.app_center_image_id = app_center_image_id
        # The name of the delivery group.
        self.app_instance_group_name = app_instance_group_name
        # Package type.
        self.app_package_type = app_package_type
        # Policy ID.
        self.app_policy_id = app_policy_id
        # The authentication mode of the delivery group.
        self.auth_mode = auth_mode
        # Specifies whether to enable automatic payment.
        # 
        # Valid values:
        # 
        # *   true
        # *   false: manual payment. This is the default value.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal.
        # 
        # Valid values:
        # 
        # *   true
        # *   false: manual payment. This is the default value.
        self.auto_renew = auto_renew
        # The ID of the region where the delivery group resides. For information about the supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        # 
        # Valid values:
        # 
        # *   cn-shanghai: China (Shanghai)
        # *   cn-hangzhou: China (Hangzhou)
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The sales mode.
        # 
        # Valid value:
        # 
        # *   Node: by resource
        # 
        # This parameter is required.
        self.charge_resource_mode = charge_resource_mode
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go
        # *   PrePaid: subscription
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # Cluster ID.
        self.cluster_id = cluster_id
        # The network settings.
        # 
        # >  If you want to use this parameter, submit a ticket.
        self.network_shrink = network_shrink
        # The node pool object.
        self.node_pool_shrink = node_pool_shrink
        # The subscription duration of resources. This parameter is required if you set `ChargeType` to `PrePaid`. The unit of this parameter is specified by `PeriodUnit`.
        # 
        # *   Valid value if you set `PeriodUnit` to `Week`:
        # 
        #     *   1
        # 
        # *   Valid values if you set `PeriodUnit` to `Month`:
        # 
        #     *   1
        #     *   2
        #     *   3
        #     *   6
        # 
        # *   Valid values if you set `PeriodUnit` to `Year`:
        # 
        #     *   1
        #     *   2
        #     *   3
        # 
        # >  If you set `ChargeType` to `PostPaid`, set this parameter to 1.
        # 
        # This parameter is required.
        self.period = period
        # The unit of the subscription duration. This parameter is available if you set `ChargeType` to `PrePaid`.
        # 
        # >  The value of this parameter is case-insensitive. For example, `Week` is valid and `week` is invalid. If you specify an invalid value combination for Period and PeriodUnit, such as `2 Week`, the operation can still be called. However, an error occurs when you place the order.
        # 
        # >  If you set `ChargeType` to `PostPaid`, set this parameter to `Month`.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        # *   Week
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The ID of the pre-open application.
        self.pre_open_app_id = pre_open_app_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type
        # The promotion ID. You can call the [GetResourcePrice](https://help.aliyun.com/document_detail/428503.html) operation to obtain the ID.
        self.promotion_id = promotion_id
        # The runtime policy.
        self.runtime_policy_shrink = runtime_policy_shrink
        # The security policy.
        self.security_policy_shrink = security_policy_shrink
        # The period of time during which the application can be recycled. The recycling period is the period of time between the time when the end user disconnects from the application and the time when processes exit the application. If you do not want to recycle the application, set this parameter to `-1`. Valid values:-1 and 3 to 300. The value must be an integer. Default value: `15`. Unit: minutes.
        # 
        # This parameter is required.
        self.session_timeout = session_timeout
        # The storage policy.
        self.storage_policy_shrink = storage_policy_shrink
        # Payment method subtype.
        self.sub_pay_type = sub_pay_type
        # The custom policy.
        self.user_define_policy_shrink = user_define_policy_shrink
        # List of authorized user group IDs.
        self.user_group_ids = user_group_ids
        # The information about the user that you want to add to the assigned user list of the delivery group. This parameter is required if you configure `Users`.
        self.user_info_shrink = user_info_shrink
        # The users that you want to add to the assigned user list of the delivery group.
        self.users = users
        # Display policy.
        self.video_policy_shrink = video_policy_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.app_package_type is not None:
            result['AppPackageType'] = self.app_package_type

        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id

        if self.auth_mode is not None:
            result['AuthMode'] = self.auth_mode

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.network_shrink is not None:
            result['Network'] = self.network_shrink

        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.runtime_policy_shrink is not None:
            result['RuntimePolicy'] = self.runtime_policy_shrink

        if self.security_policy_shrink is not None:
            result['SecurityPolicy'] = self.security_policy_shrink

        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout

        if self.storage_policy_shrink is not None:
            result['StoragePolicy'] = self.storage_policy_shrink

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        if self.user_define_policy_shrink is not None:
            result['UserDefinePolicy'] = self.user_define_policy_shrink

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        if self.users is not None:
            result['Users'] = self.users

        if self.video_policy_shrink is not None:
            result['VideoPolicy'] = self.video_policy_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('AppPackageType') is not None:
            self.app_package_type = m.get('AppPackageType')

        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')

        if m.get('AuthMode') is not None:
            self.auth_mode = m.get('AuthMode')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Network') is not None:
            self.network_shrink = m.get('Network')

        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RuntimePolicy') is not None:
            self.runtime_policy_shrink = m.get('RuntimePolicy')

        if m.get('SecurityPolicy') is not None:
            self.security_policy_shrink = m.get('SecurityPolicy')

        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')

        if m.get('StoragePolicy') is not None:
            self.storage_policy_shrink = m.get('StoragePolicy')

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        if m.get('UserDefinePolicy') is not None:
            self.user_define_policy_shrink = m.get('UserDefinePolicy')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        if m.get('VideoPolicy') is not None:
            self.video_policy_shrink = m.get('VideoPolicy')

        return self

