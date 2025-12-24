# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLiveDomainMultiStreamConfigRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        owner_id: int = None,
        switch: str = None,
    ):
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        self.owner_id = owner_id
        # Specifies whether to enable the dual-stream disaster recovery feature. Valid values:
        # 
        # *   **on**: enables the feature.
        # *   **off**: disables the feature.
        # 
        # This parameter is required.
        self.switch = switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.switch is not None:
            result['Switch'] = self.switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Switch') is not None:
            self.switch = m.get('Switch')

        return self

