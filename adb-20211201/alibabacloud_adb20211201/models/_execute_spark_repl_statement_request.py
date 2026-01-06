# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteSparkReplStatementRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        code: str = None,
        code_type: str = None,
        session_id: int = None,
    ):
        # The application ID.
        # 
        # >  You can call the [ListSparkApps](https://help.aliyun.com/document_detail/455888.html) operation to query Spark application IDs.
        self.app_id = app_id
        # The code that you want to execute.
        # 
        # This parameter is required.
        self.code = code
        # The language type of the code. Valid values:
        # 
        # *   SCALA
        # *   PYTHON
        # 
        # This parameter is required.
        self.code_type = code_type
        # The ID of the session that you want to use to execute the code.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.code is not None:
            result['Code'] = self.code

        if self.code_type is not None:
            result['CodeType'] = self.code_type

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CodeType') is not None:
            self.code_type = m.get('CodeType')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

