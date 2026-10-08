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
        # Reserved parameter. Not supported.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # * **true**: Enabled (default).
        # * **false**: Disabled.
        # 
        # > * This parameter takes effect only when you switch from pay-as-you-go to subscription.
        # > * All non-**true** strings are treated as **false**.
        self.auto_renew = auto_renew
        # Specifies whether to use coupons. Valid values:
        # * **true** (default): Coupons are used.
        # * **false**: Coupons are not used.
        self.auto_use_coupon = auto_use_coupon
        # The business extension parameter.
        self.business_info = business_info
        # The custom token that is used to ensure the idempotence of the request. 
        # > The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Reserved parameter. Not supported.
        self.dry_run = dry_run
        # Reserved parameter. Not supported.
        self.include_data_disks = include_data_disks
        # Reserved parameter. Not supported.
        self.instance_charge_type = instance_charge_type
        # The instance ID or cloud disk ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Reserved parameter. Not supported.
        self.instance_ids = instance_ids
        # The billing method of the instance after the change. Valid values:
        # * **Prepaid**: subscription.
        # * **Postpaid**: pay-as-you-go.
        self.pay_type = pay_type
        # The unit of the subscription duration. Valid values:
        # * **Year**: yearly subscription.
        # * **Month**: monthly subscription.
        # 
        # > This parameter is required if **PayType** is set to **Prepaid**.
        self.period = period
        # The coupon code.
        self.promotion_code = promotion_code
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The subscription duration. Valid values:
        # * If **Period** is set to **Year**, the valid values of UsedTime are **1 to 5**.
        # * If **Period** is set to **Month**, the valid values of UsedTime are **1 to 11**.
        # 
        # > This parameter is required if PayType is set to **Prepaid**.
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

