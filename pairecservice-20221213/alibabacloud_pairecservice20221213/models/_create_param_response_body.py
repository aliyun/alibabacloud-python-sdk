# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateParamResponseBody(DaraModel):
    def __init__(
        self,
        param_id: int = None,
        request_id: str = None,
    ):
        self.param_id = param_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_id is not None:
            result['ParamId'] = self.param_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamId') is not None:
            self.param_id = m.get('ParamId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

