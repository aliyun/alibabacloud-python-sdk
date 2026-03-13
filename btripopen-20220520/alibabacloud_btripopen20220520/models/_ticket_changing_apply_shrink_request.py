# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TicketChangingApplyShrinkRequest(DaraModel):
    def __init__(
        self,
        dis_order_id: str = None,
        dis_sub_order_id: str = None,
        is_voluntary: int = None,
        modify_flight_info_list_shrink: str = None,
        ota_item_id: str = None,
        reason: str = None,
        session_id: str = None,
        whether_retry: bool = None,
    ):
        # This parameter is required.
        self.dis_order_id = dis_order_id
        # This parameter is required.
        self.dis_sub_order_id = dis_sub_order_id
        self.is_voluntary = is_voluntary
        # This parameter is required.
        self.modify_flight_info_list_shrink = modify_flight_info_list_shrink
        # This parameter is required.
        self.ota_item_id = ota_item_id
        self.reason = reason
        # This parameter is required.
        self.session_id = session_id
        self.whether_retry = whether_retry

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.dis_sub_order_id is not None:
            result['dis_sub_order_id'] = self.dis_sub_order_id

        if self.is_voluntary is not None:
            result['is_voluntary'] = self.is_voluntary

        if self.modify_flight_info_list_shrink is not None:
            result['modify_flight_info_list'] = self.modify_flight_info_list_shrink

        if self.ota_item_id is not None:
            result['ota_item_id'] = self.ota_item_id

        if self.reason is not None:
            result['reason'] = self.reason

        if self.session_id is not None:
            result['session_id'] = self.session_id

        if self.whether_retry is not None:
            result['whether_retry'] = self.whether_retry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('dis_sub_order_id') is not None:
            self.dis_sub_order_id = m.get('dis_sub_order_id')

        if m.get('is_voluntary') is not None:
            self.is_voluntary = m.get('is_voluntary')

        if m.get('modify_flight_info_list') is not None:
            self.modify_flight_info_list_shrink = m.get('modify_flight_info_list')

        if m.get('ota_item_id') is not None:
            self.ota_item_id = m.get('ota_item_id')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('whether_retry') is not None:
            self.whether_retry = m.get('whether_retry')

        return self

