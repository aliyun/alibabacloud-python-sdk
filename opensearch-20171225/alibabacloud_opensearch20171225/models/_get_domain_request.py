# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDomainRequest(DaraModel):
    def __init__(
        self,
        app_group_identity: str = None,
    ):
        # The name or ID of the application.
        # 
        # This parameter is required.
        self.app_group_identity = app_group_identity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group_identity is not None:
            result['appGroupIdentity'] = self.app_group_identity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appGroupIdentity') is not None:
            self.app_group_identity = m.get('appGroupIdentity')

        return self

