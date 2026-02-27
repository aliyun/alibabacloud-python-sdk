# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindPasswordFreeLoginUserRequest(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
        main_biz_type: str = None,
        serial_number: str = None,
        uuid: str = None,
    ):
        self.end_user_id = end_user_id
        self.main_biz_type = main_biz_type
        self.serial_number = serial_number
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.main_biz_type is not None:
            result['MainBizType'] = self.main_biz_type

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('MainBizType') is not None:
            self.main_biz_type = m.get('MainBizType')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

