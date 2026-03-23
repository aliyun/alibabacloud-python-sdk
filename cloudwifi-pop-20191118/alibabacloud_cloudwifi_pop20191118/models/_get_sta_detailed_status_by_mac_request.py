# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStaDetailedStatusByMacRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        sta_mac: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.sta_mac = sta_mac

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.sta_mac is not None:
            result['StaMac'] = self.sta_mac

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('StaMac') is not None:
            self.sta_mac = m.get('StaMac')

        return self

