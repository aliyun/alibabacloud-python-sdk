# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceDiskTypeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: str = None,
        business_info: str = None,
        coupon_no: str = None,
        dbinstance_id: str = None,
        db_instance_storage_type: str = None,
        extra_param: str = None,
        order_type: str = None,
        provisioned_iops: int = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # - **true**: enables automatic payment. Make sure that your account has sufficient balance.
        # <props="china">- **false**: disables automatic payment. You can manually pay for the order in the console. Log on to the ApsaraDB for MongoDB console. In the upper-right corner of the page, choose **Expenses** > **Expenses and Costs**. In the left-side navigation pane, choose **Orders** > **My Orders**. On the **Orders** tab, find the target order and complete the payment.
        # <props="intl">- **false**: disables automatic payment. You can manually pay for the order in the console. Log on to the ApsaraDB for MongoDB console. In the upper-right corner of the page, choose **Expenses** > **Expenses and Costs**. In the left-side navigation pane, click **Order Management**. On the **Orders** page, find the target order and complete the payment.
        # 
        # Default value: **true**.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Valid values:
        # - **true**: enables auto-renewal.
        # - **false**: disables auto-renewal.
        # 
        # Default value: **false**.
        self.auto_renew = auto_renew
        # The additional parameter for business information.
        self.business_info = business_info
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The new disk type. Valid values:
        # - **cloud_auto**: ESSD AutoPL cloud disk.
        # 
        # > Prerequisite: The disk space of the instance must be at least 40 GB before you call this operation. If the disk space is insufficient, call ModifyDBInstanceSpec to expand the disk.
        self.db_instance_storage_type = db_instance_storage_type
        # The additional parameter.
        self.extra_param = extra_param
        # The specification change type. Valid values:
        # 
        # - **UPGRADE**: upgrades the configurations.
        # - **DOWNGRADE**: downgrades the configurations.
        # 
        # > This parameter is available only when the billing method of the instance is subscription.
        self.order_type = order_type
        # The provisioned performance (IOPS). Valid values: 0 to 50,000.
        # 
        # > If DbInstanceStorageType is set to cloud_auto, this parameter is conditionally required and can be set to 0. If this parameter is not specified, the API returns InvalidParameter.
        self.provisioned_iops = provisioned_iops
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.db_instance_storage_type is not None:
            result['DbInstanceStorageType'] = self.db_instance_storage_type

        if self.extra_param is not None:
            result['ExtraParam'] = self.extra_param

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DbInstanceStorageType') is not None:
            self.db_instance_storage_type = m.get('DbInstanceStorageType')

        if m.get('ExtraParam') is not None:
            self.extra_param = m.get('ExtraParam')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

