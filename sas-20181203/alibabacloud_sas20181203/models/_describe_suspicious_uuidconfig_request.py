# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSuspiciousUUIDConfigRequest(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The type of proactive defense. Valid values:
        # 
        # *   **auto_breaking**: virus defense
        # *   **ransomware_breaking**: ransomware capture
        # *   **webshell_cloud_breaking**: webshell defense
        # *   **alinet**: malicious behavior defense
        # *   **alisecguard**: client protection
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

