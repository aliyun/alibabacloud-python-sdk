# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDBTaskSQLJobLogRequest(DaraModel):
    def __init__(
        self,
        job_id: int = None,
        tid: int = None,
    ):
        # The ID of the SQL task. You can call the [ListDBTaskSQLJob](https://help.aliyun.com/document_detail/207049.html) operation to query the ID of the SQL task.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

