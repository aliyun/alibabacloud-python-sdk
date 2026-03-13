# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class ElectronicItineraryBatchApplyRequest(DaraModel):
    def __init__(
        self,
        apply_itinerary_list: List[main_models.ElectronicItineraryBatchApplyRequestApplyItineraryList] = None,
        can_reprint: bool = None,
    ):
        # This parameter is required.
        self.apply_itinerary_list = apply_itinerary_list
        self.can_reprint = can_reprint

    def validate(self):
        if self.apply_itinerary_list:
            for v1 in self.apply_itinerary_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['apply_itinerary_list'] = []
        if self.apply_itinerary_list is not None:
            for k1 in self.apply_itinerary_list:
                result['apply_itinerary_list'].append(k1.to_map() if k1 else None)

        if self.can_reprint is not None:
            result['can_reprint'] = self.can_reprint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_itinerary_list = []
        if m.get('apply_itinerary_list') is not None:
            for k1 in m.get('apply_itinerary_list'):
                temp_model = main_models.ElectronicItineraryBatchApplyRequestApplyItineraryList()
                self.apply_itinerary_list.append(temp_model.from_map(k1))

        if m.get('can_reprint') is not None:
            self.can_reprint = m.get('can_reprint')

        return self

class ElectronicItineraryBatchApplyRequestApplyItineraryList(DaraModel):
    def __init__(
        self,
        purchaser_name: str = None,
        purchaser_tax_no: str = None,
        purchaser_type: int = None,
        ticket_no: str = None,
    ):
        self.purchaser_name = purchaser_name
        self.purchaser_tax_no = purchaser_tax_no
        # This parameter is required.
        self.purchaser_type = purchaser_type
        # This parameter is required.
        self.ticket_no = ticket_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.purchaser_name is not None:
            result['purchaser_name'] = self.purchaser_name

        if self.purchaser_tax_no is not None:
            result['purchaser_tax_no'] = self.purchaser_tax_no

        if self.purchaser_type is not None:
            result['purchaser_type'] = self.purchaser_type

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('purchaser_name') is not None:
            self.purchaser_name = m.get('purchaser_name')

        if m.get('purchaser_tax_no') is not None:
            self.purchaser_tax_no = m.get('purchaser_tax_no')

        if m.get('purchaser_type') is not None:
            self.purchaser_type = m.get('purchaser_type')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        return self

