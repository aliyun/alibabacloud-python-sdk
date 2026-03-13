# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModuleOrderItemListBaggageRuleOfferBaggageInfoMapValue(DaraModel):
    def __init__(
        self,
        start_city_code: str = None,
        end_city_code: str = None,
        carry_free_pc: int = None,
        carry_bag_weight: int = None,
        carry_bag_size: str = None,
        is_all_carry_bag_weight: bool = None,
        total_pcs: int = None,
        total_weight: int = None,
        carry_unknown: bool = None,
        carry_length: int = None,
        carry_width: int = None,
        carry_height: int = None,
        carry_sum_of_length_width_height: int = None,
        free_pcs: int = None,
        baggage_weight: int = None,
        baggage_unit: str = None,
        baggage_size: str = None,
        all_weight: bool = None,
        length: int = None,
        width: int = None,
        height: int = None,
        sum_of_length_width_height: int = None,
        unknown: bool = None,
        cn_desc: str = None,
        en_desc: str = None,
        attribute: str = None,
        baggage_price: int = None,
        carry_on_baggage_tips: str = None,
    ):
        self.start_city_code = start_city_code
        self.end_city_code = end_city_code
        self.carry_free_pc = carry_free_pc
        self.carry_bag_weight = carry_bag_weight
        self.carry_bag_size = carry_bag_size
        self.is_all_carry_bag_weight = is_all_carry_bag_weight
        self.total_pcs = total_pcs
        self.total_weight = total_weight
        self.carry_unknown = carry_unknown
        self.carry_length = carry_length
        self.carry_width = carry_width
        self.carry_height = carry_height
        self.carry_sum_of_length_width_height = carry_sum_of_length_width_height
        self.free_pcs = free_pcs
        self.baggage_weight = baggage_weight
        self.baggage_unit = baggage_unit
        self.baggage_size = baggage_size
        self.all_weight = all_weight
        self.length = length
        self.width = width
        self.height = height
        self.sum_of_length_width_height = sum_of_length_width_height
        self.unknown = unknown
        self.cn_desc = cn_desc
        self.en_desc = en_desc
        self.attribute = attribute
        self.baggage_price = baggage_price
        self.carry_on_baggage_tips = carry_on_baggage_tips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.start_city_code is not None:
            result['start_city_code'] = self.start_city_code

        if self.end_city_code is not None:
            result['end_city_code'] = self.end_city_code

        if self.carry_free_pc is not None:
            result['carry_free_pc'] = self.carry_free_pc

        if self.carry_bag_weight is not None:
            result['carry_bag_weight'] = self.carry_bag_weight

        if self.carry_bag_size is not None:
            result['carry_bag_size'] = self.carry_bag_size

        if self.is_all_carry_bag_weight is not None:
            result['is_all_carry_bag_weight'] = self.is_all_carry_bag_weight

        if self.total_pcs is not None:
            result['total_pcs'] = self.total_pcs

        if self.total_weight is not None:
            result['total_weight'] = self.total_weight

        if self.carry_unknown is not None:
            result['carry_unknown'] = self.carry_unknown

        if self.carry_length is not None:
            result['carry_length'] = self.carry_length

        if self.carry_width is not None:
            result['carry_width'] = self.carry_width

        if self.carry_height is not None:
            result['carry_height'] = self.carry_height

        if self.carry_sum_of_length_width_height is not None:
            result['carry_sum_of_length_width_height'] = self.carry_sum_of_length_width_height

        if self.free_pcs is not None:
            result['free_pcs'] = self.free_pcs

        if self.baggage_weight is not None:
            result['baggage_weight'] = self.baggage_weight

        if self.baggage_unit is not None:
            result['baggage_unit'] = self.baggage_unit

        if self.baggage_size is not None:
            result['baggage_size'] = self.baggage_size

        if self.all_weight is not None:
            result['all_weight'] = self.all_weight

        if self.length is not None:
            result['length'] = self.length

        if self.width is not None:
            result['width'] = self.width

        if self.height is not None:
            result['height'] = self.height

        if self.sum_of_length_width_height is not None:
            result['sum_of_length_width_height'] = self.sum_of_length_width_height

        if self.unknown is not None:
            result['unknown'] = self.unknown

        if self.cn_desc is not None:
            result['cn_desc'] = self.cn_desc

        if self.en_desc is not None:
            result['en_desc'] = self.en_desc

        if self.attribute is not None:
            result['attribute'] = self.attribute

        if self.baggage_price is not None:
            result['baggage_price'] = self.baggage_price

        if self.carry_on_baggage_tips is not None:
            result['carry_on_baggage_tips'] = self.carry_on_baggage_tips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('start_city_code') is not None:
            self.start_city_code = m.get('start_city_code')

        if m.get('end_city_code') is not None:
            self.end_city_code = m.get('end_city_code')

        if m.get('carry_free_pc') is not None:
            self.carry_free_pc = m.get('carry_free_pc')

        if m.get('carry_bag_weight') is not None:
            self.carry_bag_weight = m.get('carry_bag_weight')

        if m.get('carry_bag_size') is not None:
            self.carry_bag_size = m.get('carry_bag_size')

        if m.get('is_all_carry_bag_weight') is not None:
            self.is_all_carry_bag_weight = m.get('is_all_carry_bag_weight')

        if m.get('total_pcs') is not None:
            self.total_pcs = m.get('total_pcs')

        if m.get('total_weight') is not None:
            self.total_weight = m.get('total_weight')

        if m.get('carry_unknown') is not None:
            self.carry_unknown = m.get('carry_unknown')

        if m.get('carry_length') is not None:
            self.carry_length = m.get('carry_length')

        if m.get('carry_width') is not None:
            self.carry_width = m.get('carry_width')

        if m.get('carry_height') is not None:
            self.carry_height = m.get('carry_height')

        if m.get('carry_sum_of_length_width_height') is not None:
            self.carry_sum_of_length_width_height = m.get('carry_sum_of_length_width_height')

        if m.get('free_pcs') is not None:
            self.free_pcs = m.get('free_pcs')

        if m.get('baggage_weight') is not None:
            self.baggage_weight = m.get('baggage_weight')

        if m.get('baggage_unit') is not None:
            self.baggage_unit = m.get('baggage_unit')

        if m.get('baggage_size') is not None:
            self.baggage_size = m.get('baggage_size')

        if m.get('all_weight') is not None:
            self.all_weight = m.get('all_weight')

        if m.get('length') is not None:
            self.length = m.get('length')

        if m.get('width') is not None:
            self.width = m.get('width')

        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('sum_of_length_width_height') is not None:
            self.sum_of_length_width_height = m.get('sum_of_length_width_height')

        if m.get('unknown') is not None:
            self.unknown = m.get('unknown')

        if m.get('cn_desc') is not None:
            self.cn_desc = m.get('cn_desc')

        if m.get('en_desc') is not None:
            self.en_desc = m.get('en_desc')

        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')

        if m.get('baggage_price') is not None:
            self.baggage_price = m.get('baggage_price')

        if m.get('carry_on_baggage_tips') is not None:
            self.carry_on_baggage_tips = m.get('carry_on_baggage_tips')

        return self

