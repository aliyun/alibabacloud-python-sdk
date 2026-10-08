# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRCInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_use_coupon: bool = None,
        business_info: str = None,
        direction: str = None,
        dry_run: bool = None,
        instance_id: str = None,
        instance_type: str = None,
        promotion_code: str = None,
        reboot_time: str = None,
        reboot_when_finished: bool = None,
        region_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # - **true** (default): Automatic payment is enabled. Make sure that your account balance is sufficient.
        # - **false**: An order is generated but payment is not automatically made.
        # > If your payment method balance is insufficient, set the parameter AutoPay to false. An unpaid order is generated, and you can log on to the ApsaraDB RDS console to complete the payment.
        # >
        self.auto_pay = auto_pay
        # Specifies whether to automatically use coupons. Valid values:
        # * **true** (default): Coupons are automatically used.
        # * **false**: Coupons are not used.
        # 
        # > If you use coupons and then perform a downgrade, the amount deducted by coupons is not refunded.
        self.auto_use_coupon = auto_use_coupon
        self.business_info = business_info
        # The type of the Upgrade/Downgrade. Valid values:
        # > This parameter does not need to be uploaded. The system can automatically determine whether the change is an upgrade or a downgrade. If you upload this parameter, follow the rules below.
        # - **Up** (default): Upgrades the instance type. Make sure that your account payment method balance is sufficient.
        # - **Down**: Downgrades the instance type. Set Direction to down when the instance type specified by InstanceType is lower than the current instance type.
        self.direction = direction
        # Specifies whether to perform a dry run. Valid values:
        # * **true**: Performs a dry run without creating the instance. The system checks items such as the request parameters, request format, service limits, and available resources.
        # * **false** (default): Sends the request. If the request passes the check, the instance is created.
        self.dry_run = dry_run
        # The instance ID.
        self.instance_id = instance_id
        # The target instance type. For information about the instance types supported by RDS Custom instances, see [RDS Custom instance types](https://help.aliyun.com/document_detail/2844823.html).
        self.instance_type = instance_type
        # The coupon code.
        self.promotion_code = promotion_code
        # The restart time of the instance.
        # 
        # - If **RebootWhenFinished** is set to **false** and the instance status is **Running**, you **must** set a restart time within 48 hours.
        # - The time follows the ISO 8601 standard in UTC+0. Format: `yyyy-MM-ddTHH:mmZ`.
        self.reboot_time = reboot_time
        # Specifies whether to immediately restart the instance after the specification change is complete. Valid values:
        # 
        # - **true** (default): The instance is restarted immediately.
        # - **false**: The instance is not restarted.
        # 
        # > If the instance is in the **Stopped** state, the instance remains in the Stopped state and is not restarted even if you set `RebootWhenFinished=true`.
        self.reboot_when_finished = reboot_when_finished
        # The region ID of the instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.reboot_time is not None:
            result['RebootTime'] = self.reboot_time

        if self.reboot_when_finished is not None:
            result['RebootWhenFinished'] = self.reboot_when_finished

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('RebootTime') is not None:
            self.reboot_time = m.get('RebootTime')

        if m.get('RebootWhenFinished') is not None:
            self.reboot_when_finished = m.get('RebootWhenFinished')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

