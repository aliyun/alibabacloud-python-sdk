# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetRoutineEnvironmentVariablesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        set_keys: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The list of environment variable keys that were set successfully.
        self.set_keys = set_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.set_keys is not None:
            result['SetKeys'] = self.set_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SetKeys') is not None:
            self.set_keys = m.get('SetKeys')

        return self

