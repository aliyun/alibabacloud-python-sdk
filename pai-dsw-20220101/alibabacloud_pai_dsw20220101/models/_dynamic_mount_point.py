# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DynamicMountPoint(DaraModel):
    def __init__(
        self,
        options: str = None,
        root_path: str = None,
    ):
        self.options = options
        # This parameter is required.
        self.root_path = root_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.options is not None:
            result['Options'] = self.options

        if self.root_path is not None:
            result['RootPath'] = self.root_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('RootPath') is not None:
            self.root_path = m.get('RootPath')

        return self

