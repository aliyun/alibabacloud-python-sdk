# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableFunctionInvocationRequest(DaraModel):
    def __init__(
        self,
        abort_ongoing_request: bool = None,
        reason: str = None,
    ):
        # Specifies whether to immediately terminate all ongoing requests.
        self.abort_ongoing_request = abort_ongoing_request
        # The reason for disabling the function\\"s invocation.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abort_ongoing_request is not None:
            result['abortOngoingRequest'] = self.abort_ongoing_request

        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('abortOngoingRequest') is not None:
            self.abort_ongoing_request = m.get('abortOngoingRequest')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

