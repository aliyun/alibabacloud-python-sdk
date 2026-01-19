# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBackendModelResponseBody(DaraModel):
    def __init__(
        self,
        backend_model_id: str = None,
        request_id: str = None,
    ):
        self.backend_model_id = backend_model_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_model_id is not None:
            result['BackendModelId'] = self.backend_model_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendModelId') is not None:
            self.backend_model_id = m.get('BackendModelId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

