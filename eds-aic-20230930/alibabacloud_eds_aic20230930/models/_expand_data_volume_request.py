# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ExpandDataVolumeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        biz_region_id: str = None,
        node_ids: List[str] = None,
        phone_data_volume: int = None,
        promotion_id: str = None,
        share_data_volume: int = None,
    ):
        self.auto_pay = auto_pay
        self.biz_region_id = biz_region_id
        self.node_ids = node_ids
        self.phone_data_volume = phone_data_volume
        self.promotion_id = promotion_id
        self.share_data_volume = share_data_volume

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

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.phone_data_volume is not None:
            result['PhoneDataVolume'] = self.phone_data_volume

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.share_data_volume is not None:
            result['ShareDataVolume'] = self.share_data_volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('PhoneDataVolume') is not None:
            self.phone_data_volume = m.get('PhoneDataVolume')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('ShareDataVolume') is not None:
            self.share_data_volume = m.get('ShareDataVolume')

        return self

