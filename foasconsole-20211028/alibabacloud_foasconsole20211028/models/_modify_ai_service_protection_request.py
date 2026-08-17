# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAiServiceProtectionRequest(DaraModel):
    def __init__(
        self,
        deletion_protection: bool = None,
        region: str = None,
    ):
        # Specifies whether to enable manual shutdown protection.
        # 
        # This parameter is required.
        self.deletion_protection = deletion_protection
        # The region ID.
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

