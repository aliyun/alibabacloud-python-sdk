# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTaskConcurrencyRequest(DaraModel):
    def __init__(
        self,
        application_code: str = None,
        caller_uac_account_id: str = None,
        current_workspace_id: str = None,
        task_id: int = None,
    ):
        self.application_code = application_code
        self.caller_uac_account_id = caller_uac_account_id
        self.current_workspace_id = current_workspace_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_code is not None:
            result['ApplicationCode'] = self.application_code

        if self.caller_uac_account_id is not None:
            result['CallerUacAccountId'] = self.caller_uac_account_id

        if self.current_workspace_id is not None:
            result['CurrentWorkspaceId'] = self.current_workspace_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCode') is not None:
            self.application_code = m.get('ApplicationCode')

        if m.get('CallerUacAccountId') is not None:
            self.caller_uac_account_id = m.get('CallerUacAccountId')

        if m.get('CurrentWorkspaceId') is not None:
            self.current_workspace_id = m.get('CurrentWorkspaceId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

