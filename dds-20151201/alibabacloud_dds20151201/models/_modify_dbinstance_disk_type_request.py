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
        # 
        # *   **true**: enables automatic payment. Make sure that you have sufficient balance within your account.
        # *   **false**: disables automatic payment. You must perform the following operations to pay for the instance: Log on to the ApsaraDB for MongoDB console. In the upper-right corner, click **Expenses** and select **User Center** from the drop-down list. The User Center page appears. In the left-side navigation pane, choose **Order Management** > Renew. On the Renewal tab, find the bill that you want to pay and then click Renew in the Actions column.
        # 
        # Default value: **true**.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # Default value: **false**.
        self.auto_renew = auto_renew
        # The business information. This is an additional parameter.
        self.business_info = business_info
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The new disk type. Valid values:
        # 
        # *   **cloud_auto**: ESSD AutoPL disk
        # *   **cloud_essd1**: PL1 ESSD
        # *   **cloud_essd2**: PL2 ESSD
        # *   **cloud_essd3**: PL3 ESSD
        self.db_instance_storage_type = db_instance_storage_type
        # An additional parameter.
        self.extra_param = extra_param
        # The type of configuration changes. Valid values:
        # 
        # *   **UPGRADE**
        # *   **DOWNGRADE**
        # 
        # >  This parameter is valid only when the billing method of the instance is subscription.
        self.order_type = order_type
        # The provisioned IOPS. Valid values: 0 to 50000.
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

