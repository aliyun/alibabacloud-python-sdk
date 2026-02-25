# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WebVersionStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        status: str = None,
    ):
        # The error message of the application execution. If the execution is successful, a null value is returned.
        self.error_message = error_message
        # The state of the application execution. Valid values:
        # 
        # *   **Completed**: The execution is successful.
        # *   **Updating**:The instance is being updated.
        # *   **Updating**:The execution failed and a non-null error message is returned.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

