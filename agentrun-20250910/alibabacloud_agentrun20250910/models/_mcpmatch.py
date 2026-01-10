# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class MCPMatch(DaraModel):
    def __init__(
        self,
        path: main_models.MCPPathMatch = None,
    ):
        self.path = path

    def validate(self):
        if self.path:
            self.path.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['path'] = self.path.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            temp_model = main_models.MCPPathMatch()
            self.path = temp_model.from_map(m.get('path'))

        return self

