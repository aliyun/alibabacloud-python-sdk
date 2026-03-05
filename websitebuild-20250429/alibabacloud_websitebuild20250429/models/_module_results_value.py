# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModuleResultsValue(DaraModel):
    def __init__(
        self,
        passed: bool = None,
        resource_code: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.passed = passed
        self.resource_code = resource_code
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passed is not None:
            result['Passed'] = self.passed

        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        return self

