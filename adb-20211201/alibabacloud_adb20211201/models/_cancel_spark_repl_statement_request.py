# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelSparkReplStatementRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        session_id: int = None,
        statement_id: int = None,
    ):
        # The application ID.
        # 
        # >  You can call the [ListSparkApps](https://help.aliyun.com/document_detail/455888.html) operation to query Spark application IDs.
        self.app_id = app_id
        # The session ID.
        self.session_id = session_id
        # The unique ID of the code block in the Spark job.
        self.statement_id = statement_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.statement_id is not None:
            result['StatementId'] = self.statement_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StatementId') is not None:
            self.statement_id = m.get('StatementId')

        return self

