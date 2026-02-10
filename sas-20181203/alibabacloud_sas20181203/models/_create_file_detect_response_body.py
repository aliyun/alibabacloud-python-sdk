# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFileDetectResponseBody(DaraModel):
    def __init__(
        self,
        hash_key: str = None,
        request_id: str = None,
    ):
        # The identifier of the file.
        self.hash_key = hash_key
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hash_key is not None:
            result['HashKey'] = self.hash_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

