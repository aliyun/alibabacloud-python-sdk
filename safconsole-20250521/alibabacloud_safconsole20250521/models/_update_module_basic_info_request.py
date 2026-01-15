# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateModuleBasicInfoRequest(DaraModel):
    def __init__(
        self,
        customer_module_id: int = None,
        customer_module_name: str = None,
        description: str = None,
        module_type: str = None,
        store_path: str = None,
    ):
        # Customer model ID
        self.customer_module_id = customer_module_id
        # Model name.
        self.customer_module_name = customer_module_name
        # Description.
        self.description = description
        # Module type.
        self.module_type = module_type
        # Test address.
        self.store_path = store_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_module_id is not None:
            result['CustomerModuleId'] = self.customer_module_id

        if self.customer_module_name is not None:
            result['CustomerModuleName'] = self.customer_module_name

        if self.description is not None:
            result['Description'] = self.description

        if self.module_type is not None:
            result['ModuleType'] = self.module_type

        if self.store_path is not None:
            result['StorePath'] = self.store_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerModuleId') is not None:
            self.customer_module_id = m.get('CustomerModuleId')

        if m.get('CustomerModuleName') is not None:
            self.customer_module_name = m.get('CustomerModuleName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModuleType') is not None:
            self.module_type = m.get('ModuleType')

        if m.get('StorePath') is not None:
            self.store_path = m.get('StorePath')

        return self

