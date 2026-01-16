# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class HTTPTriggerConfig(DaraModel):
    def __init__(
        self,
        auth_config: str = None,
        auth_type: str = None,
        disable_urlinternet: bool = None,
        methods: List[str] = None,
    ):
        self.auth_config = auth_config
        self.auth_type = auth_type
        self.disable_urlinternet = disable_urlinternet
        self.methods = methods

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config

        if self.auth_type is not None:
            result['authType'] = self.auth_type

        if self.disable_urlinternet is not None:
            result['disableURLInternet'] = self.disable_urlinternet

        if self.methods is not None:
            result['methods'] = self.methods

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            self.auth_config = m.get('authConfig')

        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('disableURLInternet') is not None:
            self.disable_urlinternet = m.get('disableURLInternet')

        if m.get('methods') is not None:
            self.methods = m.get('methods')

        return self

