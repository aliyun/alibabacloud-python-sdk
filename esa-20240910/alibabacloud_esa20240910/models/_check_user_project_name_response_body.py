# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckUserProjectNameResponseBody(DaraModel):
    def __init__(
        self,
        check: bool = None,
        description: str = None,
        project_name: str = None,
        request_id: str = None,
    ):
        # Indicates whether the name is valid. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.check = check
        # The reason why the name passed or failed the check.
        self.description = description
        # The name of the real-time log delivery task.
        self.project_name = project_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check is not None:
            result['Check'] = self.check

        if self.description is not None:
            result['Description'] = self.description

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Check') is not None:
            self.check = m.get('Check')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

