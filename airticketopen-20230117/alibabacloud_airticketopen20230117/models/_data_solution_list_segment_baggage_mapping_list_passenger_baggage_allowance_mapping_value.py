# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataSolutionListSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue(DaraModel):
    def __init__(
        self,
        baggage_amount: int = None,
        baggage_weight: int = None,
        baggage_weight_unit: str = None,
        is_all_weight: bool = None,
        carry_on_amount: int = None,
        carry_on_weight: int = None,
        carry_on_weight_unit: str = None,
        is_all_carry_on_weight: bool = None,
        carry_length: int = None,
        carry_width: int = None,
        carry_height: int = None,
        carry_sum_of_length_width_height: int = None,
        length: int = None,
        width: int = None,
        height: int = None,
        sum_of_length_width_height: int = None,
    ):
        # Number of checked baggage pieces
        self.baggage_amount = baggage_amount
        # Checked baggage weight
        self.baggage_weight = baggage_weight
        # Checked baggage weight unit KG
        self.baggage_weight_unit = baggage_weight_unit
        # Whether it is total checked baggage weight
        self.is_all_weight = is_all_weight
        # Number of carry-on baggage pieces
        self.carry_on_amount = carry_on_amount
        # Carry-on baggage weight
        self.carry_on_weight = carry_on_weight
        # Carry-on baggage weight unit KG
        self.carry_on_weight_unit = carry_on_weight_unit
        # Whether it is total carry-on baggage weight
        self.is_all_carry_on_weight = is_all_carry_on_weight
        self.carry_length = carry_length
        self.carry_width = carry_width
        self.carry_height = carry_height
        self.carry_sum_of_length_width_height = carry_sum_of_length_width_height
        self.length = length
        self.width = width
        self.height = height
        self.sum_of_length_width_height = sum_of_length_width_height

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_amount is not None:
            result['baggage_amount'] = self.baggage_amount

        if self.baggage_weight is not None:
            result['baggage_weight'] = self.baggage_weight

        if self.baggage_weight_unit is not None:
            result['baggage_weight_unit'] = self.baggage_weight_unit

        if self.is_all_weight is not None:
            result['is_all_weight'] = self.is_all_weight

        if self.carry_on_amount is not None:
            result['carry_on_amount'] = self.carry_on_amount

        if self.carry_on_weight is not None:
            result['carry_on_weight'] = self.carry_on_weight

        if self.carry_on_weight_unit is not None:
            result['carry_on_weight_unit'] = self.carry_on_weight_unit

        if self.is_all_carry_on_weight is not None:
            result['is_all_carry_on_weight'] = self.is_all_carry_on_weight

        if self.carry_length is not None:
            result['carry_length'] = self.carry_length

        if self.carry_width is not None:
            result['carry_width'] = self.carry_width

        if self.carry_height is not None:
            result['carry_height'] = self.carry_height

        if self.carry_sum_of_length_width_height is not None:
            result['carry_sum_of_length_width_height'] = self.carry_sum_of_length_width_height

        if self.length is not None:
            result['length'] = self.length

        if self.width is not None:
            result['width'] = self.width

        if self.height is not None:
            result['height'] = self.height

        if self.sum_of_length_width_height is not None:
            result['sum_of_length_width_height'] = self.sum_of_length_width_height

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_amount') is not None:
            self.baggage_amount = m.get('baggage_amount')

        if m.get('baggage_weight') is not None:
            self.baggage_weight = m.get('baggage_weight')

        if m.get('baggage_weight_unit') is not None:
            self.baggage_weight_unit = m.get('baggage_weight_unit')

        if m.get('is_all_weight') is not None:
            self.is_all_weight = m.get('is_all_weight')

        if m.get('carry_on_amount') is not None:
            self.carry_on_amount = m.get('carry_on_amount')

        if m.get('carry_on_weight') is not None:
            self.carry_on_weight = m.get('carry_on_weight')

        if m.get('carry_on_weight_unit') is not None:
            self.carry_on_weight_unit = m.get('carry_on_weight_unit')

        if m.get('is_all_carry_on_weight') is not None:
            self.is_all_carry_on_weight = m.get('is_all_carry_on_weight')

        if m.get('carry_length') is not None:
            self.carry_length = m.get('carry_length')

        if m.get('carry_width') is not None:
            self.carry_width = m.get('carry_width')

        if m.get('carry_height') is not None:
            self.carry_height = m.get('carry_height')

        if m.get('carry_sum_of_length_width_height') is not None:
            self.carry_sum_of_length_width_height = m.get('carry_sum_of_length_width_height')

        if m.get('length') is not None:
            self.length = m.get('length')

        if m.get('width') is not None:
            self.width = m.get('width')

        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('sum_of_length_width_height') is not None:
            self.sum_of_length_width_height = m.get('sum_of_length_width_height')

        return self

