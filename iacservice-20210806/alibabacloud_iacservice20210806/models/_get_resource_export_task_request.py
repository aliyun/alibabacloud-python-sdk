# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceExportTaskRequest(DaraModel):
    def __init__(
        self,
        export_version: str = None,
    ):
        self.export_version = export_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_version is not None:
            result['exportVersion'] = self.export_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')

        return self

