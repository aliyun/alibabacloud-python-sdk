# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SeccompProfile(DaraModel):
    def __init__(
        self,
        localhost_profile: str = None,
        type: str = None,
    ):
        # The path of the Seccomp profile on the node. This parameter takes effect only when Type is set to Localhost.
        self.localhost_profile = localhost_profile
        # The Seccomp configuration type. Valid values: Localhost, RuntimeDefault, Unconfined.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.localhost_profile is not None:
            result['LocalhostProfile'] = self.localhost_profile

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalhostProfile') is not None:
            self.localhost_profile = m.get('LocalhostProfile')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

