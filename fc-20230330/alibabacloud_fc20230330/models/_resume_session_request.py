# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResumeSessionRequest(DaraModel):
    def __init__(
        self,
        file_system_only: bool = None,
        qualifier: str = None,
    ):
        self.file_system_only = file_system_only
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_only is not None:
            result['fileSystemOnly'] = self.file_system_only

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSystemOnly') is not None:
            self.file_system_only = m.get('fileSystemOnly')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        return self

