# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRCInstanceChargeTypeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: str = None,
        auto_use_coupon: bool = None,
        business_info: str = None,
        client_token: str = None,
        dry_run: bool = None,
        include_data_disks: bool = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_ids: str = None,
        pay_type: str = None,
        period: str = None,
        promotion_code: str = None,
        region_id: str = None,
        used_time: int = None,
    ):
        # The reserved parameter. This parameter is not supported.
        self.auto_pay = auto_pay
        # Specifies whether to enable the auto-renewal feature. Valid values:
        # * **true**
        # * **false**
        # > *   This parameter is valid only when you change the billing method from pay-as-you-go to subscription.
        # > *   All strings except **true** are considered **false**.
        self.auto_renew = auto_renew
        # Specifies whether to use a coupon. Valid values:
        # * **true** (default)
        # * **false**
        self.auto_use_coupon = auto_use_coupon
        # The additional business information about the instance.
        self.business_info = business_info
        # The custom client token that is used to ensure the idempotence of the request.
        # > The value can contain ASCII characters and can be up to 64 characters in length.
        self.client_token = client_token
        # The reserved parameter. This parameter is not supported.
        self.dry_run = dry_run
        # The reserved parameter. This parameter is not supported.
        self.include_data_disks = include_data_disks
        # The reserved parameter. This parameter is not supported.
        self.instance_charge_type = instance_charge_type
        # The ID of the instance or disk.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The reserved parameter. This parameter is not supported.
        self.instance_ids = instance_ids
        # The new billing method of the instance. Valid values:
        # * **Prepaid**: subscription.
        # * **Postpaid**: pay-as-you-go.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The renewal cycle of the instance. Valid values:
        # * **Year**
        # * **Month**
        # > This parameter must be specified if you set the PayType parameter to **Prepaid**.
        self.period = period
        # The coupon code.
        self.promotion_code = promotion_code
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The subscription duration of the instance.
        # *   If you set the **Period** parameter to **Year**, the value of the **UsedTime** parameter ranges from **1** to **5**.
        # *   If the **Period** parameter is set to **Month**, the value of the **UsedTime** parameter ranges from **1** to **11**.
        # 
        # > If you set the **PayType** parameter to **Prepaid**, you must specify this parameter.
        self.used_time = used_time

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

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.include_data_disks is not None:
            result['IncludeDataDisks'] = self.include_data_disks

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('BusinessInfo') is not None:
            self.business_info = m.get('BusinessInfo')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('IncludeDataDisks') is not None:
            self.include_data_disks = m.get('IncludeDataDisks')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

