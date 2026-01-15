# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IterateModelRequest(DaraModel):
    def __init__(
        self,
        customer_module_id: int = None,
    ):
        self.customer_module_id = customer_module_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_module_id is not None:
            result['CustomerModuleId'] = self.customer_module_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerModuleId') is not None:
            self.customer_module_id = m.get('CustomerModuleId')

        return self

