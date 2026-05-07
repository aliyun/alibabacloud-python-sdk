# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetAvailableLLMModelsResponseBody(DaraModel):
    def __init__(
        self,
        models: List[str] = None,
        request_id: str = None,
    ):
        self.models = models
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.models is not None:
            result['Models'] = self.models

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Models') is not None:
            self.models = m.get('Models')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

