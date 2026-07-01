# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRcsSignMenuByVersionRequest(DaraModel):
    def __init__(
        self,
        rcs_menu_version: str = None,
        sign_name: str = None,
    ):
        # This parameter is required.
        self.rcs_menu_version = rcs_menu_version
        # This parameter is required.
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rcs_menu_version is not None:
            result['RcsMenuVersion'] = self.rcs_menu_version

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RcsMenuVersion') is not None:
            self.rcs_menu_version = m.get('RcsMenuVersion')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        return self

