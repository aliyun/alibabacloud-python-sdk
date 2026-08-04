# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAndDoVoipCallForHotelShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_data: str = None,
        callee_nick: str = None,
        callee_phone_num: str = None,
        device_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.biz_data = biz_data
        self.callee_nick = callee_nick
        self.callee_phone_num = callee_phone_num
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_data is not None:
            result['BizData'] = self.biz_data

        if self.callee_nick is not None:
            result['CalleeNick'] = self.callee_nick

        if self.callee_phone_num is not None:
            result['CalleePhoneNum'] = self.callee_phone_num

        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')

        if m.get('CalleeNick') is not None:
            self.callee_nick = m.get('CalleeNick')

        if m.get('CalleePhoneNum') is not None:
            self.callee_phone_num = m.get('CalleePhoneNum')

        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        return self

