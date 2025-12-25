# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PromotionInfo(DaraModel):
    def __init__(
        self,
        can_prom_fee: str = None,
        is_selected: bool = None,
        promotion_desc: str = None,
        promotion_name: str = None,
        promotion_option_code: str = None,
        promotion_option_no: str = None,
        selected: bool = None,
    ):
        self.can_prom_fee = can_prom_fee
        self.is_selected = is_selected
        self.promotion_desc = promotion_desc
        self.promotion_name = promotion_name
        self.promotion_option_code = promotion_option_code
        self.promotion_option_no = promotion_option_no
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_prom_fee is not None:
            result['canPromFee'] = self.can_prom_fee

        if self.is_selected is not None:
            result['isSelected'] = self.is_selected

        if self.promotion_desc is not None:
            result['promotionDesc'] = self.promotion_desc

        if self.promotion_name is not None:
            result['promotionName'] = self.promotion_name

        if self.promotion_option_code is not None:
            result['promotionOptionCode'] = self.promotion_option_code

        if self.promotion_option_no is not None:
            result['promotionOptionNo'] = self.promotion_option_no

        if self.selected is not None:
            result['selected'] = self.selected

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('canPromFee') is not None:
            self.can_prom_fee = m.get('canPromFee')

        if m.get('isSelected') is not None:
            self.is_selected = m.get('isSelected')

        if m.get('promotionDesc') is not None:
            self.promotion_desc = m.get('promotionDesc')

        if m.get('promotionName') is not None:
            self.promotion_name = m.get('promotionName')

        if m.get('promotionOptionCode') is not None:
            self.promotion_option_code = m.get('promotionOptionCode')

        if m.get('promotionOptionNo') is not None:
            self.promotion_option_no = m.get('promotionOptionNo')

        if m.get('selected') is not None:
            self.selected = m.get('selected')

        return self

