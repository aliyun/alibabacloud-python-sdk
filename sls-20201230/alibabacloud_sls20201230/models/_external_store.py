# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ExternalStore(DaraModel):
    def __init__(
        self,
        external_store_name: str = None,
        parameter: Dict[str, Any] = None,
        store_type: str = None,
    ):
        # This parameter is required.
        self.external_store_name = external_store_name
        # This parameter is required.
        self.parameter = parameter
        # This parameter is required.
        self.store_type = store_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_store_name is not None:
            result['externalStoreName'] = self.external_store_name

        if self.parameter is not None:
            result['parameter'] = self.parameter

        if self.store_type is not None:
            result['storeType'] = self.store_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalStoreName') is not None:
            self.external_store_name = m.get('externalStoreName')

        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')

        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')

        return self

