# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSilencePolicyResponseBody(DaraModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the silence policy was deleted successfully. Valid values:
        # 
        # *   `true`: The silence policy was deleted successfully.
        # *   `false`: The silence policy failed to be deleted.
        self.is_success = is_success
        # The operation that you want to perform. Set the value to **DeleteSilencePolicy**.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

