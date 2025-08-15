# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class AlterTableRequest(DaraModel):
    def __init__(
        self,
        changes: List[main_models.FullSchemaChange] = None,
    ):
        self.changes = changes

    def validate(self):
        if self.changes:
            for v1 in self.changes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['changes'] = []
        if self.changes is not None:
            for k1 in self.changes:
                result['changes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.changes = []
        if m.get('changes') is not None:
            for k1 in m.get('changes'):
                temp_model = main_models.FullSchemaChange()
                self.changes.append(temp_model.from_map(k1))

        return self

