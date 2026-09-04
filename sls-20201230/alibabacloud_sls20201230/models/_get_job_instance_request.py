# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobInstanceRequest(DaraModel):
    def __init__(
        self,
        caller_owner: str = None,
    ):
        # The owner of the job.
        self.caller_owner = caller_owner

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller_owner is not None:
            result['callerOwner'] = self.caller_owner

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callerOwner') is not None:
            self.caller_owner = m.get('callerOwner')

        return self

