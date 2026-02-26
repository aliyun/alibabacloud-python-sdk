# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EticketInfo(DaraModel):
    def __init__(
        self,
        available_num: int = None,
        code: str = None,
        code_status: int = None,
        end_time: str = None,
        lock_num: int = None,
        qrcode_url: str = None,
        start_time: str = None,
        use_time: str = None,
        used_num: int = None,
    ):
        self.available_num = available_num
        self.code = code
        self.code_status = code_status
        self.end_time = end_time
        self.lock_num = lock_num
        self.qrcode_url = qrcode_url
        self.start_time = start_time
        self.use_time = use_time
        self.used_num = used_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_num is not None:
            result['availableNum'] = self.available_num

        if self.code is not None:
            result['code'] = self.code

        if self.code_status is not None:
            result['codeStatus'] = self.code_status

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.lock_num is not None:
            result['lockNum'] = self.lock_num

        if self.qrcode_url is not None:
            result['qrcodeUrl'] = self.qrcode_url

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.use_time is not None:
            result['useTime'] = self.use_time

        if self.used_num is not None:
            result['usedNum'] = self.used_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('availableNum') is not None:
            self.available_num = m.get('availableNum')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('codeStatus') is not None:
            self.code_status = m.get('codeStatus')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('lockNum') is not None:
            self.lock_num = m.get('lockNum')

        if m.get('qrcodeUrl') is not None:
            self.qrcode_url = m.get('qrcodeUrl')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('useTime') is not None:
            self.use_time = m.get('useTime')

        if m.get('usedNum') is not None:
            self.used_num = m.get('usedNum')

        return self

