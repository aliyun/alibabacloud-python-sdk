# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetExecuteStateResponseBody(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        log_file: Dict[str, Any] = None,
        request_id: str = None,
        state: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.log_file = log_file
        # Id of the request
        self.request_id = request_id
        self.state = state
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.log_file is not None:
            result['logFile'] = self.log_file

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.state is not None:
            result['state'] = self.state

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('logFile') is not None:
            self.log_file = m.get('logFile')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

