# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateTestFileRequest(DaraModel):
    def __init__(
        self,
        customer_module_id: str = None,
        file_path: str = None,
    ):
        # Model ID.
        self.customer_module_id = customer_module_id
        # File path.
        self.file_path = file_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_module_id is not None:
            result['CustomerModuleId'] = self.customer_module_id

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerModuleId') is not None:
            self.customer_module_id = m.get('CustomerModuleId')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        return self

