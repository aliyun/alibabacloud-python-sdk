# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ExpandPhoneDataVolumeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        biz_region_id: str = None,
        instance_ids: List[str] = None,
        paid_call_back_url: str = None,
        phone_data_volume: int = None,
        promotion_id: str = None,
    ):
        # Specifies whether to enable automatic payment. Default value: false.
        self.auto_pay = auto_pay
        # The region ID.
        self.biz_region_id = biz_region_id
        # The IDs of the cloud phone matrix instances. You can specify 1 to 100 instance IDs.
        self.instance_ids = instance_ids
        # The redirect URL to the payment success page.
        self.paid_call_back_url = paid_call_back_url
        # The expected size of the independent device storage after the expansion. Unit: GiB.>Notice: The new value must be greater than the original independent device storage size of the instance.
        self.phone_data_volume = phone_data_volume
        # The promotion ID.
        self.promotion_id = promotion_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.paid_call_back_url is not None:
            result['PaidCallBackUrl'] = self.paid_call_back_url

        if self.phone_data_volume is not None:
            result['PhoneDataVolume'] = self.phone_data_volume

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PaidCallBackUrl') is not None:
            self.paid_call_back_url = m.get('PaidCallBackUrl')

        if m.get('PhoneDataVolume') is not None:
            self.phone_data_volume = m.get('PhoneDataVolume')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

