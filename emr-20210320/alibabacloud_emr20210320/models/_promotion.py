# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Promotion(DaraModel):
    def __init__(
        self,
        product_code: str = None,
        promotion_desc: str = None,
        promotion_name: str = None,
        promotion_option_code: str = None,
        promotion_option_no: str = None,
    ):
        # 产品码。
        self.product_code = product_code
        # 优惠券描述。
        self.promotion_desc = promotion_desc
        # 优惠券名称。
        self.promotion_name = promotion_name
        # 优惠券码。
        self.promotion_option_code = promotion_option_code
        # 优惠券号。
        # 
        # This parameter is required.
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
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')

        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')

        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        return self

