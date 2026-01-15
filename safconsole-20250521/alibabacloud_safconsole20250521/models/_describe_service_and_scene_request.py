# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeServiceAndSceneRequest(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        customer_module_id: int = None,
    ):
        self.auth_type = auth_type
        self.customer_module_id = customer_module_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.customer_module_id is not None:
            result['CustomerModuleId'] = self.customer_module_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('CustomerModuleId') is not None:
            self.customer_module_id = m.get('CustomerModuleId')

        return self

