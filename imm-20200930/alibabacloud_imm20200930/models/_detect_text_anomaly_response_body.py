# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetectTextAnomalyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        suggestion: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the text contains anomalies. Valid values:
        # 
        # *   pass: the text does not contain anomalies.
        # *   block: the text contains anomalies.
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

