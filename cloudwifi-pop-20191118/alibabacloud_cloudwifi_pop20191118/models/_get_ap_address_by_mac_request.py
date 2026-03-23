# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetApAddressByMacRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        language: str = None,
        mac: str = None,
    ):
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.language = language
        # This parameter is required.
        self.mac = mac

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

        if self.language is not None:
            result['Language'] = self.language

        if self.mac is not None:
            result['Mac'] = self.mac

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        return self

