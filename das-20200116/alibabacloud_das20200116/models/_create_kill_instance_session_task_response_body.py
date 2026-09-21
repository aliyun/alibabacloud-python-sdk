# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKillInstanceSessionTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned status code.
        self.code = code
        # The task ID for terminating sessions.
        # 
        # > When you invoke this API operation for a PolarDB for MySQL instance with the **NodeId** request parameter left empty (no node ID specified) and the **KillAllSessions** request parameter set to **true** (terminate all sessions), a list of task IDs is returned based on the number of nodes, such as ["f77d535b45405bd462b21caa3ee8\\*\\*\\*\\*", "e93ab549abb081eb5dcd5396a29b\\*\\*\\*\\*"\\].
        self.data = data
        # The returned message.
        # >If the request is successful, **Successful** is returned. If the request fails, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        # 
        # - **true**: The request is successful.
        # - **false**: The request fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

