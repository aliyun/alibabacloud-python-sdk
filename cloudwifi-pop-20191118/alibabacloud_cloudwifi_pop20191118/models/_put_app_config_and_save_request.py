# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutAppConfigAndSaveRequest(DaraModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
        configure_type: str = None,
        current_time: int = None,
        data: str = None,
    ):
        # This parameter is required.
        self.ap_mac = ap_mac
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.configure_type = configure_type
        # This parameter is required.
        self.current_time = current_time
        # This parameter is required.
        self.data = data

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

        if self.configure_type is not None:
            result['ConfigureType'] = self.configure_type

        if self.current_time is not None:
            result['CurrentTime'] = self.current_time

        if self.data is not None:
            result['Data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ConfigureType') is not None:
            self.configure_type = m.get('ConfigureType')

        if m.get('CurrentTime') is not None:
            self.current_time = m.get('CurrentTime')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        return self

