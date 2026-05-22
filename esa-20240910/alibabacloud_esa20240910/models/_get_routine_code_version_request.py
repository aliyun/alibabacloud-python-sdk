# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRoutineCodeVersionRequest(DaraModel):
    def __init__(
        self,
        code_version: str = None,
        name: str = None,
    ):
        # The code version.
        # 
        # This parameter is required.
        self.code_version = code_version
        # The routine name.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

