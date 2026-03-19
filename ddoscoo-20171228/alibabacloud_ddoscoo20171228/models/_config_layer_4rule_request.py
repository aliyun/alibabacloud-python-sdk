# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class ConfigLayer4RuleRequest(DaraModel):
    def __init__(
        self,
        listeners: str = None,
        proxy_enable: int = None,
        us_timeout: main_models.ConfigLayer4RuleRequestUsTimeout = None,
    ):
        # This parameter is required.
        self.listeners = listeners
        self.proxy_enable = proxy_enable
        self.us_timeout = us_timeout

    def validate(self):
        if self.us_timeout:
            self.us_timeout.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listeners is not None:
            result['Listeners'] = self.listeners

        if self.proxy_enable is not None:
            result['ProxyEnable'] = self.proxy_enable

        if self.us_timeout is not None:
            result['UsTimeout'] = self.us_timeout.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')

        if m.get('ProxyEnable') is not None:
            self.proxy_enable = m.get('ProxyEnable')

        if m.get('UsTimeout') is not None:
            temp_model = main_models.ConfigLayer4RuleRequestUsTimeout()
            self.us_timeout = temp_model.from_map(m.get('UsTimeout'))

        return self



class ConfigLayer4RuleRequestUsTimeout(DaraModel):
    def __init__(
        self,
        connect_timeout: int = None,
        rs_timeout: int = None,
    ):
        self.connect_timeout = connect_timeout
        self.rs_timeout = rs_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout

        if self.rs_timeout is not None:
            result['RsTimeout'] = self.rs_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')

        if m.get('RsTimeout') is not None:
            self.rs_timeout = m.get('RsTimeout')

        return self

