# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchDeleteKvWithHighCapacityResponseBody(DaraModel):
    def __init__(
        self,
        fail_keys: List[str] = None,
        request_id: str = None,
        success_keys: List[str] = None,
    ):
        # The keys that failed to be deleted.
        self.fail_keys = fail_keys
        # The request ID.
        self.request_id = request_id
        # The keys that are deleted.
        self.success_keys = success_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_keys is not None:
            result['FailKeys'] = self.fail_keys

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_keys is not None:
            result['SuccessKeys'] = self.success_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailKeys') is not None:
            self.fail_keys = m.get('FailKeys')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessKeys') is not None:
            self.success_keys = m.get('SuccessKeys')

        return self

