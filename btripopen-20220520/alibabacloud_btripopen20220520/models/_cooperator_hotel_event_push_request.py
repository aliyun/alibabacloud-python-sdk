# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CooperatorHotelEventPushRequest(DaraModel):
    def __init__(
        self,
        change_order_status: int = None,
        change_order_status_desc: str = None,
        cooperator_order_id: str = None,
        event: str = None,
        event_desc: str = None,
        event_time: str = None,
        order_id: str = None,
    ):
        self.change_order_status = change_order_status
        self.change_order_status_desc = change_order_status_desc
        # This parameter is required.
        self.cooperator_order_id = cooperator_order_id
        # This parameter is required.
        self.event = event
        self.event_desc = event_desc
        # This parameter is required.
        self.event_time = event_time
        # This parameter is required.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_status is not None:
            result['change_order_status'] = self.change_order_status

        if self.change_order_status_desc is not None:
            result['change_order_status_desc'] = self.change_order_status_desc

        if self.cooperator_order_id is not None:
            result['cooperator_order_id'] = self.cooperator_order_id

        if self.event is not None:
            result['event'] = self.event

        if self.event_desc is not None:
            result['event_desc'] = self.event_desc

        if self.event_time is not None:
            result['event_time'] = self.event_time

        if self.order_id is not None:
            result['order_id'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_order_status') is not None:
            self.change_order_status = m.get('change_order_status')

        if m.get('change_order_status_desc') is not None:
            self.change_order_status_desc = m.get('change_order_status_desc')

        if m.get('cooperator_order_id') is not None:
            self.cooperator_order_id = m.get('cooperator_order_id')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('event_desc') is not None:
            self.event_desc = m.get('event_desc')

        if m.get('event_time') is not None:
            self.event_time = m.get('event_time')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        return self

