# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelOrderChangeApplyRequest(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        dis_order_id: str = None,
        reason: str = None,
        room_info_list: List[main_models.HotelOrderChangeApplyRequestRoomInfoList] = None,
        sale_order_id: str = None,
    ):
        self.btrip_user_id = btrip_user_id
        # This parameter is required.
        self.dis_order_id = dis_order_id
        # This parameter is required.
        self.reason = reason
        # This parameter is required.
        self.room_info_list = room_info_list
        # This parameter is required.
        self.sale_order_id = sale_order_id

    def validate(self):
        if self.room_info_list:
            for v1 in self.room_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.reason is not None:
            result['reason'] = self.reason

        result['room_info_list'] = []
        if self.room_info_list is not None:
            for k1 in self.room_info_list:
                result['room_info_list'].append(k1.to_map() if k1 else None)

        if self.sale_order_id is not None:
            result['sale_order_id'] = self.sale_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        self.room_info_list = []
        if m.get('room_info_list') is not None:
            for k1 in m.get('room_info_list'):
                temp_model = main_models.HotelOrderChangeApplyRequestRoomInfoList()
                self.room_info_list.append(temp_model.from_map(k1))

        if m.get('sale_order_id') is not None:
            self.sale_order_id = m.get('sale_order_id')

        return self

class HotelOrderChangeApplyRequestRoomInfoList(DaraModel):
    def __init__(
        self,
        cancel_date: List[str] = None,
        room_no: int = None,
    ):
        # This parameter is required.
        self.cancel_date = cancel_date
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_date is not None:
            result['cancel_date'] = self.cancel_date

        if self.room_no is not None:
            result['room_no'] = self.room_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cancel_date') is not None:
            self.cancel_date = m.get('cancel_date')

        if m.get('room_no') is not None:
            self.room_no = m.get('room_no')

        return self

