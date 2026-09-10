# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecMetaDataComponentNameRequest(DaraModel):
    def __init__(
        self,
        ds_name: str = None,
    ):
        # The datasource name to check. The system performs an exact match against non-deleted datasources under the current tenant.
        self.ds_name = ds_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds_name is not None:
            result['dsName'] = self.ds_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dsName') is not None:
            self.ds_name = m.get('dsName')

        return self

