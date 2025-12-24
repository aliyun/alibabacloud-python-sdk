# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class QueryRtcAsrTasksResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        request_id: str = None,
        ret_code: int = None,
        tasks: Dict[str, Any] = None,
    ):
        # The result of the request. If success is returned, the request was successful. If an error message is returned, the request failed.
        self.description = description
        # The request ID.
        self.request_id = request_id
        # The HTTP status code. HTTP status code 2000 indicates that the request was successful. Other HTTP status codes indicate that the request failed.
        self.ret_code = ret_code
        # The results returned for the tasks.
        self.tasks = tasks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        if self.tasks is not None:
            result['Tasks'] = self.tasks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        if m.get('Tasks') is not None:
            self.tasks = m.get('Tasks')

        return self

