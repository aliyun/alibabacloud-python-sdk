# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPackageRequest(DaraModel):
    def __init__(
        self,
        source_project: str = None,
    ):
        self.source_project = source_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_project is not None:
            result['sourceProject'] = self.source_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceProject') is not None:
            self.source_project = m.get('sourceProject')

        return self

