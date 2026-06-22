# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PromotionParam(DaraModel):
    def __init__(
        self,
        product_code: str = None,
        promotion_option_code: str = None,
        promotion_option_no: str = None,
    ):
        self.product_code = product_code
        self.promotion_option_code = promotion_option_code
        self.promotion_option_no = promotion_option_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.promotion_option_code is not None:
            result['PromotionOptionCode'] = self.promotion_option_code

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        return self

