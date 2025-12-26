# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAlgorithmResponseBody(DaraModel):
    def __init__(
        self,
        algorithm_id: str = None,
        request_id: str = None,
    ):
        self.algorithm_id = algorithm_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_id is not None:
            result['AlgorithmId'] = self.algorithm_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmId') is not None:
            self.algorithm_id = m.get('AlgorithmId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

