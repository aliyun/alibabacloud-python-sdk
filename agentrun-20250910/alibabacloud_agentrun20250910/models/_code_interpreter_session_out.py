# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CodeInterpreterSessionOut(DaraModel):
    def __init__(
        self,
        code_interpreter_id: str = None,
        code_interpreter_name: str = None,
        created_at: str = None,
        last_updated_at: str = None,
        session_id: str = None,
        session_idle_timeout_seconds: int = None,
        status: str = None,
    ):
        # The Unique Identifier of the associated code interpreter
        # 
        # This parameter is required.
        self.code_interpreter_id = code_interpreter_id
        # The name of the code interpreter session
        self.code_interpreter_name = code_interpreter_name
        # The creation time of the code interpreter session, in ISO 8601 format
        self.created_at = created_at
        # The last update time of the code interpreter session, in ISO 8601 format
        self.last_updated_at = last_updated_at
        # The Unique Identifier of the code interpreter session
        # 
        # This parameter is required.
        self.session_id = session_id
        # The idle timeout duration of the code interpreter session, in seconds. After the instance receives no session requests, it enters an idle state, which is billed under the idle billing model. If the idle duration exceeds this timeout, the session automatically expires and can no longer be used.
        self.session_idle_timeout_seconds = session_idle_timeout_seconds
        # The current status of the code interpreter session
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_interpreter_id is not None:
            result['codeInterpreterId'] = self.code_interpreter_id

        if self.code_interpreter_name is not None:
            result['codeInterpreterName'] = self.code_interpreter_name

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.session_idle_timeout_seconds is not None:
            result['sessionIdleTimeoutSeconds'] = self.session_idle_timeout_seconds

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeInterpreterId') is not None:
            self.code_interpreter_id = m.get('codeInterpreterId')

        if m.get('codeInterpreterName') is not None:
            self.code_interpreter_name = m.get('codeInterpreterName')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

