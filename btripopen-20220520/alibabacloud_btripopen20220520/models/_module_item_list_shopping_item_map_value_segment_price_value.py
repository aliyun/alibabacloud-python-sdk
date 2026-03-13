# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class ModuleItemListShoppingItemMapValueSegmentPriceValue(DaraModel):
    def __init__(
        self,
        floor_price: int = None,
        ticket_price: int = None,
        sell_price: int = None,
        original_sell_price: int = None,
        base_total_price: int = None,
        before_control_price: int = None,
        tax: int = None,
        supply_price: int = None,
        basic_cabin_price: int = None,
        build_price: int = None,
        oil_price: int = None,
        first_standard_price: int = None,
        business_standard_price: int = None,
        common_standard_price: int = None,
        inter_ticket_price: int = None,
        subtracted_price: int = None,
        origin_common_price: int = None,
        dynamic_promotion_price: int = None,
        installment_num: int = None,
        installment_price: float = None,
        competition_dynamic_price: int = None,
        competition_promotion_price: int = None,
        min_before_control_price_of_normal: int = None,
        price_show_info: main_models.ModuleItemListShoppingItemMapValueSegmentPriceValuePriceShowInfo = None,
    ):
        self.floor_price = floor_price
        self.ticket_price = ticket_price
        self.sell_price = sell_price
        self.original_sell_price = original_sell_price
        self.base_total_price = base_total_price
        self.before_control_price = before_control_price
        self.tax = tax
        self.supply_price = supply_price
        self.basic_cabin_price = basic_cabin_price
        self.build_price = build_price
        self.oil_price = oil_price
        self.first_standard_price = first_standard_price
        self.business_standard_price = business_standard_price
        self.common_standard_price = common_standard_price
        # fdPrice
        self.inter_ticket_price = inter_ticket_price
        self.subtracted_price = subtracted_price
        self.origin_common_price = origin_common_price
        self.dynamic_promotion_price = dynamic_promotion_price
        self.installment_num = installment_num
        self.installment_price = installment_price
        self.competition_dynamic_price = competition_dynamic_price
        self.competition_promotion_price = competition_promotion_price
        self.min_before_control_price_of_normal = min_before_control_price_of_normal
        self.price_show_info = price_show_info

    def validate(self):
        if self.price_show_info:
            self.price_show_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.floor_price is not None:
            result['floor_price'] = self.floor_price

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.sell_price is not None:
            result['sell_price'] = self.sell_price

        if self.original_sell_price is not None:
            result['original_sell_price'] = self.original_sell_price

        if self.base_total_price is not None:
            result['base_total_price'] = self.base_total_price

        if self.before_control_price is not None:
            result['before_control_price'] = self.before_control_price

        if self.tax is not None:
            result['tax'] = self.tax

        if self.supply_price is not None:
            result['supply_price'] = self.supply_price

        if self.basic_cabin_price is not None:
            result['basic_cabin_price'] = self.basic_cabin_price

        if self.build_price is not None:
            result['build_price'] = self.build_price

        if self.oil_price is not None:
            result['oil_price'] = self.oil_price

        if self.first_standard_price is not None:
            result['first_standard_price'] = self.first_standard_price

        if self.business_standard_price is not None:
            result['business_standard_price'] = self.business_standard_price

        if self.common_standard_price is not None:
            result['common_standard_price'] = self.common_standard_price

        if self.inter_ticket_price is not None:
            result['inter_ticket_price'] = self.inter_ticket_price

        if self.subtracted_price is not None:
            result['subtracted_price'] = self.subtracted_price

        if self.origin_common_price is not None:
            result['origin_common_price'] = self.origin_common_price

        if self.dynamic_promotion_price is not None:
            result['dynamic_promotion_price'] = self.dynamic_promotion_price

        if self.installment_num is not None:
            result['installment_num'] = self.installment_num

        if self.installment_price is not None:
            result['installment_price'] = self.installment_price

        if self.competition_dynamic_price is not None:
            result['competition_dynamic_price'] = self.competition_dynamic_price

        if self.competition_promotion_price is not None:
            result['competition_promotion_price'] = self.competition_promotion_price

        if self.min_before_control_price_of_normal is not None:
            result['min_before_control_price_of_normal'] = self.min_before_control_price_of_normal

        if self.price_show_info is not None:
            result['price_show_info'] = self.price_show_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('floor_price') is not None:
            self.floor_price = m.get('floor_price')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('sell_price') is not None:
            self.sell_price = m.get('sell_price')

        if m.get('original_sell_price') is not None:
            self.original_sell_price = m.get('original_sell_price')

        if m.get('base_total_price') is not None:
            self.base_total_price = m.get('base_total_price')

        if m.get('before_control_price') is not None:
            self.before_control_price = m.get('before_control_price')

        if m.get('tax') is not None:
            self.tax = m.get('tax')

        if m.get('supply_price') is not None:
            self.supply_price = m.get('supply_price')

        if m.get('basic_cabin_price') is not None:
            self.basic_cabin_price = m.get('basic_cabin_price')

        if m.get('build_price') is not None:
            self.build_price = m.get('build_price')

        if m.get('oil_price') is not None:
            self.oil_price = m.get('oil_price')

        if m.get('first_standard_price') is not None:
            self.first_standard_price = m.get('first_standard_price')

        if m.get('business_standard_price') is not None:
            self.business_standard_price = m.get('business_standard_price')

        if m.get('common_standard_price') is not None:
            self.common_standard_price = m.get('common_standard_price')

        if m.get('inter_ticket_price') is not None:
            self.inter_ticket_price = m.get('inter_ticket_price')

        if m.get('subtracted_price') is not None:
            self.subtracted_price = m.get('subtracted_price')

        if m.get('origin_common_price') is not None:
            self.origin_common_price = m.get('origin_common_price')

        if m.get('dynamic_promotion_price') is not None:
            self.dynamic_promotion_price = m.get('dynamic_promotion_price')

        if m.get('installment_num') is not None:
            self.installment_num = m.get('installment_num')

        if m.get('installment_price') is not None:
            self.installment_price = m.get('installment_price')

        if m.get('competition_dynamic_price') is not None:
            self.competition_dynamic_price = m.get('competition_dynamic_price')

        if m.get('competition_promotion_price') is not None:
            self.competition_promotion_price = m.get('competition_promotion_price')

        if m.get('min_before_control_price_of_normal') is not None:
            self.min_before_control_price_of_normal = m.get('min_before_control_price_of_normal')

        if m.get('price_show_info') is not None:
            temp_model = main_models.ModuleItemListShoppingItemMapValueSegmentPriceValuePriceShowInfo()
            self.price_show_info = temp_model.from_map(m.get('price_show_info'))

        return self

class ModuleItemListShoppingItemMapValueSegmentPriceValuePriceShowInfo(DaraModel):
    def __init__(
        self,
        discount_info: str = None,
        discount_num: float = None,
        show_ticket_price: bool = None,
    ):
        self.discount_info = discount_info
        self.discount_num = discount_num
        self.show_ticket_price = show_ticket_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_info is not None:
            result['discount_info'] = self.discount_info

        if self.discount_num is not None:
            result['discount_num'] = self.discount_num

        if self.show_ticket_price is not None:
            result['show_ticket_price'] = self.show_ticket_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('discount_info') is not None:
            self.discount_info = m.get('discount_info')

        if m.get('discount_num') is not None:
            self.discount_num = m.get('discount_num')

        if m.get('show_ticket_price') is not None:
            self.show_ticket_price = m.get('show_ticket_price')

        return self

