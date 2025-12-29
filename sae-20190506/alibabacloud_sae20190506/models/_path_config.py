# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PathConfig(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        path: str = None,
    ):
        self.application_name = application_name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['applicationName'] = self.application_name

        if self.path is not None:
            result['path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationName') is not None:
            self.application_name = m.get('applicationName')

        if m.get('path') is not None:
            self.path = m.get('path')

        return self

