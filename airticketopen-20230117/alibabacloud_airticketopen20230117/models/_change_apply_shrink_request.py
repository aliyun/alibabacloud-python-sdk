# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeApplyShrinkRequest(DaraModel):
    def __init__(
        self,
        change_passenger_list_shrink: str = None,
        changed_journeys_shrink: str = None,
        contact_shrink: str = None,
        order_num: int = None,
        remark: str = None,
        type: int = None,
    ):
        # The list of passengers for the change.
        # 
        # This parameter is required.
        self.change_passenger_list_shrink = change_passenger_list_shrink
        # The target journey for the change.
        # 
        # This parameter is required.
        self.changed_journeys_shrink = changed_journeys_shrink
        # The contact information for the change.
        # 
        # This parameter is required.
        self.contact_shrink = contact_shrink
        # The order number.
        # 
        # This parameter is required.
        self.order_num = order_num
        # The buyer remarks.
        self.remark = remark
        # The change type. Valid values:
        # - 0: voluntary change
        # - 1: flight schedule change or flight cancellation.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_passenger_list_shrink is not None:
            result['change_passenger_list'] = self.change_passenger_list_shrink

        if self.changed_journeys_shrink is not None:
            result['changed_journeys'] = self.changed_journeys_shrink

        if self.contact_shrink is not None:
            result['contact'] = self.contact_shrink

        if self.order_num is not None:
            result['order_num'] = self.order_num

        if self.remark is not None:
            result['remark'] = self.remark

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_passenger_list') is not None:
            self.change_passenger_list_shrink = m.get('change_passenger_list')

        if m.get('changed_journeys') is not None:
            self.changed_journeys_shrink = m.get('changed_journeys')

        if m.get('contact') is not None:
            self.contact_shrink = m.get('contact')

        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

