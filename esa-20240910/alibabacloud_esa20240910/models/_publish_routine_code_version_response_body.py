# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishRoutineCodeVersionResponseBody(DaraModel):
    def __init__(
        self,
        code_version: str = None,
        request_id: str = None,
    ):
        # The code version.
        self.code_version = code_version
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

