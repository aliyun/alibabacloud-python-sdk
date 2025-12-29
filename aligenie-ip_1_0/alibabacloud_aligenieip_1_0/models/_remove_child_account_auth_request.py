# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveChildAccountAuthRequest(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        child_account_name: str = None,
        hotel_id: str = None,
        tb_open_id: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.child_account_name = child_account_name
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.tb_open_id = tb_open_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.child_account_name is not None:
            result['ChildAccountName'] = self.child_account_name

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('ChildAccountName') is not None:
            self.child_account_name = m.get('ChildAccountName')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')

        return self

