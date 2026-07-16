# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyDesktopChargeTypeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        charge_type: str = None,
        desktop_id: List[str] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
        use_duration: int = None,
    ):
        # Specifies whether to enable automatic payment.
        self.auto_pay = auto_pay
        # The new billing method.
        self.charge_type = charge_type
        # The IDs of the cloud desktops. You can specify 1 to 20 IDs.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The subscription duration. This parameter is required only when you set the `ChargeType` parameter to `PrePaid`. The unit of the duration is specified by the `PeriodUnit` parameter.
        # 
        # - If you set the `PeriodUnit` parameter to `Week`, you can set this parameter only to 1.
        # 
        # - If you set the `PeriodUnit` parameter to `Month`, you can set this parameter to 1, 2, 3, or 6.
        # 
        # - If you set the `PeriodUnit` parameter to `Year`, you can set this parameter to 1, 2, 3, 4, or 5.
        self.period = period
        # The unit of the subscription duration.
        self.period_unit = period_unit
        # The promotion ID.
        self.promotion_id = promotion_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.reseller_owner_uid = reseller_owner_uid
        # > This parameter is in invitational preview and is not publicly available.
        self.use_duration = use_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        if self.use_duration is not None:
            result['UseDuration'] = self.use_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        if m.get('UseDuration') is not None:
            self.use_duration = m.get('UseDuration')

        return self

