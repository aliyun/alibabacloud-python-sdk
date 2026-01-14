# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AppServiceGroup(DaraModel):
    def __init__(
        self,
        name: str = None,
        qr_code: str = None,
        type: str = None,
        url: str = None,
    ):
        self.name = name
        self.qr_code = qr_code
        # 例如：dingtalk、wx 等
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.qr_code is not None:
            result['QrCode'] = self.qr_code

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QrCode') is not None:
            self.qr_code = m.get('QrCode')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

