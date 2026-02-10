# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDynamicDictRequest(DaraModel):
    def __init__(
        self,
        override: bool = None,
        source_ip: str = None,
    ):
        # Specifies whether to overwrite existing data. Valid values:
        # 
        # *   true
        # *   false
        self.override = override
        # The source IP address.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.override is not None:
            result['Override'] = self.override

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Override') is not None:
            self.override = m.get('Override')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

