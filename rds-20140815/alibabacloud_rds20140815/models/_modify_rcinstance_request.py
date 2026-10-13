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
        # - **true** (default): enables automatic payment. Make sure that your account balance is sufficient.
        # - **false**: generates an order without deducting fees.
        # > If your account balance is insufficient, you can set the AutoPay parameter to false. An unpaid order is generated. You can log on to the ApsaraDB RDS console to complete the payment.
        # >
        self.auto_pay = auto_pay
        # Specifies whether to automatically use coupons. Valid values:
        # * **true**: automatically uses coupons. This is the default value.
        # * **false**: does not automatically use coupons.
        # 
        # > If you use a coupon and then downgrade the instance type, the amount deducted by the voucher is not refunded.
        self.auto_use_coupon = auto_use_coupon
        self.business_info = business_info
        # The instance upgrade or downgrade type. Valid values:
        # > You do not need to specify this parameter. The system automatically determines whether to upgrade or downgrade the instance type. If you want to specify it, follow these rules:
        # - **Up** (default): upgrades the instance type. Make sure that your account balance is sufficient.
        # - **Down**: downgrades the instance type. When the instance type specified in InstanceType is lower than the current instance type, set Direction to Down.
        self.direction = direction
        # Specifies whether to perform a precheck on the instance creation operation. Valid values:
        # * **true**: performs a precheck without creating an instance. Check items include request parameters, request format, service limits, and inventory.
        # * **false**: sends a normal request and directly creates the instance after the request passes the precheck. This is the default value.
        self.dry_run = dry_run
        # The instance ID.
        self.instance_id = instance_id
        # The destination instance type. For more information about the instance types supported by RDS Target instances, see [RDS Target instance types](https://help.aliyun.com/document_detail/2844823.html).
        self.instance_type = instance_type
        # The coupon code.
        self.promotion_code = promotion_code
        # The restart time of the instance.
        # 
        # - If **RebootWhenFinished** is set to **false** and the instance is in the **Running** state, you **must** specify a restart time within 48 hours.
        # - Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mmZ` format. The time must be in UTC.
        self.reboot_time = reboot_time
        # Specifies whether to immediately restart the instance after the instance type change is complete. Valid values:
        # 
        # - **true**: restarts the instance immediately. This is the default value.
        # - **false**: does not restart the instance immediately.
        # 
        # > If the instance is in the **Stopped** state, it remains in the Stopped state and is not restarted even if you set RebootWhenFinished to true.
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

