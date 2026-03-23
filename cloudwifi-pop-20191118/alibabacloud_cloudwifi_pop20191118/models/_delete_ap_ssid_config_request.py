# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteApSsidConfigRequest(DaraModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
        radio_index: str = None,
        ssid: str = None,
    ):
        # This parameter is required.
        self.ap_mac = ap_mac
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.radio_index = radio_index
        # This parameter is required.
        self.ssid = ssid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.radio_index is not None:
            result['RadioIndex'] = self.radio_index

        if self.ssid is not None:
            result['Ssid'] = self.ssid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('RadioIndex') is not None:
            self.radio_index = m.get('RadioIndex')

        if m.get('Ssid') is not None:
            self.ssid = m.get('Ssid')

        return self

