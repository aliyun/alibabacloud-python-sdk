# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PromotionInfo(DaraModel):
    def __init__(
        self,
        can_prom_fee: str = None,
        is_selected: str = None,
        promotion_desc: str = None,
        promotion_name: str = None,
        promotion_option_code: str = None,
        promotion_option_no: str = None,
    ):
        self.can_prom_fee = can_prom_fee
        self.is_selected = is_selected
        self.promotion_desc = promotion_desc
        self.promotion_name = promotion_name
        self.promotion_option_code = promotion_option_code
        self.promotion_option_no = promotion_option_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_prom_fee is not None:
            result['CanPromFee'] = self.can_prom_fee

        if self.is_selected is not None:
            result['IsSelected'] = self.is_selected

        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc

        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name

        if self.promotion_option_code is not None:
            result['PromotionOptionCode'] = self.promotion_option_code

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanPromFee') is not None:
            self.can_prom_fee = m.get('CanPromFee')

        if m.get('IsSelected') is not None:
            self.is_selected = m.get('IsSelected')

        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')

        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')

        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        return self

