# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ElectronicItineraryBatchApplyShrinkRequest(DaraModel):
    def __init__(
        self,
        apply_itinerary_list_shrink: str = None,
        can_reprint: bool = None,
    ):
        # This parameter is required.
        self.apply_itinerary_list_shrink = apply_itinerary_list_shrink
        self.can_reprint = can_reprint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_itinerary_list_shrink is not None:
            result['apply_itinerary_list'] = self.apply_itinerary_list_shrink

        if self.can_reprint is not None:
            result['can_reprint'] = self.can_reprint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_itinerary_list') is not None:
            self.apply_itinerary_list_shrink = m.get('apply_itinerary_list')

        if m.get('can_reprint') is not None:
            self.can_reprint = m.get('can_reprint')

        return self

