# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRCInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_use_coupon: bool = None,
        direction: str = None,
        dry_run: bool = None,
        instance_id: str = None,
        instance_type: str = None,
        promotion_code: str = None,
        reboot_time: str = None,
        reboot_when_finished: bool = None,
        region_id: str = None,
    ):
        # Specifies whether to enable the automatic payment feature. Valid values:
        # 
        # *   **true** (default): enables the feature. You must make sure that your account balance is sufficient.
        # *   **false**: disables the feature. An unpaid order is generated.
        # 
        # >  If your account balance is insufficient, you can set AutoPay to false. In this case, an unpaid order is generated. You can complete the payment in the Expenses and Costs console.
        self.auto_pay = auto_pay
        self.auto_use_coupon = auto_use_coupon
        # The type of the change that you want to perform on the instance. Valid values:
        # 
        # >  This parameter is optional. The system can automatically determine whether the instance change is an upgrade or a downgrade. If you want to specify this parameter, take note of the following items:
        # 
        # *   **Upgrade** (default): upgrades the instance type. Make sure that your account balance is sufficient.
        # *   **Down**: downgrades the instance type. If the new instance type specified by InstanceType has lower specifications than the current instance type, set Direction to Down.
        self.direction = direction
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, service limits, and resource inventory.
        # *   **false**: performs a dry run and performs the actual request. If the request passes the dry run, the operation is performed.
        self.dry_run = dry_run
        # The instance ID.
        self.instance_id = instance_id
        # The new instance type. For more information about the instance types that are supported by RDS Custom instances, see [Instance types of RDS Custom instances](https://help.aliyun.com/document_detail/2844823.html).
        self.instance_type = instance_type
        self.promotion_code = promotion_code
        self.reboot_time = reboot_time
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

