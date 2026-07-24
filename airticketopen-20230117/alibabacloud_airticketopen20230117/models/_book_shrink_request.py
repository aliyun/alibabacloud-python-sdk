# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BookShrinkRequest(DaraModel):
    def __init__(
        self,
        contact_shrink: str = None,
        out_order_num: str = None,
        passenger_ancillary_purchase_map_list_shrink: str = None,
        passenger_list_shrink: str = None,
        solution_id: str = None,
    ):
        # The contact information.
        # 
        # This parameter is required.
        self.contact_shrink = contact_shrink
        # The external order number.
        # 
        # This parameter is required.
        self.out_order_num = out_order_num
        # The mapping between passengers and ancillary purchases.
        self.passenger_ancillary_purchase_map_list_shrink = passenger_ancillary_purchase_map_list_shrink
        # The list of passengers.
        # 
        # This parameter is required.
        self.passenger_list_shrink = passenger_list_shrink
        # solution_id.
        # 
        # This parameter is required.
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_shrink is not None:
            result['contact'] = self.contact_shrink

        if self.out_order_num is not None:
            result['out_order_num'] = self.out_order_num

        if self.passenger_ancillary_purchase_map_list_shrink is not None:
            result['passenger_ancillary_purchase_map_list'] = self.passenger_ancillary_purchase_map_list_shrink

        if self.passenger_list_shrink is not None:
            result['passenger_list'] = self.passenger_list_shrink

        if self.solution_id is not None:
            result['solution_id'] = self.solution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contact') is not None:
            self.contact_shrink = m.get('contact')

        if m.get('out_order_num') is not None:
            self.out_order_num = m.get('out_order_num')

        if m.get('passenger_ancillary_purchase_map_list') is not None:
            self.passenger_ancillary_purchase_map_list_shrink = m.get('passenger_ancillary_purchase_map_list')

        if m.get('passenger_list') is not None:
            self.passenger_list_shrink = m.get('passenger_list')

        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')

        return self

