# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModuleGroupItemSubItemsBaggageRuleBaggageInfoMapValue(DaraModel):
    def __init__(
        self,
        carry_freepc: int = None,
        carry_bag_weight: int = None,
        carry_bag_size: str = None,
        is_all_carry_bag_weight: bool = None,
        airline: str = None,
        start_airport: str = None,
        end_airport: str = None,
        start_city_code: str = None,
        end_city_code: str = None,
        free_pcs: int = None,
        baggage_weight: int = None,
        baggage_unit: str = None,
        baggage_size: str = None,
        all_weight: bool = None,
    ):
        self.carry_freepc = carry_freepc
        self.carry_bag_weight = carry_bag_weight
        self.carry_bag_size = carry_bag_size
        self.is_all_carry_bag_weight = is_all_carry_bag_weight
        self.airline = airline
        self.start_airport = start_airport
        self.end_airport = end_airport
        self.start_city_code = start_city_code
        self.end_city_code = end_city_code
        self.free_pcs = free_pcs
        self.baggage_weight = baggage_weight
        self.baggage_unit = baggage_unit
        self.baggage_size = baggage_size
        self.all_weight = all_weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carry_freepc is not None:
            result['carry_freepc'] = self.carry_freepc

        if self.carry_bag_weight is not None:
            result['carry_bag_weight'] = self.carry_bag_weight

        if self.carry_bag_size is not None:
            result['carry_bag_size'] = self.carry_bag_size

        if self.is_all_carry_bag_weight is not None:
            result['is_all_carry_bag_weight'] = self.is_all_carry_bag_weight

        if self.airline is not None:
            result['airline'] = self.airline

        if self.start_airport is not None:
            result['start_airport'] = self.start_airport

        if self.end_airport is not None:
            result['end_airport'] = self.end_airport

        if self.start_city_code is not None:
            result['start_city_code'] = self.start_city_code

        if self.end_city_code is not None:
            result['end_city_code'] = self.end_city_code

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carry_freepc') is not None:
            self.carry_freepc = m.get('carry_freepc')

        if m.get('carry_bag_weight') is not None:
            self.carry_bag_weight = m.get('carry_bag_weight')

        if m.get('carry_bag_size') is not None:
            self.carry_bag_size = m.get('carry_bag_size')

        if m.get('is_all_carry_bag_weight') is not None:
            self.is_all_carry_bag_weight = m.get('is_all_carry_bag_weight')

        if m.get('airline') is not None:
            self.airline = m.get('airline')

        if m.get('start_airport') is not None:
            self.start_airport = m.get('start_airport')

        if m.get('end_airport') is not None:
            self.end_airport = m.get('end_airport')

        if m.get('start_city_code') is not None:
            self.start_city_code = m.get('start_city_code')

        if m.get('end_city_code') is not None:
            self.end_city_code = m.get('end_city_code')

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

        return self

