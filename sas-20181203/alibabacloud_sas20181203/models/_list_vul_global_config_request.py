# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVulGlobalConfigRequest(DaraModel):
    def __init__(
        self,
        config_key: str = None,
    ):
        # The key of the configuration item. Valid values:
        # 
        # *   **vul_scan_ip_list**: The IP addresses that are detected.
        self.config_key = config_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')

        return self

