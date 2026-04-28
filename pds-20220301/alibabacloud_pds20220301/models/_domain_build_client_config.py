# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DomainBuildClientConfig(DaraModel):
    def __init__(
        self,
        copyright: str = None,
        name: str = None,
    ):
        self.copyright = copyright
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.copyright is not None:
            result['copyright'] = self.copyright

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('copyright') is not None:
            self.copyright = m.get('copyright')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

